from django.urls import path

from .views import TakeExamView, RecommendationView

app_name = 'exams'

urlpatterns = [
    path('', TakeExamView.as_view(), name="take"),
    path('recomendacion/<slug:slug>',
         RecommendationView.as_view(), name="recommendation"),
]
