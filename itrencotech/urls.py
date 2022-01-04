from django.urls import path

from . import views

app_name = 'itrencotech'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/ceo/', views.navbar_about_ceo, name='navbar_about_ceo'),
    path('about/history/', views.navbar_about_history, name='navbar_about_history'),
    path('about/ideology/', views.navbar_about_ideology, name='navbar_about_ideology'),
    path('about/route/', views.navbar_about_route, name='navbar_about_route'),
    path('production/home/', views.body_production_home, name='body_production_home'),
    path('production/mold/', views.body_production_mold, name='body_production_mold'),
    path('production/cnc/', views.body_production_cnc, name='body_production_cnc'),
    path('production/press/', views.body_production_press, name='body_production_press'),
]