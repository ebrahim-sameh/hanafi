from django.urls import path
from django.urls import path

from dashboard import views
from .views import HomeView, AboutView
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',HomeView.as_view(),name='dashboard-home'),
    path('about/', AboutView.as_view(), name='dashboard-about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]

