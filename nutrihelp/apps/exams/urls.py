from django.urls import path

from .views import TakeExamView

app_name = 'exams'

urlpatterns = [
    path('', TakeExamView.as_view(), name="take"),
]
