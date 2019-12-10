from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView

from core.models import Incident
from core import forms


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_incidents'] = Incident.objects.all()[:3]
        return context


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


class NewFeedView(ListView):
    model = Incident
    paginate_by = 30
    template_name = 'core/news.html'