from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 itrencotech에 오신것을 환영합니다.")


def portfolio(request):
    """ 포트폴리오 페이지 """
    return render(request, 'navBar/portfolio/portfolio.html')


def review(request):
    """ 후기 페이지 """
    return render(request, 'navBar/review/review.html')