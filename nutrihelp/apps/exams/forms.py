from django import forms
from django.forms.fields import DateField

from .models import Exam, Question, AnsweredQuestion


class TakeExamForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.SelectDateWidget(empty_label=("Escoja un año", "Escoja un mes", "Escoja un día"),), label="Fecha de nacimiento")

    class Meta:
        model = Exam
        exclude = ['answered_questions', 'user', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in Question.objects.filter(active=True):
            self.fields[question.slug] = forms.ModelChoiceField(
                queryset=question.answers, empty_label="Seleccione una respuesta", label=question.question_text)

    def clean(self):
        # Nothing to clean
        pass

    def save(self, user):
        exam = self.instance
        exam.user = user
        exam.save()
        for question in Question.objects.filter(active=True):
            exam.answered_questions.add(
                question, through_defaults={'answer': self.cleaned_data[question.slug]})
        # profile = self.instance
        # profile.first_name = self.cleaned_data[“first_name”]
        # profile.last_name = self.cleaned_data[“last_name”]

        # profile.interest_set.all().delete()
        # for interest in self.cleaned_data[“interests”]:
        #     ProfileInterest.objects.create(
        #         profile=profile,
        #         interest=interest,
        #     )