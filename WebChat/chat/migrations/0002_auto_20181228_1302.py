# Generated by Django 2.1.4 on 2018-12-28 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatinfo',
            name='chat_content',
            field=models.CharField(default='isnull', max_length=400, verbose_name='发送的内容'),
        ),
        migrations.AlterField(
            model_name='chatinfo',
            name='user_id',
            field=models.CharField(default='user id', max_length=50, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='chatinfo',
            name='user_name',
            field=models.CharField(default='no name', max_length=50, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.CharField(default='user id', max_length=50, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(default='no name user', max_length=50, verbose_name='用户名'),
        ),
    ]