from django import forms
from django.contrib import admin
from django.contrib.auth.models import Permission, Group

from core.models import Incident


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
    class Meta:
        model = Incident
        fields = ('video', 'city', 'headline', 'description',)
        