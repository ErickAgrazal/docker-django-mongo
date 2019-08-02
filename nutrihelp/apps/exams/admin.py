from django.contrib import admin

from .models import (Question, Answer, Exam, AnsweredQuestion, Recommendation)


class AnswerInline(admin.TabularInline):
    model = Answer


class AnsweredQuestionInline(admin.TabularInline):
    model = AnsweredQuestion
    exclude = ['active', ]


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


@admin.register(Exam)
class ExamsTakenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ['user', ]
    search_fields = ('user', )
    actions_on_top = True
    actions_on_bottom = True
    inlines = [
        AnsweredQuestionInline,
    ]


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('title', 'upper', 'bottom')
    # list_filter = []
    actions_on_top = True
    actions_on_bottom = True
