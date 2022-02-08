from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import SignUpView

app_name = 'common'

urlpatterns = [

    path('login/', views.login_main, name='login_main'),
    # path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login_main'),  # 로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # 로그아웃

    # path('logout/', views.logout_main, name='logout'),

    # path('signUp/', views.signUp, name='signUp'),  # 회원가입 페이지
    path('signUp/', SignUpView.as_view(), name='signUp'),
    path('signUp/completed', views.signUpCompleted, name='signUp_completed'),  # 회원가입 완료 페이지

    # 찾기
    path('find_id_passwd/', views.findIdPasswd, name='find_id_passwd'),  # 아이디/비밀번호 찾기 선택
    path('find_id/', views.findId, name='find_id'),  # 아이디 찾기
    path('find_id/phone', views.findIdPhone, name='find_id_phone'),  # 아이디 찾기 - 휴대폰 번호로 찾기
    path('find_id/email', views.verification, name='find_id_email'),  # 아이디 찾기 - 이메일로 찾기

    path('find_id/email2', views.verification2, name='find_id_email2'),  # 아이디 찾기 - 이메일로 찾기2

    path('find_id/phone/id_list', views.findIdListbyPhone, name='find_id_list_by_phone'),  # 아이디 찾기 - 전화번호로 찾은 아이디 목록
    path('find_id/email/id_list', views.findIdListbyEmail, name='find_id_list_by_email'),  # 아이디 찾기 - 이메일로 찾은 아이디 목록

    path('find_passwd/', views.findPasswd, name='find_passwd'),  # 비밀번호 찾기 - 아이디 입력
    path('find_passwd/id_list', views.findPasswdIdList, name='find_passwd_id_list'),  # 비밀번호 찾기 - 아이디 목록
    path('find_passwd/phone', views.findPasswdPhone, name='find_passwd_phone'),  # 비밀번호 찾기 - 휴대폰 번호로 찾기
    path('find_passwd/email', views.findPasswdEmail, name='find_passwd_email'),  # 비밀번호 찾기 - 이메일로 찾기
    path('find_passwd/reset', views.findPasswdReset, name='find_passwd_reset'),  # 비밀번호 찾기 - 재설정
    path('find_passwd/completed', views.findPasswdCompleted, name='find_passwd_completed'),  # 비밀번호 찾기 - 재설정


    # 이메일 인증
    # path('activate/<str:uidb64>/<str:token>/', Activate.as_view())
