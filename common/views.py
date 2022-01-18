from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import auth

from common.models import Users

""" ───────────────────────── 로그인/회원가입 ───────────────────────── """
# 일반 로그인
def login(request):
    """ 로그인 페이지 """
    if request.method == 'POST':
        username = request.POST.get('id', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'login/login.html', {'error': 'username 또는 password가 틀렸습니다.'})
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'login/login.html')


def signUp(request):
    """ 회원가입 페이지 """
    if request.method == 'GET':
        return render(request, 'login/signUp.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', '')  # 이름
        user_id = request.POST.get('user_id', '')  # 아이디
        user_pw = request.POST.get('password', '')  # 비밀번호
        # user_pw_confirm = request.POST.get('password-confirm', '')    # 비밀번호 확인(지금은 없으므로 주석 처리)
        phone_num = request.POST.get('user_tel', '')  # 휴대전화
        company_name = request.POST.get('company_name', '')  # 회사명
        company_address = request.POST.get('company_address', '')  # 회사 주소
        company_tel = request.POST.get('company_tel', '')  # 회사 전화
        email = request.POST.get('email', '')  # 이메일

        # 필수 항목 입력 누락 시
        if (user_name or user_id or user_pw or phone_num
                or company_name or company_address or company_tel or email) == '':
            return redirect("/common/signUp/")
        # elif user_pw != user_pw_confirm:
        #     return redirect("{% url 'common:signUp' %}")
        else:
            user = Users(
                id=user_id,
                name=user_name,
                password=user_pw,
                phone_num=phone_num,
                company_name=company_name,
                company_address=company_address,
                company_tel=company_tel,
                email=email
            )
            user.save()

        return redirect("/common/signUp_completed/")


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
