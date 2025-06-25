from django.urls import path
from .import views
urlpatterns = [
    
    path('', views.studentView, name='studentView'),
    
]