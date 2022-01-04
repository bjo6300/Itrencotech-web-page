from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def index(request):
    return render(request, 'home.html')

def body_onlyIdea_onlyIdea(request):
    return render(request, 'body/onlyIdea/onlyIdea_home.html')

def body_prototyping_prototyping_home(request):
    # 시제품 제작 메인
    return render(request, 'body/prototyping/prototyping_home.html')

def body_onlyIdea_onlyIdea_mechanical_design(request): 
    # 기계설계
    return render(request, 'body/onlyIdea/onlyIdea_mechanical_design.html')

def body_onlyIdea_onlyIdea_product_mechanism_design(request):
    # 제품 기구설계
    return render(request, 'body/onlyIdea/onlyIdea_product_mechanism_design.html')

def body_onlyIdea_onlyIdea_production_design(request):
    # 제품 디자인
    return render(request, 'body/onlyIdea/onlyIdea_production_design.html')