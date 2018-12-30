from django.db import models


class ChatInfo(models.Model):
    # 用户名
    user_name = models.CharField(max_length=50, default="匿名", verbose_name="用户名")
    # 用户发送的内容
    chat_content = models.CharField(max_length=400, default="空", verbose_name="发送的内容")

    class Meta:
        verbose_name = "聊天内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.chat_content


class UserInfo(models.Model):
    # 用户名
    user_name = models.CharField(max_length=50, default="匿名用户", verbose_name="用户名")
    # 用户密码
    user_pwd = models.CharField(max_length=50,verbose_name="用户密码")