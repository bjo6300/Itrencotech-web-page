from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth

from common.forms import UserForm
from django.urls import reverse

""" ───────────────────────── 로그인/회원가입 ───────────────────────── """
# 일반 로그인
def login_main(request):
    """ 로그인 페이지 """
    if request.method == 'POST':
        username = request.POST.get('username', None)  # 이름
        password = request.POST.get('password1', None)  # 비밀번호
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
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # userid = form.cleaned_data.get('userid')
            # password1 = form.cleaned_data.get('password1')
            # user = authenticate(username=userid, password=password1)
            # 사용자 인증
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # 로그인
            logout(request)
            return redirect('/common/signUp/completed')
            # url = reverse('location:get_location')
            # print("location_url ", url)
            # return HttpResponseRedirect(url)
    else:
        form = UserForm()
    return render(request, 'login/signUp.html', {'form': form})


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
