from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('body/onlyIdea/onlyIdea_home/', views.body_onlyIdea_onlyIdea, name='onlyIdea'),
    path('body/prototyping/prototyping_home/', views.body_prototyping_prototyping_home, name='prototyping'),
    
    
]