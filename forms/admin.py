from django.contrib import admin
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from .models import *


# Register your models here.


class FormsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "description", "confirmationMsg")}),
        (
            "Техническая информация",
            {"fields": ("id", "creator", "createdAt", "updatedAt")},
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser is not True:
            self.readonly_fields = ("id", "creator", "createdAt", "updatedAt")
        else:
            self.readonly_fields = ("id", "createdAt", "updatedAt")
        return super(FormsAdmin, self).get_form(request, obj)

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(FormsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("question", "question_type", "description", "form")}),
        ("Техническая информация", {"fields": ("id", "creator")}),
    )

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser is not True:
            self.readonly_fields = ("id", "creator")
        else:
            self.readonly_fields = ("id",)
        form = super(QuestionsAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_superuser is not True:
            form.base_fields["form"].queryset = Forms.objects.filter(
                creator=request.user
            )
        return form

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(QuestionsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)


class ChoicesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("choice", "question")}),
        ("Техническая информация", {"fields": ("id", "creator")}),
    )

    def get_form(self, request, obj=None, **kwargs):

        if request.user.is_superuser is not True:
            self.readonly_fields = ("id", "creator")
        else:
            self.readonly_fields = ("id",)
        form = super(ChoicesAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_superuser is not True:
            form.base_fields["question"].queryset = Questions.objects.filter(
                creator=request.user
            )
        return form

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ChoicesAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)


admin.site.register(Forms, FormsAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(UserAnswers)
