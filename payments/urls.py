from django.urls import path
from . import views
from .views import pay

urlpatterns = [
    path('course/<int:pk>/pay/',pay.as_view(), name='pay'),
]
