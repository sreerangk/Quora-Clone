from django.urls import path
from .views import (register, user_login, user_logout, QuestionListView, question_detail,ask_question, like_answer)

urlpatterns = [
    path('', QuestionListView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('question/<int:pk>/', question_detail, name='question-detail'),
    path('ask/', ask_question, name='ask-question'),
    path('like/<int:pk>/', like_answer, name='like-answer'),
]