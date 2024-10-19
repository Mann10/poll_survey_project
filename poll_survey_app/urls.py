from django.urls import path
from .views import PollListCreateView, QuestionListCreateView, ChoiceListCreateView, AnswerListCreateView,PollResultChartView


urlpatterns = [
    path('',Homepage.as_view(),name='homepage'),
    path('polls/', PollListCreateView.as_view(), name='polls'),
    path('polls/<int:pk>/', PollListCreateView.as_view(), name='polls'),
    path('questions/', QuestionListCreateView.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionListCreateView.as_view(), name='questions'),
    path('choices/', ChoiceListCreateView.as_view(), name='choices'),
    path('choices/<int:pk>/', ChoiceListCreateView.as_view(), name='choices'),
    path('answers/', AnswerListCreateView.as_view(), name='answers'),
    path('polls/<int:poll_id>/chart/', PollResultChartView.as_view(), name='poll_results_chart')
]
