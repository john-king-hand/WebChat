# Generated by Django 2.0.2 on 2018-12-28 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_chatinfo_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatInfo',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
