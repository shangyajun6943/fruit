# Generated by Django 2.0.1 on 2018-02-01 09:51

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=40, unique=True)),
                ('volume', models.IntegerField()),
                ('shop_introduction', models.TextField(max_length=255)),
                ('shop_address', models.TextField(max_length=255)),
                ('create_data', models.DateTimeField()),
                ('isdelete', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'shop_user',
            },
            managers=[
                ('shops', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('passwd', models.CharField(max_length=40)),
                ('gender', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0)),
                ('user_address', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=11)),
                ('shop_id', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('head_picture', models.URLField()),
                ('isdelete', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
    ]
