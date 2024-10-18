from rest_framework import generics
from .models import Poll, Question, Choice, Answer
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView

import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse

from .permissions import CanSubmitSurvey


class PollListCreateView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

class QuestionListCreateView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class ChoiceListCreateView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]

class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,CanSubmitSurvey]
    

class PollResultChartView(APIView):
    def get(self, request, poll_id):
        # Get poll and related questions
        poll = Poll.objects.get(id=poll_id)
        questions = poll.questions.all()

        # Create a figure for the chart
        plt.figure(figsize=(10, 6))

        for idx, question in enumerate(questions):
            if question.choices.exists():
                # Handle MCQ questions
                labels = [choice.text for choice in question.choices.all()]
                votes = [Answer.objects.filter(question=question, choice=choice).count() for choice in question.choices.all()]

                # Add a bar chart for each MCQ question
                plt.subplot(len(questions), 1, idx + 1)
                plt.bar(labels, votes)
                plt.title(f"MCQ: {question.text}")
                plt.xlabel("Choices")
                plt.ylabel("Votes")
            else:
                # If no choices exist (though we assume this won't happen), display a message
                plt.subplot(len(questions), 1, idx + 1)
                plt.text(0.5, 0.5, "No choices available", horizontalalignment='center', verticalalignment='center', fontsize=12)
                plt.axis('off')
                plt.title(f"Question: {question.text}")

        # Save the chart as an image in memory
        buffer = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Convert image to base64
        image_png = buffer.getvalue()
        buffer.close()

        response = HttpResponse(image_png, content_type='image/png')
        return response
    
    
