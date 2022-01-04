from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('portfolio/', views.portfolio),
    path('review/', views.review)
]