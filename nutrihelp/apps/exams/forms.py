from django import forms

from .models import Exam, Question


class TakeExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        exclude = ['answered_questions', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for question in Question.objects.filter(active=True):
            self.fields[question.question_text] = forms.ModelChoiceField(
                queryset=question.answers, empty_label="Seleccione una respuesta", label=question.question_text)

    def clean(self):
        for question in Question.objects.filter(active=True):
            while self.cleaned_data.get(question.question_text):
                pass
                # def clean(self):
                #     interests = set()
                #     i = 0
                #     field_name = 'interest_%s' % (i,)
                #     while self.cleaned_data.get(field_name):
                #        interest = self.cleaned_data[field_name]
                #        if interest in interests:
                #            self.add_error(field_name, 'Duplicate')
                #        else:
                #            interests.add(interest)
                #        i += 1
                #        field_name = 'interest_%s' % (i,)
                #    self.cleaned_data[“interests”] = interests

                # def save(self):
                #     profile = self.instance
                #     profile.first_name = self.cleaned_data[“first_name”]
                #     profile.last_name = self.cleaned_data[“last_name”]

                #     profile.interest_set.all().delete()
                #     for interest in self.cleaned_data[“interests”]:
                #        ProfileInterest.objects.create(
                #            profile=profile,
                #            interest=interest,
                #        )
