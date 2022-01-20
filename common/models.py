from django.db import models


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

    def __str__(self):
        return self.user_name

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'
