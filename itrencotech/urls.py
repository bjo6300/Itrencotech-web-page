from django.urls import path

from . import views

app_name = 'itrencotech'

urlpatterns = [
    path('', views.index, name='index'),

    # 포트폴리오
    path('portfolio/', views.portfolio, name='portfolio'), # 포트폴리오 홈
    path('portfolio/design', views.portfolioDesign, name='portfolio_design'),  # 제품 디자인
    path('portfolio/machineDesign', views.portfolioMachineDesign, name='portfolio_machine_design'), # 기계시스템 설계
    path('portfolio/HW_machine', views.portfolioHWmachine, name='portfolio_HW_machine'),  # HW 기구설계

    path('portfolio/3d', views.portfolio3d, name='portfolio_3d'), # 3D 프린팅
    path('portfolio/mockup', views.portfolioMockup, name='portfolio_mockup'),  # 목업 CNC 가공
    path('portfolio/cnc', views.portfolioCnc, name='portfolio_cnc'), # 부품 CNC 가공
    path('portfolio/sdm', views.portfolioSdm, name='portfolio_sdm'), # Smart Digital Mold

    path('portfolio/mold', views.portfolioMold, name='portfolio_mold'), # 금형 제작
    path('portfolio/injection_molding', views.portfolioInjectionMolding, name='portfolio_injection_molding'), # 사출 성형
    path('portfolio/equipmentDesign', views.portfolioEquipmentDesign, name='portfolio_equipment_design'),  # 판금 절곡

    
    # 고객 후기
    path('review/best', views.reviewBest, name='review_best'), # 베스트 후기
    path('review/recent', views.reviewRecent, name='review_recent'), # 최신순
    path('review/highRating', views.reviewHighRating, name='review_high_rating'), # 평점높은순
    path('review/lowRating', views.reviewLowRating, name='review_low_rating'), # 평점낮은순


    # ONLY IDEA
    path('onlyIdea/onlyIdea_home/', views.body_onlyIdea_onlyIdea, name='onlyIdea'), # ONLY IDEA 홈
    path('onlyIdea/onlyIdea_detail/', views.onlyIdea_detail, name='onlyIdea_detail'), # 상세설명


    # 시제품 제작
    path('prototyping/prototyping_home/', views.body_prototyping_prototyping_home, name='prototyping'), # 시제품 제작 홈
    path('prototyping/prototyping_detail/', views.prototyping_detail, name='prototyping_detail'), # 상세설명


    # 양산
    path('production/home', views.body_production_home, name='body_production_home'),  # 양산 홈
    path('production/production_detail/', views.production_detail, name='production_detail'), # 상세설명


    # 회사 소개
    path('about/ceo/', views.navbar_about_ceo, name='navbar_about_ceo'),
    path('about/history/', views.navbar_about_history, name='navbar_about_history'),
    path('about/ideology/', views.navbar_about_ideology, name='navbar_about_ideology'),
    path('about/route/', views.navbar_about_route, name='navbar_about_route'),
    path('about/test/', views.navbar_about_test, name='navbar_about_test'),


    # 주문
    path('order/order_home/', views.order_home, name='order_home'),
    path('order/order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order/order_form_onlyIdea/', views.order_form_onlyIdea, name='order_form_onlyIdea'),
    path('order/order_form_prototyping/', views.order_form_prototyping, name='order_form_prototyping'),
    path('order/order_form_production/', views.order_form_production, name='order_form_production'),

    # 마이페이지

    path('navBar/mypage/mypage_home/', views.mypage_home, name='mypage_home'),
    path('navBar/mypage/mypage_order_history/', views.mypage_order_history, name='mypage_order_history'),
    path('navBar/mypage/mypage_info/', views.mypage_info, name='mypage_info'),
    path('myPage/myPage_update_info/', views.myPage_update_info, name='myPage_update_info'),

]
