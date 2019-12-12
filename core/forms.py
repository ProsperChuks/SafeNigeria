# django imports
from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.forms.models import ModelChoiceField
from django.contrib.auth.models import Permission, Group

# project app imports
from core.models import Incident, State

# third party library imports
from django_select2.forms import Select2Widget
from django.core.exceptions import ValidationError


class UserAdminFormCustomizer(forms.ModelForm):
    """
    helps to customize user model admin page and remove 
    unwanted details
    """

    class Meta:
        model = Group
        fields = ('permissions',)

    ##### 
    ##### Learn how to configure permission field to accept blank
    ##### (not_required by default in admin page)

    # permissions = forms.ModelMultipleChoiceField(
    #     Permission.objects.exclude(
    #         content_type__app_label__in=[
    #             'auth','admin','sessions','contenttypes','users'
    #         ]),

    #     widget=admin.widgets.FilteredSelectMultiple(
    #         'permissions', 
    #         False
    #     )
    # )


class ReportForm(forms.ModelForm):
    """
    creates a form that will be used to create report
    """
    # using django-select2 to make form more elegant
    city = ModelChoiceField (
                queryset=State.objects.all(), widget=Select2Widget)
    class Meta:
        model = Incident
        fields = ('video', 'headline', 'city', 'location', 'description',)

    def clean_video(self):
        file = self.cleaned_data.get("video", False)

        # retrieve the file format from the uploaded file
        file_type = str(file)[len(str(file)) - 4:]
        
        # the format accepted as a video
        valid_formats = ['.mp4', '.webm', '.ogg']

        if not file_type in valid_formats :
            raise ValidationError("Invalid file. Please upload a video")
        return file
