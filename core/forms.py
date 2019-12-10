# django imports
from django import forms
from django.contrib import admin
from django.forms.models import ModelChoiceField
from django.contrib.auth.models import Permission, Group

# project app imports
from core.models import Incident, State

# third party library imports
from django_select2.forms import Select2Widget


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
        fields = ('video', 'city', 'headline', 'description',)
