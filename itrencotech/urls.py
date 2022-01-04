from django.urls import path

from . import views

app_name = 'itrencotech'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('findIdPasswd/', views.findIdPasswd, name='findIdPasswd'),
    path('findId/', views.findId, name='findId'),

]