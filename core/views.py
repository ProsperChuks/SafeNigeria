from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from core import forms


class HomePageView(TemplateView):
    template_name = 'core/home.html'

class ReportPageView(FormView):
    template_name = 'core/reports.html'
    form_class = forms.ReportForm
    context_object_name = 'form'
    success_url = '/'

    def form_valid(self, form):
        """
        when form is valid, then save the form
        """
        incident = form.save(commit=False)
        incident.user = self.request.user
        incident.save()
        return super().form_valid(form)
    
