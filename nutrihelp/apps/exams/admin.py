from django.contrib import admin

from .models import (Question, Answer)


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'active', 'created_at')
    list_filter = ['question_text', 'active', ]
    search_fields = ('question_text', )
    actions_on_top = True
    actions_on_bottom = True
    inlines = [
        AnswerInline,
    ]
