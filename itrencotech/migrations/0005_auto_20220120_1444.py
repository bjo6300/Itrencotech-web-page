# Generated by Django 3.1.3 on 2022-01-20 05:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('itrencotech', '0004_reviewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliomodel',
            name='category_index',
            field=models.ForeignKey(db_column='category_index', on_delete=django.db.models.deletion.CASCADE, related_name='portfoliomodel_category_index', to='itrencotech.categorymodel', verbose_name='카테고리 인덱스'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='category_index',
            field=models.ForeignKey(db_column='category_index', on_delete=django.db.models.deletion.CASCADE, related_name='reviewmodel_category_index', to='itrencotech.categorymodel', verbose_name='카테고리 인덱스'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='reviewmodel_user_id', to='common.usermodel', verbose_name='작성자 아이디'),
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('order_num', models.AutoField(primary_key=True, serialize=False, verbose_name='주문 번호')),
                ('business_num', models.CharField(max_length=255, verbose_name='사업자 등록 번호')),
                ('name', models.CharField(max_length=50, verbose_name='담당자')),
                ('email', models.CharField(max_length=100, verbose_name='이메일')),
                ('phone_num', models.CharField(max_length=13, verbose_name='연락처')),
                ('title', models.CharField(max_length=100, verbose_name='제품 제목')),
                ('description', models.CharField(max_length=255, verbose_name='제품 설명')),
                ('material', models.CharField(max_length=100, verbose_name='소재')),
                ('quantity', models.IntegerField(default=1, verbose_name='제품 수량')),
                ('size', models.CharField(max_length=255, verbose_name='크기(가로/세로/높이)')),
                ('path', models.CharField(max_length=255, verbose_name='파일 경로')),
                ('etc', models.CharField(max_length=255, null=True, verbose_name='기타')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='주문일')),
                ('state', models.CharField(default='접수 완료', max_length=20, verbose_name='주문 상태')),
                ('category_index', models.ForeignKey(db_column='category_index', on_delete=django.db.models.deletion.CASCADE, related_name='ordermodel_category_index', to='itrencotech.categorymodel', verbose_name='카테고리 인덱스')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='ordermodel_user_id', to='common.usermodel', verbose_name='주문자 아이디')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
