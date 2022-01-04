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
    path('review/', views.review, name='review'),

    path('onlyIdea/onlyIdea_home/', views.body_onlyIdea_onlyIdea, name='onlyIdea'),
    path('prototyping/prototyping_home/', views.body_prototyping_prototyping_home, name='prototyping'),

    path('onlyIdea/onlyIdea_mechanical_design/',
            views.body_onlyIdea_onlyIdea_mechanical_design, name='mechanical_design'), # 기계설계
    path('onlyIdea/onlyIdea_product_mechanism_design/',
            views.body_onlyIdea_onlyIdea_product_mechanism_design, name='product_mechanism_design'), # 제품기구설계
    path('onlyIdea/onlyIdea_production_design/',
            views.body_onlyIdea_onlyIdea_production_design, name='production_design'), # 제품디자인
    
    path('prototyping/3DPrinting/', views.body_prototyping_3Dprinting, name='3Dprinting'), # 3D 프린팅
    path('prototyping/mockUp/', views.body_prototyping_mockUp, name='mockUp'), # 목업
    path('prototyping/CNC/', views.body_prototyping_CNC, name='CNC'), # CNC 가공
    path('prototyping/sheeting_bending/', 
            views.body_prototyping_sheeting_bending, name='sheeting_bending'),  # 판금 절곡
    
    path('about/ceo/', views.navbar_about_ceo, name='navbar_about_ceo'),
    path('about/history/', views.navbar_about_history, name='navbar_about_history'),
    path('about/ideology/', views.navbar_about_ideology, name='navbar_about_ideology'),
    path('about/route/', views.navbar_about_route, name='navbar_about_route'),

    path('production/home', views.body_production_home, name='body_production_home'),
    path('production/mold/', views.body_production_mold, name='body_production_mold'),
    path('production/cnc/', views.body_production_cnc, name='body_production_cnc'),
    path('production/press/', views.body_production_press, name='body_production_press'),

]