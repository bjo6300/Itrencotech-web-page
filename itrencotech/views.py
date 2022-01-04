from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.http import HttpResponse


def index(request):
    """
    홈페이지 출력
    """
    return render(request, 'body/main.html')


def navbar_about_ceo(request):
    return render(request, 'navBar/about/ceo.html')


def navbar_about_history(request):
    return render(request, 'navBar/about/history.html')


def navbar_about_ideology(request):
    return render(request, 'navBar/about/ideology.html')


def navbar_about_route(request):
    return render(request, 'navBar/about/route.html')


def body_production_home(request):
    return render(request, 'body/production/home.html')


def body_production_mold(request):
    return render(request, 'body/production/mold.html')


def body_production_cnc(request):
    return render(request, 'body/production/cnc.html')


def body_production_press(request):
    return render(request, 'body/production/press.html')

