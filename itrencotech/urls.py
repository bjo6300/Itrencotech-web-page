from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('body/onlyIdea/onlyIdea_home/', views.body_onlyIdea_onlyIdea, name='onlyIdea'),
    path('body/prototyping/prototyping_home/', views.body_prototyping_prototyping_home, name='prototyping'),

    path('body/onlyIdea/onlyIdea_mechanical_design/', views.body_onlyIdea_onlyIdea_mechanical_design, name='mechanical_design'), # 기계설계
    path('body/onlyIdea/onlyIdea_product_mechanism_design/', views.body_onlyIdea_onlyIdea_product_mechanism_design, name='product_mechanism_design'), # 제품기구설계
    path('body/onlyIdea/onlyIdea_production_design/', views.body_onlyIdea_onlyIdea_production_design, name='production_design'), # 제품디자인
    
    path('body/prototyping/3DPrinting/', views.body_prototyping_3Dprinting, name='3Dprinting'), # 3D 프린팅
    path('body/prototyping/mockUp/', views.body_prototyping_mockUp, name='mockUp'), # 목업
    path('body/prototyping/CNC/', views.body_prototyping_CNC, name='CNC'), # CNC 가공
    path('body/prototyping/sheeting_bending/', views.body_prototyping_sheeting_bending, name='sheeting_bending'), # 판금 절곡
    
]