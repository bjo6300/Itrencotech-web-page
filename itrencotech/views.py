from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import json


def index(request):
    return render(request, 'body/main.html')

# 
# def login(request):
#     """ 로그인 페이지 """
#     return render(request, 'login/login.html')
# 
# 
# def signUp(request):
#     """ 회원가입 페이지 """
#     return render(request, 'login/signUp.html')
# 
# 
# def signUpCompleted(request):
#     """ 회원가입 완료 페이지 """
#     return render(request, 'login/signUp_completed.html')
# 
# 
# def findIdPasswd(request):
#     """ 아이디 / 비밀번호 찾기 페이지 """
#     return render(request, 'login/find_id_passwd.html')
# 
# 
# """ ───────────────────────── 아이디 찾기 ───────────────────────── """
# def findId(request):
#     """ 아이디 찾기 페이지 """
#     return render(request, 'login/find_id.html')
# 
# def findIdPhone(request):
#     """ 아이디 찾기 - 휴대폰 번호로 찾기 """
#     return render(request, 'login/find_id_phone.html')
# 
# 
# def findIdEmail(request):
#     """ 아이디 찾기 - 이메일로 찾기 """
#     return render(request, 'login/find_id_email.html')
# 
# 
# def findIdListbyPhone(request):
#     """ 아이디 찾기 - 전화번호로 찾은 아이디 목록 """
#     context = {'by': "전화번호"}
#     return render(request, 'login/find_id_list.html', context)
# 
# def findIdListbyEmail(request):
#     """ 아이디 찾기 - 이메일로 찾은 아이디 목록 """
#     context = {'by': "이메일"}
#     return render(request, 'login/find_id_list.html', context)
# 
# 
# """ ───────────────────────── 비밀번호 찾기 ───────────────────────── """
# def findPasswd(request):
#     """ 비밀번호 찾기 페이지 """
#     return render(request, 'login/find_passwd.html')
# 
# 
# def findPasswdIdList(request):
#     """ 비밀번호 찾기 - 아이디 목록 페이지 """
#     return render(request, 'login/find_passwd_id_list.html')
# 
# 
# def findPasswdPhone(request):
#     """ 비밀번호 찾기 - 휴대폰 번호로 찾기 """
#     return render(request, 'login/find_passwd_phone.html')
# 
# 
# def findPasswdEmail(request):
#     """ 비밀번호 찾기 - 이메일로 찾기 """
#     return render(request, 'login/find_passwd_email.html')
# 
# 
# def findPasswdReset(request):
#     """ 비밀번호 찾기 - 비밀번호 재설정 """
#     return render(request, 'login/find_passwd_reset.html')
# 
# 
# def findPasswdCompleted(request):
#     """ 비밀번호 찾기 - 비밀번호 재설정 완료 """
#     return render(request, 'login/find_passwd_completed.html')





def portfolio(request):
    """ 포트폴리오 페이지 """
    return render(request, 'navBar/portfolio/portfolio.html')


def portfolioDesign(request):
    """ 포트폴리오 - 제품 디자인 페이지 """
    return render(request, 'navBar/portfolio/design.html')


def portfolioMachineDesign(request):
    """ 포트폴리오 - 기계시스템 설계 페이지 """
    return render(request, 'navBar/portfolio/machine_design.html')


def portfolioHWmachine(request):
    """ 포트폴리오 - H/W 기구설계 페이지 """
    return render(request, 'navBar/portfolio/HW_machine.html')


def portfolio3d(request):
    """ 포트폴리오 - 3D 프린팅 페이지 """
    return render(request, 'navBar/portfolio/3d.html')


def portfolioMockup(request):
    """ 포트폴리오 - 목업 CNC 가공 페이지 """
    return render(request, 'navBar/portfolio/mockup.html')


def portfolioCnc(request):
    """ 포트폴리오 - 부품 CNC 가공 페이지 """
    return render(request, 'navBar/portfolio/cnc.html')


