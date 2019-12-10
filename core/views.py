from django.shortcuts import render
from django.views.generic import TemplateView, FormView


class HomePageView(TemplateView):
    template_name = 'core/home.html'

class ReportPageView(TemplateView):
    template_name = 'core/reports.html'    
