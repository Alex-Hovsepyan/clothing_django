from django.urls import path
from . import views

urlpatterns = [
    path('forlogin/login/', views.login_request, name='login'),
    path('forlogin/register/',views.register_request, name='register'),
    path('forlogin/logout', views.logout_request, name='logout'),
]