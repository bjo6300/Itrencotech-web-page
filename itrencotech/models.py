from django.db import models

# 카테고리 모델  ----------------------------------------------

class CategoryModel(models.Model):
    category_index = models.AutoField(verbose_name='카테고리 인덱스', primary_key=True)
    category_main = models.CharField(max_length=50, verbose_name='메인 카테고리')
    category_sub = models.CharField(max_length=50, verbose_name='서브 카테고리')

    def __str__(self):
        return self.category_index

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'category'