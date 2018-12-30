# Generated by Django 2.1.4 on 2018-12-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20181228_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatinfo',
            options={},
        ),
        migrations.AlterField(
            model_name='chatinfo',
            name='chat_content',
            field=models.CharField(default='空', max_length=400, verbose_name='发送的内容'),
        ),
        migrations.AlterField(
            model_name='chatinfo',
            name='user_id',
            field=models.CharField(default='用户id', max_length=50, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='chatinfo',
            name='user_ip',
            field=models.CharField(default='127.0.0.1', max_length=30, verbose_name='用户IP'),
        ),
        migrations.AlterField(
            model_name='chatinfo',
            name='user_name',
            field=models.CharField(default='匿名', max_length=50, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.CharField(default='用户id', max_length=50, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_ip',
            field=models.CharField(default='1.1.1.1', max_length=30, verbose_name='用户IP'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(default='匿名用户', max_length=50, verbose_name='用户名'),
        ),
    ]
