from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import views from the current directory

urlpatterns = [
    # Add other URL patterns here
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/', views.user_list, name='user_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
