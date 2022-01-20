import hashlib

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# 회원가입 정보 저장
class UserModel(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='사용자 이름')
    user_id = models.CharField(max_length=50, primary_key=True, verbose_name='사용자 아이디')
    password1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='사용자 비밀번호')
    phone_num = models.CharField(max_length=13, verbose_name='휴대전화')
    password2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='사용자 비밀번호(확인)')
    company_name = models.CharField(max_length=30, verbose_name='회사명')
    company_address = models.CharField(max_length=100, verbose_name='회사 주소')
    company_tel = models.CharField(max_length=13, verbose_name='회사 전화')
    email = models.EmailField(max_length=100, unique=True, verbose_name='이메일')

    def __str__(self):
        return self.user_name

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'


# 커스텀 유저 모델(로그인) ----------------------------------------------

# 헬퍼(Helper) 클래스
class UserManager(BaseUserManager):
    # 일반 유저 계정 생성
    # create_user()의 첫 번째 인자는 username(즉 user_id), 나머지 부분은 데이터를 생성하는 부분
    def create_user(self, user_id, user_name, phone_num, company_name,
                    company_address, company_tel, email, password=None):
        if not user_id:
            raise ValueError('ID는 필수 항목!!')

        user = self.model(
            user_id=user_id,
            user_name=user_name,
            phone_num=phone_num,
            company_name=company_name,
            company_address=company_address,
            company_tel=company_tel,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 계정 생성
    def create_superuser(self, user_id, password, user_name, phone_num,
                         company_name, company_address, company_tel, email):
        user = self.create_user(
            user_id,
            password=password,
            user_name=user_name,
            phone_num=phone_num,
            company_name=company_name,
            company_address=company_address,
            company_tel=company_tel,
            email=self.normalize_email(email)
        )
        # 관리자 권한 True로 설정
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='사용자 아이디')
    user_name = models.CharField(max_length=50, verbose_name='사용자 이름')
    phone_num = models.CharField(max_length=13, verbose_name='휴대전화')
    company_name = models.CharField(max_length=30, verbose_name='회사명')
    company_address = models.CharField(max_length=100, verbose_name='회사 주소')
    company_tel = models.CharField(max_length=13, verbose_name='회사 전화')
    email = models.EmailField(max_length=255, unique=True, verbose_name='이메일')
    # 아래 두 필드는 django의 User Model의 필수 필드임
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # User Model 생성 시 꼭 필요한 부분
    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name', 'phone_num', 'company_name', 'company_address',
                       'company_tel', 'email']

    def __str__(self):
        return self.user_id

    def set_password(self, password):
        self.password = hashlib.sha256(password).hexdigest()

    # Custom User Model을 기본 User Model로 사용하기 위해 구현해야 하는 부분
    # True를 반환하여 권한이 있음을 알림. Object 반환 시 해당 Object로 사용 권한을 확인하는 절차가 필요함
    def has_perm(self, perm, obj=None):
        return True

    # True를 반환하여 주어진 App의 Model에 접근 가능하도록 함
    def has_module_perms(self, app_label):
        return True

    # True 반환 시 django의 관리자 화면에 로그인 할 수 있음
    @property
    def is_staff(self):
        return self.is_admin

    # def is_valid(self):
    #     pass


# 카테고리 모델  ----------------------------------------------

class CategoryModel(models.Model):
    category_index = models.AutoField(verbose_name='카테고리 인덱스', primary_key=True)
    category_main = models.CharField(max_length=50, verbose_name='메인 카테고리')
    category_sub = models.CharField(max_length=50, verbose_name='서브 카테고리')

    def __str__(self):
        return self.category_index

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'category'
