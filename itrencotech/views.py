from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 itrencotech에 오신것을 환영합니다.")

def login(request):
    return render(request, 'login/login.html')

def signUp(request):
    return render(request, 'login/signUp.html')

def findIdPasswd(request):
    return render(request, 'login/findIdPasswd.html')

def findId(request):
    return render(request, 'login/findId.html')
