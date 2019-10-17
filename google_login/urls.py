from django.urls import path
from . import views


urlpatterns = [
    path('', views.glogin, name='glogin'),
    path('accounts/profile/', views.login_success, name='login_success') 
]