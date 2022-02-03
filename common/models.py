"""
common/models.py
- Custom User Model 구현
"""

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):

    # username_field에 'userid'(사용자 아이디)를 사용할 것임
    def create_user(self, userid, username, company_name,
                    company_address, company_tel, phone_num, email, auth_num=None, password=None):
        if not userid:
            raise ValueError('Users must have an user id')
        if not username:
            raise ValueError('Users must have an user name')
        if not company_name:
            raise ValueError('must have user company name')
        if not company_address:
            raise ValueError('must have user company address')
        if not company_tel:
            raise ValueError('must have user company tel')
        if not phone_num:
            raise ValueError('must have user phone num')
        if not password:
            raise ValueError('must have user password')
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            userid=userid,
            username=username,
            company_name=company_name,
            company_address=company_address,
            company_tel=company_tel,
            phone_num=phone_num,
            email=self.normalize_email(email),
            auth_num=auth_num
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, username, company_name,
                         company_address, company_tel, phone_num, email, password, auth_num=None):
        user = self.create_user(
            userid,
            password=password,
            username=username,
            company_name=company_name,
            company_address=company_address,
            company_tel=company_tel,
            phone_num=phone_num,
            email=self.normalize_email(email),
            auth_num=auth_num
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userid = models.CharField(max_length=50, primary_key=True, null=False, blank=False,
                              unique=True, verbose_name='사용자 아이디')
    username = models.CharField(max_length=50, null=False, blank=False, verbose_name='사용자 이름')
    phone_num = models.CharField(max_length=13, null=False, blank=False, verbose_name='휴대전화')
    company_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='회사명')
    company_address = models.CharField(max_length=100, null=False, blank=False, verbose_name='회사 주소')
    company_tel = models.CharField(max_length=13, null=False, blank=False, verbose_name='회사 전화')
    email = models.EmailField(verbose_name='이메일', max_length=255, unique=True, null=False, blank=False)
    auth_num = models.CharField(verbose_name='인증번호', max_length=8, null=True)
    # 아래 두 개의 필드는 Django의 User Model을 구성할 때 필수로 요구되는 항목
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['username', 'phone_num', 'company_name', 'company_address', 'company_tel', 'email']

    def __str__(self):
        return self.userid

    # True를 반환하여 권한이 있는 것을 알림
    # Object 반환 시 해당 Object로 사용 권한을 확인하는 절차가 필요함
    def has_perm(self, perm, obj=None):
        return True

    # True를 반환하여 주어진 App의 Model에 접근 가능하도록 함
    def has_module_perms(self, app_label):
        return True

    # True 반환 시 Django의 관리자 화면에 로그인 가능
    @property
    def is_staff(self):
        return self.is_admin




