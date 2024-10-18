from rest_framework import permissions
from .models import *

class CanSubmitSurvey(permissions.BasePermission):
    """
    Custom permission to check if the user has already filled the survey for a specific question.
    """

    def has_permission(self, request, view):
        # Get the question ID from the request payload (usually in POST data)
        question_id = request.data.get('question')
        # If question_id is not in the payload, deny permission
        if not question_id:
            return False

        # Check if the user has already submitted answers for this question
        # Assuming you have a model that tracks user responses (like Answer model)
        has_submitted = Answer.objects.filter(question_id=question_id, user=request.user).exists()
        # Allow if the user has not submitted; deny if they have
        return not has_submitted