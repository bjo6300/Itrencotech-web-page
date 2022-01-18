from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.CharField(max_length=32, unique=True, primary_key=True, verbose_name="아이디")  # username(userid)와 name을 헷갈리지 말 것
    name = models.CharField(max_length=32, verbose_name="이름")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    phone_num = models.CharField(max_length=32, unique=True, verbose_name="휴대전화")
    company_name = models.CharField(max_length=32, verbose_name="회사명")
    company_address = models.CharField(max_length=64, verbose_name="회사 주소")
    company_tel = models.CharField(max_length=128, verbose_name="회사 전화")
    email = models.EmailField(max_length=128, unique=True, verbose_name="이메일")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')

    class Meta:
        db_table = "user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"

    def __str__(self):
        return self.name
