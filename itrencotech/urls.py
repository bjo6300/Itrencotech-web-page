from django.urls import path

from . import views

app_name = 'itrencotech'

urlpatterns = [
    path('', views.index, name='index'),
    path('navBar/about/ceo/', views.navbar_about_ceo, name='navbar_about_ceo'),
    path('navBar/about/history/', views.navbar_about_history, name='navbar_about_history'),
    path('navBar/about/ideology/', views.navbar_about_ideology, name='navbar_about_ideology'),
    path('navBar/about/route/', views.navbar_about_route, name='navbar_about_route'),
    path('body/production/home/', views.body_production_home, name='body_production_home'),
]