from django.db import models

from ..core.models import AbstractHistory


class Question(AbstractHistory):
    question_text = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Pregunta")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"


class Answer(AbstractHistory):
    answer_text = models.CharField(max_length=20, blank=True,
                                   null=True, verbose_name="Respuesta")
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name="Pregunta", related_name='answers')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
