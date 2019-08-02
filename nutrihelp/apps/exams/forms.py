from django import forms
from django.forms.fields import DateField

from .models import Exam, Question, AnsweredQuestion, Recommendation

BIRTH_YEAR_CHOICES = range(1940, 2019)


class TakeExamForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, empty_label=("Escoja un año", "Escoja un mes", "Escoja un día"),), label="Fecha de nacimiento")

    class Meta:
        model = Exam
        exclude = ['answered_questions', 'user', 'active', 'recommendation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in Question.objects.filter(active=True):
            self.fields[question.slug] = forms.ModelChoiceField(
                queryset=question.answers, empty_label="Seleccione una respuesta", label=question.question_text)

    def clean(self):
        # Nothing to clean
        pass

    def save(self, user):
        score = 0
        exam = self.instance
        exam.user = user
        exam.save()
        for question in Question.objects.filter(active=True):
            score += self.cleaned_data[question.slug].weight
            exam.answered_questions.add(
                question, through_defaults={'answer': self.cleaned_data[question.slug]})
        print(score)
        try:
            exam.recommendation = Recommendation.objects.get(
                upper__gte=score, lower__lte=score)
        except Exception:
            exam.recommendation = None
        exam.save(update_fields=['recommendation', ])
