from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

from ..core.models import AbstractHistory


class Question(AbstractHistory):
    question_text = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Pregunta")
    slug = AutoSlugField(populate_from='question_text')

    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"


class Answer(AbstractHistory):
    answer_text = models.CharField(max_length=200, blank=True,
                                   null=True, verbose_name="Respuesta")
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name="Pregunta", related_name='answers')
    weight = models.IntegerField(default=10, verbose_name="Puntaje")
    slug = AutoSlugField(populate_from='answer_text')

    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"


class Exam(AbstractHistory):
    SINGLE = 'SO'
    MARRIED = 'CA'
    DIVORCED = 'DI'
    WIDOWER = 'VI'
    CIVIL_STATUSES = [
        (SINGLE, 'Solter@'),
        (MARRIED, 'Casad@'),
        (DIVORCED, 'Divorciad@'),
        (WIDOWER, 'Viud@'),
    ]
    name = models.CharField(max_length=20, blank=True,
                            null=True, verbose_name="Nombre")
    last_name = models.CharField(max_length=20, blank=True,
                                 null=True, verbose_name="Apellidos")
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="Fecha de nacimiento")
    contact = models.CharField(max_length=20, blank=True,
                               null=True, verbose_name="Contacto")
    civil_status = models.CharField(
        max_length=2,
        choices=CIVIL_STATUSES,
        default=SINGLE,
        verbose_name="Estado civil"
    )
    live_accompanied = models.BooleanField(
        verbose_name='¿Vive acompañado?', default=True)
    disease = models.BooleanField(
        verbose_name='¿Sufre de alguna enfermedad?', default=True)
    drugs = models.TextField(verbose_name="¿Qué medicamentos toma?")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario")
    answered_questions = models.ManyToManyField(
        Question, verbose_name="Respuesta de pregunta", through='AnsweredQuestion')
    recommendation = models.ForeignKey(
        'Recommendation', null=True, blank=True,
        on_delete=models.CASCADE, verbose_name="Recomendación")
    slug = AutoSlugField(populate_from='user')

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Exámen"
        verbose_name_plural = "Exámenes"


class AnsweredQuestion(AbstractHistory):
    exam = models.ForeignKey(Exam, null=True, blank=True, on_delete=models.CASCADE,
                             verbose_name="Examen", related_name='+')
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE,
                                 verbose_name="Pregunta", related_name='+')
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name="Respuesta", related_name='+')

    def __str__(self):
        return "{}-{}-{}".format(self.exam, self.question, self.answer)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Repuesta a pregunta"
        verbose_name_plural = "Respuesta a preguntas"


class Recommendation(AbstractHistory):
    upper = models.IntegerField(default=100, verbose_name="Puntaje superior")
    lower = models.IntegerField(default=0, verbose_name="Puntaje inferior")
    title = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name="Título")
    content = HTMLField(verbose_name="Contenido")
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Recomendación"
        verbose_name_plural = "Recomendaciones"
