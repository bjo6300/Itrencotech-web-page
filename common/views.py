
# 로그인/회원가입 ---------------------------------------
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import User

# 이메일 인증 -------------------------------------------
import ctypes, string, random

from django.views import View
from django.core.mail import EmailMessage


# ------------------------------------------------------

""" ───────────────────────── 로그인/회원가입 ───────────────────────── """

# 로그인 함수
def login_main(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request, userid=userid, password=password)

        if user is None:
            return render(request, 'login/login.html', {'error': 'username or password가 틀렸습니다.'})
        else:
            auth.login(request, user)
            return redirect('/')
    elif request.method == 'GET':
        return render(request, 'login/login.html')


# 회원가입 클래스
class SignUpView(View):
    # POST 요청 시
    def post(self, request):
        username = request.POST.get('username', None)  # 이름
        userid = request.POST.get('userid', None)  # 아이디
        password1 = request.POST.get('password1', None)  # 비밀번호
        phone_num = request.POST.get('phone_num', None)  # 휴대전화
        password2 = request.POST.get('password2', None)  # 비밀번호(확인)
        company_name = request.POST.get('company_name', None)  # 회사명
        company_address = request.POST.get('company_address', None)  # 회사 주소
        company_tel = request.POST.get('company_tel', None)  # 회사 전화
        email = request.POST.get('email', None)  # 이메일
        res_data = {}

        # 빈 칸 확인
        # if not (username and userid and password1 and password2 and phone_num
        #         and company_name and company_address and company_tel and email):
        #     res_data['error'] = "입력하지 않은 칸이 있습니다."

        # 아이디가 5자 미만이면
        # if len(userid) < 5:
            # print('5자 이상의 아이디를 입력해 주세요.')
            # ctypes.windll.user32.MessageBoxW(0, '5자 이상의 아이디를 입력해 주세요.', '이메일 인증 창            ')
            # return render(request, 'login/signup.html')

        # 아이디 중복 확인
        if User.objects.filter(userid=userid).exists():  # 아이디 중복 체크
            messages.warning(request, '이미 존재하는 아이디입니다!')
            return render(request, 'login/signup.html')

        # 비밀번호 일치 여부 확인
        # if password1 != password2:
        #     res_data['error'] = '비밀번호가 일치하지 않습니다.'

        # DB에 사용자 계정 생성
        user = User.objects.create_user(userid=userid, username=username,
                                        phone_num=phone_num, company_name=company_name,
                                        company_address=company_address, company_tel=company_tel,
                                        email=email, password=password1)
        user.save()
        return render(request, 'login/signup_completed.html', res_data)

    # GET 요청 시(회원가입 버튼 클릭 등)
    def get(self, request):
        return render(request, 'login/signup.html')


# ---------------------------------------------------------------------------------------------------------------------


def signUpCompleted(request):
    """ 회원가입 완료 페이지 """
    return render(request, 'login/signup_completed.html')


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
    if request.method == 'POST':
        userid = request.POST['input-id']
        # 만약 입력 란이 비워져 있다면
        if userid == '':
            # print('아이디를 입력해 주세요.')
            # ctypes.windll.user32.MessageBoxW(0, '아이디를 입력해 주세요', '아이디 입력 오류            ')
            return render(request, 'login/find_passwd.html')
        # 아이디가 DB 안에 있다면
        if User.objects.filter(userid=userid).exists():
            user = User.objects.get(userid=userid)

            # 전처리 (수정 필요)
            email = '***' + user.email[3:]
            phone_num = user.phone_num[:5] + '***' + user.phone_num[8:10] + '***'
            return render(request, 'login/find_passwd_id_list.html', {'email': email, 'phone_num': phone_num,
                                                                      'userid': user.userid})
        # 아이디가 DB 안에 없다면
        else:
            print('존재하지 않는 아이디입니다.')
            # ctypes.windll.user32.MessageBoxW(0, '존재하지 않는 아이디입니다.', '아이디 입력 오류            ')
            return render(request, 'login/find_passwd.html', {'id-check': 'false'})
    elif request.method == 'GET':
        return render(request, 'login/find_passwd.html')


def findPasswdIdList(request):
    """ 비밀번호 찾기 - 아이디 목록 페이지 """
    if request.method == 'POST':
        userid = request.POST['userid']
        user = User.objects.get(userid=userid)

        # 인증 번호 생성 후 메일 전송
        auth_num = email_auth_num()
        EmailMessage(subject='이메일 인증 코드입니다.',
                     body=f'다음의 코드를 입력하세요\n{auth_num}',
                     to=[user.email]).send()
        # 인증 번호를 DB에 저장
        user.auth_num = auth_num
        user.save()
        return render(request, 'login/find_passwd_email.html', {'userid': userid})

    elif request.method == 'GET':
        return render(request, 'login/find_passwd_email.html')


def findPasswdPhone(request):
    """ 비밀번호 찾기 - 휴대폰 번호로 찾기 """
    return render(request, 'login/find_passwd_phone.html')


