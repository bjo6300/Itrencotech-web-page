
# 로그인/회원가입 ---------------------------------------
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from common.models import User

# 이메일 인증 -------------------------------------------
import jwt
import json
import ctypes

from .mail import email_auth_num
from .token import common_activation_token
from .text import message
from config.my_settings import SECRET_KEY, EMAIL

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text

from django.contrib import messages

# ------------------------------------------------------

""" ───────────────────────── 로그인/회원가입 ───────────────────────── """

def login_main(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, userid=userid, password=password)

        if user is None:
            return render(request, 'login/login.html', {'error': 'username or password가 틀렸습니다.'})
        else:
            auth.login(request, user)
            return redirect('/')
    elif request.method == 'GET':
        return render(request, 'login/login.html')


# 이메일 인증 적용 중인 회원가입 클래스
class SignUpView(View):
    # POST 요청 시
    def post(self, request):
        username = request.POST.get('username', None)  # 이름
        userid = request.POST.get('userid', None)  # 아이디
        password1 = request.POST.get('password1', None)  # 비밀번호
        phone_num = request.POST.get('phone_num', None)  # 휴대전화
        password2 = request.POST.get('password2', None)  # 비밀번호(확인)
        company_name = request.POST.get('company_name', None)  # 회사명
        company_address = request.POST.get('company_address', None)  # 회사 주소
        company_tel = request.POST.get('company_tel', None)  # 회사 전화
        email = request.POST.get('email', None)  # 이메일
        res_data = {}

        # 빈 칸 확인
        if not (username and userid and password1 and password2 and phone_num
                and company_name and company_address and company_tel and email):
            res_data['error'] = "입력하지 않은 칸이 있습니다."
        # 아이디 중복 확인
        if User.objects.filter(userid=userid).exists():  # 아이디 중복 체크
            print('이미 존재하는 아이디입니다!')
            messages.warning(request, '이미 존재하는 아이디입니다!')
            return render(request, 'login/signup.html')
        # 비밀번호 일치 여부 확인
        if password1 != password2:
            print('비밀번호가 일치하지 않습니다.')
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        user = User.objects.create_user(userid=userid, username=username,
                                        phone_num=phone_num, company_name=company_name,
                                        company_address=company_address, company_tel=company_tel,
                                        email=email, password=password1)
        user.save()
        return render(request, 'login/signUp_completed.html', res_data)

    # GET 요청 시(회원가입 버튼 클릭 등)
    def get(self, request):
        return render(request, 'login/signup.html')


# ---------------------------------------------------------------------------------------------------------------------


def signUpCompleted(request):
    """ 회원가입 완료 페이지 """
    return render(request, 'login/signUp_completed.html')


def findIdPasswd(request):
    """ 아이디 / 비밀번호 찾기 페이지 """
    return render(request, 'login/find_id_passwd.html')


""" ───────────────────────── 아이디 찾기 ───────────────────────── """


def findId(request):
    """ 아이디 찾기 페이지 """
    return render(request, 'login/find_id.html')


def findIdPhone(request):
    """ 아이디 찾기 - 휴대폰 번호로 찾기 """
    return render(request, 'login/find_id_phone.html')


def findIdEmail(request):
    """ 아이디 찾기 - 이메일로 찾기 """
    return render(request, 'login/find_id_email.html')


def findIdListbyPhone(request):
    """ 아이디 찾기 - 전화번호로 찾은 아이디 목록 """
    context = {'by': "전화번호"}
    return render(request, 'login/find_id_list.html', context)


def findIdListbyEmail(request):
    """ 아이디 찾기 - 이메일로 찾은 아이디 목록 """
    context = {'by': "이메일"}
    return render(request, 'login/find_id_list.html', context)


""" ───────────────────────── 비밀번호 찾기 ───────────────────────── """


def findPasswd(request):
    """ 비밀번호 찾기 페이지 """
    return render(request, 'login/find_passwd.html')


def findPasswdIdList(request):
    """ 비밀번호 찾기 - 아이디 목록 페이지 """
    return render(request, 'login/find_passwd_id_list.html')


def findPasswdPhone(request):
    """ 비밀번호 찾기 - 휴대폰 번호로 찾기 """
    return render(request, 'login/find_passwd_phone.html')


def findPasswdEmail(request):
    """ 비밀번호 찾기 - 이메일로 찾기 """
    return render(request, 'login/find_passwd_email.html')


def findPasswdReset(request):
    """ 비밀번호 찾기 - 비밀번호 재설정 """
    return render(request, 'login/find_passwd_reset.html')


def findPasswdCompleted(request):
    """ 비밀번호 찾기 - 비밀번호 재설정 완료 """
    return render(request, 'login/find_passwd_completed.html')


def verification(request):
    """ 이메일 인증 """
    if request.method == 'POST':
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        input_email = email1+'@'+email2

        # 이메일이 있으면
        if User.objects.filter(email=input_email).exists():
            # ctypes.windll.user32.MessageBoxW(0, '인증번호가 전송되었습니다.', '이메일 인증 창            ')
            # messages.add_message(request, messages.INFO, '테스트')

            users = User.objects.filter(email=input_email)

            auth_num = email_auth_num()
            EmailMessage(subject='이메일 인증 코드입니다.',
                         body=f'다음의 코드를 입력하세요\n{auth_num}',
                         to=[input_email]).send()

            for user in users:
                user.auth_num = auth_num
                user.save()
        # 이메일이 없으면
        else:
            # 없다고 알림창을 띄워야 함
            ctypes.windll.user32.MessageBoxW(0, '이메일 없음', '이메일 인증 창            ')

        return render(request, 'login/find_id_email.html', {'email1': email1, 'email2': email2})
    elif request.method == 'GET':
        return render(request, 'login/find_id_email.html')


def verification2(request):
    if request.method == 'POST':
        email1 = request.POST.get('email1', None)
        email2 = request.POST.get('email2', None)
        auth_num = request.POST.get('auth_num', None)
        input_email = email1 + '@' + email2

        if User.objects.filter(email=input_email).exists():
            users = User.objects.filter(email=input_email)

            if users[0].auth_num == auth_num:
                for user in users:
                    user.auth_num = None
                    user.save()
                return render(request, 'login/find_id_list.html', {'users': users})
            else:
                ctypes.windll.user32.MessageBoxW(0, '인증번호가 틀렸습니다.', '이메일 인증 창            ')
                return render(request, 'login/find_id_email.html', {'email1': email1, 'email2': email2})
        else:
            print('가입된 이메일이 없습니다.')
            return render(request, 'login/find_id_email.html')
    elif request.method == 'GET':
        return render(request, 'login/find_id_email.html')


