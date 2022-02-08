from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from common.models import User
import datetime

DELETED_USER = "deleted_user"
DELETED_CATEGORY = "deleted_category"


# 카테고리 모델  ----------------------------------------------

class Category(models.Model):
    category_index = models.AutoField(verbose_name='카테고리 인덱스', primary_key=True)
    category_main = models.CharField(max_length=50, verbose_name='메인 카테고리')
    category_sub = models.CharField(max_length=50, verbose_name='서브 카테고리')

    def __str__(self):
        return str(self.category_index)

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'category'


# 포트폴리오 모델  ----------------------------------------------

class Portfolio(models.Model):
    board_index = models.AutoField(verbose_name='게시글 인덱스', primary_key=True)
    category_index = models.ForeignKey(Category, related_name="%(class)s_category_index", on_delete=models.CASCADE,
                                       db_column='category_index', verbose_name='카테고리 인덱스')
    portfolio_img = models.CharField(max_length=100, verbose_name='이미지 주소')
    content = models.CharField(max_length=500, verbose_name='내용')

    def __str__(self):
        return str(self.category_index)

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'portfolio'


# 고객 후기 모델  ----------------------------------------------

class Review(models.Model):
    board_index = models.AutoField(verbose_name='게시글 인덱스', primary_key=True)
    category_index = models.ForeignKey(Category, related_name="%(class)s_category_index", on_delete=models.CASCADE,
                                       db_column='category_index', verbose_name='카테고리 인덱스')
    userid = models.ForeignKey(User, related_name="%(class)s_userid", on_delete=models.SET_DEFAULT,
                               default=DELETED_USER,
                               db_column='userid', verbose_name='작성자 아이디')
    rating = models.FloatField(verbose_name='별점')
    date = models.DateField(default=datetime.date.today, verbose_name='작성일')
    content = models.CharField(max_length=500, verbose_name='내용')
    review_img = models.CharField(max_length=100, verbose_name='이미지 주소')

    def __str__(self):
        return str(self.board_index)

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'review'


# 주문 모델  ----------------------------------------------

class Order(models.Model):
    order_num = models.AutoField(verbose_name='주문 번호', primary_key=True)
    category_index = models.ForeignKey(Category, related_name="%(class)s_category_index", on_delete=models.SET_DEFAULT,
                                       default=DELETED_CATEGORY,
                                       db_column='category_index', verbose_name='카테고리 인덱스')
    userid = models.ForeignKey(User, related_name="%(class)s_userid", on_delete=models.SET_DEFAULT,
                               default=DELETED_USER,
                               db_column='userid', verbose_name='주문자 아이디')
    company_name = models.CharField(max_length=30, verbose_name='회사명')
    business_num = models.CharField(max_length=255, verbose_name='사업자 등록 번호')
    name = models.CharField(max_length=50, verbose_name='담당자')
    email = models.CharField(max_length=100, verbose_name='이메일')
    phone_num = models.CharField(max_length=13, verbose_name='연락처')
    title = models.CharField(max_length=100, verbose_name='제품 제목')
    description = models.CharField(max_length=255, verbose_name='제품 설명')
    material = models.CharField(max_length=100, verbose_name='소재')
    quantity = models.IntegerField(default=1, verbose_name='제품 수량')
    size = models.CharField(max_length=255, verbose_name='크기(가로/세로/높이)')
    path = models.CharField(max_length=255, verbose_name='파일 경로')
    etc = models.CharField(max_length=255, null=True, verbose_name='기타')
    date = models.DateField(default=datetime.date.today, verbose_name='주문일')
    state = models.CharField(max_length=20, default='Got it', verbose_name='주문 상태')

    def __str__(self):
        return str(self.order_num)

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'orders'
