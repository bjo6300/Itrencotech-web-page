import json
import traceback

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# from common.forms import UserForm
from common.models import UserModel

""" ───────────────────────── 로그인/회원가입 ───────────────────────── """


# 일반 로그인
# def login_main(request):
#     """ 로그인 페이지 """
#     if request.method == 'POST':
#         username = request.POST.get('username', None)  # 아이디
#         password = request.POST.get('password1', None)  # 비밀번호
#         user = authenticate(request, username=username, password=password)
#         if user is None:
#             return render(request, 'login/login.html', {'error': 'username 또는 password가 틀렸습니다.'})
#         else:
#             auth.login(request, user)
#             return redirect('/')
#     else:
#         return render(request, 'login/login.html')


# def login2_main(request):
#     template_name = 'login/login.html'
#     request.session['loginOK'] = False
#     try:
#         data = request.POST
#         input_id = data['user_id']
#         input_password = data['password1']
#     except (KeyError, input_id == '', input_password == ''):
#         context = {
#             'uid': 'empty',
#             'upass': 'empty',
#         }
#         return render(request, template_name, context)
#     else:
#         if UserModel.objects.filter(user_id=input_id).exists():
#             get_user = UserModel.objects.get(user_id=input_id)
#             if get_user.password1 == input_password:
#                 request.session['loginOK'] = True
#                 context = {
#                     'result': '로그인 성공'
#                 }
#             else:
#                 request.session['loginOK'] = False
#                 context = {
#                     'result': '비밀번호가 틀렸습니다.'
#                 }
#         else:
#             request.session['loginOK'] = False
#             context = {
#                 'result': '존재하지 않는 id입니다.'
#         }
#     return HttpResponse(json.dumps(context), content_type='application/json')


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


# 0119 로그인/회원가입 추가 함수 --------------------------------------------------------------------------------------



# 회원가입 진행 시 auth_user가 아닌 user 테이블에 정보가 저장되므로 유의할 것
# ※※※※※ 현재 회원가입 버튼을 누르면 signUp2() 함수에서 구현되도록 임시 조치 중임 ※※※※※
def signUp2(request):
    # GET 방식 호출일 때
    if request.method == 'GET':
        return render(request, 'login/signup.html')
    # POSS 방식 호출일 때
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', None)  # 이름
        user_id = request.POST.get('user_id', None)  # 아이디
        password1 = request.POST.get('password1', None)  # 비밀번호
        phone_num = request.POST.get('phone_num', None)  # 휴대전화
        password2 = request.POST.get('password2', None)  # 비밀번호(확인)
        company_name = request.POST.get('company_name', None)  # 회사명
        company_address = request.POST.get('company_address', None)  # 회사 주소
        company_tel = request.POST.get('company_tel', None)  # 회사 전화
        email = request.POST.get('email', None)  # 이메일
        res_data = {}
        if not (user_name and user_id and password1 and phone_num and password2
                and company_name and company_address and company_tel and email):
            res_data['error'] = "입력하지 않은 칸이 있습니다."
        if password1 != password2:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            user = UserModel(user_name=user_name, user_id=user_id,
                             # password1=make_password(password1), password2=make_password(password2),
                             password1=password1, password2=password2,  # 암호화 적용 함수를 만든 뒤에는 위의 문장으로 대체
                             phone_num=phone_num, company_name=company_name,
                             company_address=company_address, company_tel=company_tel, email=email)
            user.save()
        return render(request, 'login/signUp_completed.html', res_data)


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
