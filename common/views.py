
# 로그인/회원가입 ---------------------------------------
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from common.models import User

# 이메일 인증 -------------------------------------------
import jwt
import json

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

# ------------------------------------------------------


""" ───────────────────────── 로그인/회원가입 ───────────────────────── """

def login_main(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, userid=userid, password=password)

        if user is None:
            # print('userid 또는 password가 틀렸습니다.')
            return render(request, 'login/login.html', {'error': 'username 또는 password가 틀렸습니다.'})
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
        # 이메일 인증
        try:
            validate_email(email)
            if User.objects.filter(email=email).exists():
                messages.warning(request, '이미 회원가입이 되어 있는 이메일입니다!')
                return JsonResponse({"message": "EXISTS_EMAIL"}, status=400)
            user = User.objects.create_user(userid=userid, username=username,
                                            phone_num=phone_num, company_name=company_name,
                                            company_address=company_address, company_tel=company_tel,
                                            email=email, password=password1)
            user.save()

            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = common_activation_token.make_token(user)
            message_data = message(domain, uidb64, token)

            mail_title = "이메일 인증을 완료해주세요."
            mail_to = email
            send_email = EmailMessage(mail_title, message_data, to=[mail_to])
            send_email.send()
            return render(request, 'login/signUp_completed.html', res_data)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"}, status=400)
        except TypeError:
            return JsonResponse({"message": "INVALID_TYPE"}, status=400)
        except ValidationError:
            return JsonResponse({"message": "VALIDATION_ERROR"}, status=400)

    # GET 요청 시(회원가입 버튼 클릭 등)
    def get(self, request):
        return render(request, 'login/signup.html')


# 이메일 인증을 담당하는 클래스
class Activate(View):
    def get(self, request, uid64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uid64))
            user = User.objects.get(pk=uid)

            if common_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return JsonResponse({"message": "AUTH FAIL"}, status=400)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"}, status=400)
        except ValidationError:
            return JsonResponse({"message": "VALIDATION_ERROR"}, status=400)


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
