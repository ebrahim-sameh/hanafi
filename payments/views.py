from django.shortcuts import render
from dashboard.models import Post
from django.views.generic import DetailView

# Create your views here.


# def index(request,  *args, **kwargs):
#     return render(request, 'payments/index.html')

class pay(DetailView):
    model = Post
    template_name = "payments/index.html"