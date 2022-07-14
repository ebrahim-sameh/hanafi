from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "dashboard/home.html"

class AboutView(TemplateView):
    template_name = "dashboard/about.html"
