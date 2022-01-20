from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itrencotech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('board_index', models.AutoField(primary_key=True, serialize=False, verbose_name='게시글 인덱스')),
                ('portfolio_img', models.CharField(max_length=100, verbose_name='이미지 주소')),
                ('content', models.CharField(max_length=500, verbose_name='내용')),
                ('category_index', models.ForeignKey(db_column='카테고리 인덱스', on_delete=django.db.models.deletion.CASCADE, related_name='portfoliomodel_ccategory_index', to='itrencotech.categorymodel', verbose_name='카테고리 인덱스')),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
    ]
