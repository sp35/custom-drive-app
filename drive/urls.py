from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'drive-home'),
    path('upload/<int:pk>/download', views.download, name = 'file-download'),
	path('user_uploads/', views.user_uploads, name = 'drive-user-upload'),    
]

