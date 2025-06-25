from django.urls import path
from .import views
urlpatterns = [
    
    path('studentList', views.studentViewAPI, name='studentViewAPI'),
    path('studentDetailViewAPI/<int:pk>', views.studentDetailViewAPI, name='studentDetailViewAPI'),
    
]