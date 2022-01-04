from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


def index(request):
    return render(request, 'body/main.html')


def login(request):
    return render(request, 'login/login.html')

def signUp(request):
    return render(request, 'login/signUp.html')

def findIdPasswd(request):
    return render(request, 'login/findIdPasswd.html')

def findId(request):
    return render(request, 'login/findId.html')

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


def body_prototyping_3Dprinting(request):
    # 3D 프린팅
    return render(request, 'body/prototyping/3DPrinting.html')


def body_prototyping_mockUp(request):
    # 목업
    return render(request, 'body/prototyping/mockUp.html')


def body_prototyping_CNC(request):
    # CNC 가공
    return render(request, 'body/prototyping/CNC.html')


def body_prototyping_sheeting_bending(request):
    # 판금 절곡
    return render(request, 'body/prototyping/sheeting_bending.html')


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