def portfolioSdm(request):
    """ 포트폴리오 - Smart Digital Mold 페이지 """
    return render(request, 'navBar/portfolio/sdm.html')


def portfolioMold(request):
    """ 포트폴리오 - 금형 제작 페이지 """
    return render(request, 'navBar/portfolio/mold.html')


def portfolioInjectionMolding(request):
    """ 포트폴리오 - 사출 성형 페이지 """
    return render(request, 'navBar/portfolio/injection_molding.html')


def portfolioEquipmentDesign(request):
    """ 포트폴리오 - 판금 절곡 페이지 """
    return render(request, 'navBar/portfolio/equipment_design.html')

def reviewBest(request):
    """ 후기 - 베스트후기 페이지 """
    return render(request, 'navBar/review/review_best.html')


def reviewRecent(request):
    """ 후기 - 최신순 페이지 """
    return render(request, 'navBar/review/review_recent.html')


def reviewHighRating(request):
    """ 후기 - 높은평점순 페이지 """
    return render(request, 'navBar/review/review_high_rating.html')


def reviewLowRating(request):
    """ 후기 - 낮은평점순 페이지 """
    return render(request, 'navBar/review/review_low_rating.html')





def body_onlyIdea_onlyIdea(request):
    # onlyIdea 메인
    return render(request, 'body/onlyIdea/onlyIdea_home.html')

def onlyIdea_detail(request):
    # onlyIdea 상세설명
    return render(request, 'body/onlyIdea/onlyIdea_detail.html')


def body_prototyping_prototyping_home(request):
    # 시제품 제작 메인
    return render(request, 'body/prototyping/prototyping_home.html')

def prototyping_detail(request):
    # 시제품 상세설명
    return render(request, 'body/prototyping/prototyping_detail.html')




def navbar_about_ceo(request):
    return render(request, 'navBar/about/ceo.html')


def navbar_about_history(request):
    return render(request, 'navBar/about/history.html')


def navbar_about_ideology(request):
    return render(request, 'navBar/about/ideology.html')


def navbar_about_route(request):
    return render(request, 'navBar/about/route.html')

def navbar_about_test(request):
    return render(request, 'navBar/about/test.html')





def body_production_home(request):
    # 양산 홈
    return render(request, 'body/production/production_home.html')


def production_detail(request):
    # 양산 상세설명
    return render(request, 'body/production/production_detail.html')

# ##### 주문 페이지 #####
def order_home(request):
    return render(request, 'order/order_home.html')


def order_confirmation(request):
    return render(request, 'order/order_confirmation.html')


def order_form_onlyIdea(request):
    if request.method == "GET":
        method = request.GET.get('method', False)
        context = {'method': method}
        contextDict = json.dumps(context)
        return render(request, 'order/order_form_onlyIdea.html', {'contextDict': contextDict})

    return render(request, 'order/order_form_onlyIdea.html')


def order_form_prototyping(request):
    if request.method == "GET":
        method = request.GET.get('method', False)
        context = {'method': method}
        contextDict = json.dumps(context)
        return render(request, 'order/order_form_prototyping.html', {'contextDict': contextDict})

    return render(request, 'order/order_form_prototyping.html')


def order_form_production(request):
    if request.method == "GET":
        method = request.GET.get('method', False)
        context = {'method': method}
        contextDict = json.dumps(context)
        return render(request, 'order/order_form_production.html', {'contextDict': contextDict})

    return render(request, 'order/order_form_production.html')

# ##### 마이페이지 #####
def mypage_home(request):
    return render(request, 'navbar/myPage/myPage_home.html')

def mypage_order_history(request):
    return render(request, 'navBar/myPage/myPage_order_history.html')

def myPage_update_info(request):
    return render(request, 'navBar/myPage/myPage_update_info.html')

def mypage_info(request):
    return render(request, 'navBar/myPage/myPage_info.html')