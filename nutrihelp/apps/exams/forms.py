from django import forms
from django.forms.fields import DateField

from .models import Exam, Question


class TakeExamForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.SelectDateWidget(empty_label=("Escoja un año", "Escoja un mes", "Escoja un día"),), label="Fecha de nacimiento")

    class Meta:
        model = Exam
        exclude = ['answered_questions', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in Question.objects.filter(active=True):
            self.fields[question.slug] = forms.ModelChoiceField(
                queryset=question.answers, empty_label="Seleccione una respuesta", label=question.question_text)

    def clean(self):
        print('In cleaning')

    def save(self):
        print('in save.....')
        # profile = self.instance
        # profile.first_name = self.cleaned_data[“first_name”]
        # profile.last_name = self.cleaned_data[“last_name”]

        # profile.interest_set.all().delete()
        # for interest in self.cleaned_data[“interests”]:
        #     ProfileInterest.objects.create(
        #         profile=profile,
        #         interest=interest,
        #     )
