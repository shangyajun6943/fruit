# Generated by Django 2.0.1 on 2018-02-01 09:51

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsname', models.CharField(max_length=40, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('goods_status', models.IntegerField(default=1)),
                ('goods_type', models.IntegerField()),
                ('goods_introduce', models.CharField(max_length=255)),
                ('goods_volume', models.IntegerField()),
                ('goods_num', models.IntegerField()),
                ('img1', models.URLField()),
                ('img2', models.URLField()),
                ('shopping_state', models.IntegerField(default=0)),
                ('isDelete', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'goods',
            },
            managers=[
                ('goods', django.db.models.manager.Manager()),
            ],
        ),
    ]
