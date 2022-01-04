from django.urls import path

from . import views

app_name = 'itrencotech'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/3d', views.portfolio3d, name='portfolio_3d'),
    path('portfolio/cnc', views.portfolioCnc, name='portfolio_cnc'),
    path('portfolio/mockup', views.portfolioMockup, name='portfolio_mockup'),
    path('portfolio/mold', views.portfolioMold, name='portfolio_mold'),
    path('review/', views.review, name='portfolio_review'),
]