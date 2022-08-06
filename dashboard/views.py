from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.decorators import login_required



class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = "dashboard/home.html"


class AboutView(TemplateView):
    template_name = "dashboard/about.html"


class PostDetailView(DetailView):
    model = Post


class pay(DetailView):
    model = Post
    template_name = "dashboard/pay.html"
