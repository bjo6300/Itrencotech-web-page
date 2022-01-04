from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 itrencotech에 오신것을 환영합니다.")


def portfolio(request):
    """ 포트폴리오 페이지 """
    return render(request, 'navBar/portfolio/portfolio.html')


def portfolio3d(request):
    """ 포트폴리오 - 3D 프린팅 페이지 """
    return render(request, 'navBar/portfolio/3d.html')


def portfolioCnc(request):
    """ 포트폴리오 - CNC 페이지 """
    return render(request, 'navBar/portfolio/cnc.html')


def portfolioMockup(request):
    """ 포트폴리오 - 목업 페이지 """
    return render(request, 'navBar/portfolio/mockup.html')


def portfolioMold(request):
    """ 포트폴리오 - 사출 금형 페이지 """
    return render(request, 'navBar/portfolio/mold.html')


def review(request):
    """ 후기 페이지 """
    return render(request, 'navBar/review/review.html')