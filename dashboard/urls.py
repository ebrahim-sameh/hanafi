from django.urls import path, include
from .views import HomeView, AboutView, PostDetailView,pay
from users import views as user_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =[
    path('',HomeView.as_view(),name='dashboard-home'),
    path('about/', AboutView.as_view(), name='dashboard-about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('course/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('course/<int:pk>/pay/',pay.as_view() , name='pay'),
    path('',include('payments.urls'))


]

