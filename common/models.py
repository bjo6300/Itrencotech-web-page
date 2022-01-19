import hashlib

from django.db import models
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, user_id, password, **kwargs):
        # 유저를 생성하는 함수
        if not user_id:
            raise ValueError('user_id is required.')
        if not password:
            raise ValueError('password is required.')
        user = UserModel(user_id=user_id)
        user.set_password(password)
        user.save()


class UserModel(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='사용자 이름')
    user_id = models.CharField(max_length=50, primary_key=True, verbose_name='사용자 아이디')
    password1 = models.BinaryField(max_length=200, blank=True, null=True, verbose_name='사용자 비밀번호')
    phone_num = models.CharField(max_length=13, verbose_name='휴대전화')
    password2 = models.BinaryField(max_length=200, blank=True, null=True, verbose_name='사용자 비밀번호(확인)')
    company_name = models.CharField(max_length=30, verbose_name='회사명')
    company_address = models.CharField(max_length=100, verbose_name='회사 주소')
    company_tel = models.CharField(max_length=13, verbose_name='회사 전화')
    email = models.EmailField(max_length=100, unique=True, verbose_name='이메일')

    objects = MyUserManager()

    def set_password(self, password):
        self.password = hashlib.sha256(password).hexdigest()

    @property
    def is_authenticated(self):
        # 이 함수는 기본 User model에서 사용하는 것으로, Anonymous가 아니면 로그인 된 것이므로 항상 True를 리턴
        return True

    @property
    def is_anonymous(self):
        # 위와 같은 이유로 False 리턴
        return False

    def __str__(self):
        return self.user_name

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'


class UserModelAuth(object):
    # 이 클래스를 정의하여 settings 에 auth backend로 등록하면
    # authenticate함수를 아래 처럼 커스터마이징 하여 사용할 수 있다.
    def authenticate(self, **kwargs):
        from django.contrib.auth import get_user_model
        user_id = kwargs.get('user_id')
        password = kwargs.get('password')
        try:
            user = get_user_model().objects.get(user_id=user_id)
        except:
            # 유저가 존재하지 않음
            return None
        if user.status == 'LOCKED':
            # 유저 상태가 잠금인 경우
            raise Exception('USER IS LOCKED')

        if str(user.password) == hashlib.sha256(password).hexdigest():
            # 패스워드 일치 => 로그인 성공
            user.login_fail_count = 0  # 패스워드 실패 횟수를 0으로 초기화
            user.save(update_fields=['login_fail_count'])
            return user
        else:
            # 패스워드 불일치 => 로그인 실패
            user.login_fail_count += 1
            user.save(update_fields=['login_fail_count'])
            return None