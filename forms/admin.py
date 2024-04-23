from django.contrib import admin

from .models import *

# Register your models here.


class FormsAdmin(admin.ModelAdmin):
    """ """

    fieldsets = (
        (
            None,
            {
                "fields":
                ("title", "description", "confirmationMsg", "only_logged_in")
            },
        ),
        (
            "Техническая информация",
            {
                "fields": ("id", "creator", "createdAt", "updatedAt")
            },
        ),
    )

    list_display = ("title", "id", "creator", "createdAt", "only_logged_in")
    list_display_links = ("title", "id")
    list_editable = ["only_logged_in"]
    list_filter = ["only_logged_in"]
    list_per_page = 5
    ordering = ["title"]
    search_fields = ("title", "id", "creator__username")

    def get_form(self, request, obj=None, **kwargs):
        """

        :param request: param obj:  (Default value = None)
        :param obj: Default value = None)
        :param **kwargs:

        """
        if request.user.is_superuser is not True:
            self.readonly_fields = ("id", "creator", "createdAt", "updatedAt")
        else:
            self.readonly_fields = ("id", "createdAt", "updatedAt")
        return super(FormsAdmin, self).get_form(request, obj)

    def save_model(self, request, obj, form, change):
        """

        :param request: param obj:
        :param form: param change:
        :param obj: param change:
        :param change:

        """
        obj.creator = request.user
        obj.save()

    def get_queryset(self, request):
        """

        :param request:

        """
        qs = super(FormsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)


class QuestionsAdmin(admin.ModelAdmin):
    """ """

    fieldsets = (
        (None, {
            "fields": ("question", "type", "description", "form", "required")
        }),
        ("Техническая информация", {
            "fields": ("id", "creator")
        }),
    )

    list_display = ("question", "id", "form", "type", "creator", "required")
    list_display_links = ("question", "id")
    list_editable = ["required"]
    list_filter = ("required", "type")
    list_per_page = 10
    ordering = ["question", "form__title"]
    search_fields = ("question", "id", "form__title")

    def get_form(self, request, obj=None, **kwargs):
        """

        :param request: param obj:  (Default value = None)
        :param obj: Default value = None)
        :param **kwargs:

        """
        if request.user.is_superuser is not True:
            self.readonly_fields = ("id", "creator")
        else:
            self.readonly_fields = ("id", )
        form = super(QuestionsAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_superuser is not True:
            form.base_fields["form"].queryset = Forms.objects.filter(
                creator=request.user)
        return form

    def save_model(self, request, obj, form, change):
        """

        :param request: param obj:
        :param form: param change:
        :param obj: param change:
        :param change:

        """
        obj.creator = request.user
        obj.save()

    def get_queryset(self, request):
        """

        :param request:

        """
        qs = super(QuestionsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)


class ChoicesAdmin(admin.ModelAdmin):
    """ """

    fieldsets = (
        (None, {
            "fields": ("choice", "question")
        }),
        ("Техническая информация", {
            "fields": ("id", "creator")
        }),
    )

    list_display = ("choice", "id", "question", "creator")
    list_display_links = ("choice", "id")
    list_filter = ["question__type"]
    list_per_page = 5
    ordering = [
        "choice", "question", "question__form", "question__type", "creator"
    ]
    search_fields = ("choice", "id", "question__question")

    def get_form(self, request, obj=None, **kwargs):
        """

        :param request: param obj:  (Default value = None)
        :param obj: Default value = None)
        :param **kwargs:

        """

        if request.user.is_superuser is not True:
            self.readonly_fields = ("id", "creator")
        else:
            self.readonly_fields = ("id", )
        form = super(ChoicesAdmin, self).get_form(request, obj, **kwargs)
        if request.user.is_superuser is not True:
            form.base_fields["question"].queryset = Questions.objects.filter(
                creator=request.user)
        return form

    def save_model(self, request, obj, form, change):
        """

        :param request: param obj:
        :param form: param change:
        :param obj: param change:
        :param change:

        """
        obj.creator = request.user
        obj.save()

    def get_queryset(self, request):
        """

        :param request:

        """
        qs = super(ChoicesAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(creator=request.user)


class AnswersAdmin(admin.ModelAdmin):
    list_display = ("choice", "id", "question", "session_id", "user")
    list_display_links = ['id']
    search_fields = ("choice", "id", "question", "session_id", "user")


admin.site.register(Forms, FormsAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(Answers, AnswersAdmin)