def findPasswdEmail(request):
    """ 비밀번호 찾기 - 이메일로 찾기 """
    if request.method == 'POST':
        userid = request.POST['userid']
        auth_num = request.POST['auth_num']

        # 해당 아이디를 가진 유저가 DB에 있으면 -> 인증 번호 비교
        if User.objects.filter(userid=userid).exists():
            user = User.objects.get(userid=userid)
            # 인증 번호가 같으면 DB에 저장된 인증 번호를 NULL로 변경
            if auth_num == user.auth_num:
                user.auth_num = None
                user.save()
                return render(request, 'login/find_passwd_reset.html', {'userid': userid})

            # 인증 번호가 다르면 알림창 띄움
            else:
                print('인증번호가 틀렸습니다.')
                # ctypes.windll.user32.MessageBoxW(0, '인증번호가 틀렸습니다.', '이메일 인증 창            ')
                return render(request, 'login/find_passwd_email.html')

        # 해당 아이디를 가진 유저가 DB에 없으면
        else:
            print('잘못된 접근입니다.')
            # ctypes.windll.user32.MessageBoxW(0, '잘못된 접근입니다.', '이메일 인증 창            ')
            return redirect('/common/find_id_passwd')

    elif request.method == 'GET':
        return render(request, 'login/find_passwd_email.html')


def findPasswdReset(request):
    """ 비밀번호 찾기 - 비밀번호 재설정 """
    if request.method == 'POST':
        userid = request.POST['userid']
        password = request.POST['password']

        # 만약 userid가 DB에 있으면
        if User.objects.filter(userid=userid).exists():
            user = User.objects.get(userid=userid)
            # 사용자의 password를 변경하는 작업 수행
            user.set_password(raw_password=password)
            user.save()
            return render(request, 'login/find_passwd_completed.html')
        # 그렇지 않고 userid가 DB에 없으면
        else:
            print('잘못된 접근입니다.')
            # ctypes.windll.user32.MessageBoxW(0, '잘못된 접근입니다.', '비밀번호 재설정 창            ')
            return redirect('/common/find_id_passwd')

    elif request.method == 'GET':
        return render(request, 'login/find_passwd_reset.html')


def findPasswdCompleted(request):
    """ 비밀번호 찾기 - 비밀번호 재설정 완료 """
    return render(request, 'login/find_passwd_completed.html')


def verification(request):
    """ 이메일 인증 """
    if request.method == 'POST':
        email1 = request.POST['email1']
        email2 = request.POST['email2']
        input_email = email1+'@'+email2

        # 해당 이메일을 가진 유저가 DB에 있으면
        if User.objects.filter(email=input_email).exists():
            users = User.objects.filter(email=input_email)
            auth_num = email_auth_num()  # 함수를 통해 인증번호 생성

            # 이메일로 인증번호 전송
            EmailMessage(subject='이메일 인증 코드입니다.',
                         body=f'다음의 코드를 입력하세요\n{auth_num}',
                         to=[input_email]).send()

            # 해당 이메일을 가진 계정에 인증번호를 모두 저장(DB)
            for user in users:
                user.auth_num = auth_num
                user.save()
        # 해당 이메일을 가진 유저가 DB에 없으면
        else:
            # 알림창을 띄움
            print('이메일 없음')
            # ctypes.windll.user32.MessageBoxW(0, '이메일 없음', '이메일 인증 창            ')

        return render(request, 'login/find_id_email.html', {'email1': email1, 'email2': email2})
    elif request.method == 'GET':
        return render(request, 'login/find_id_email.html')


def verification2(request):
    if request.method == 'POST':
        email1 = request.POST.get('email1', None)
        email2 = request.POST.get('email2', None)
        auth_num = request.POST.get('auth_num', None)
        input_email = email1 + '@' + email2

        # 해당 이메일을 가진 유저가 DB에 있으면
        if User.objects.filter(email=input_email).exists():
            users = User.objects.filter(email=input_email)

            # 유저가 입력한 인증번호와 DB에 저장된 인증번호 비교
            # 인증번호가 일치하면
            if users[0].auth_num == auth_num:
                # 해당 이메일을 가진 계정에 저장된 인증번호를 모두 NULL로 변경
                for user in users:
                    user.auth_num = None
                    user.save()
                return render(request, 'login/find_id_list.html', {'users': users, 'by': "이메일"})

            # 인증번호가 일치하지 않으면 알림창 띄움
            else:
                print('인증번호가 틀렸습니다.')
                # ctypes.windll.user32.MessageBoxW(0, '인증번호가 틀렸습니다.', '이메일 인증 창            ')
                return render(request, 'login/find_id_email.html', {'email1': email1, 'email2': email2})

        # 해당 이메일을 가진 유저가 DB에 없으면
        else:
            print('이메일을 다시 확인해 주세요.')
            # ctypes.windll.user32.MessageBoxW(0, '이메일을 다시 확인해주세요.', '이메일 인증 창            ')
            return render(request, 'login/find_id_email.html')
    elif request.method == 'GET':
        return render(request, 'login/find_id_email.html')


# 8자리의 랜덤한 인증번호를 생성하는 함수(알파벳 대문자,소문자,숫자 혼합)
def email_auth_num():
    LENGTH = 8
    string_pool = string.ascii_letters + string.digits
    auth_num = ""
    for i in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num
