from django.shortcuts import render, HttpResponse, redirect
from chat import models
from django.http import JsonResponse
import json
from django.core import serializers
from django.db.models import Max


# Create your views here.


def chong(request):
    """
    重定向
    :param request:
    :return:
    """
    return redirect('/login.html/')


def sign(request):
    """
    注册
    :param request:
    :return:
    """
    # 判断是否为 POST 请求
    if request.method == 'POST':
        name = request.POST.get('signname')  # 获取注册用户名
        pwd = request.POST.get('signpwd')  # 获取注册密码
        c = models.UserInfo.objects.filter(user_name=name)  # 拿注册用户去数据库比对，看是否已经被注册
        if c:
            # 如果被注册，返回注册界面并提示已被注册
            return render(request, 'sign.html', {'text': '该用户已被注册！'})
        else:
            # 如果没被注册，向数据库添加新用户 （用户名，密码，注册时间）
            models.UserInfo.objects.create(user_name=name, user_pwd=pwd)
            # 重定向登录界面
            return redirect('/login.html/')
    # 如果不是 POST 请求，返回 注册界面
    return render(request, 'sign.html')


def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 如果为 POST 请求
        name = request.POST.get('uname')  # 获取登录用户名
        pwd = request.POST.get('upwd')  # 获取登录密码
        c = models.UserInfo.objects.filter(user_name=name, user_pwd=pwd)  # 去数据库比对用户名和密码
        if c:
            # 添加username进session存入数据库
            request.session['username'] = name
            # 返回主页
            return redirect('/index.html/')
        else:
            # 如果用户名和密码不匹配，则返回登录页面并提示
            return render(request, 'login.html', {'text': '用户名或密码错误！'})
    # 如果不是POST请求，返回登录界面
    return render(request, 'login.html')


def index(request):
    """
        主页
    :param request:
    :return:
    """
    name = request.session.get('username')
    if name:
        return render(request, 'index.html',{"username": name})
    else:
        # 否则返回登录界面
        return redirect('/login.html')


def send_and_save(request):
    """
    发送消息并存库
    :param request:
    :return:
    """
    name = request.session.get('username')
    if name:
        content = request.GET.get("my_text")
        models.ChatInfo.objects.create(user_name=name, chat_content=content)
        return JsonResponse({"ret": 1})
    else:
        # 否则返回登录界面
        return redirect('/login.html')


def get_text(request):
    """
    获取消息
    :param request:
    :return:
    """
    name = request.session.get('username')
    if name:
        all_info = models.ChatInfo.objects.all()
        id_max = models.ChatInfo.objects.aggregate(Max('id'))['id__max']
        # 获取请求的id值
        old_info = request.GET.get("old_info")

        # 第一次请求数据
        if int(old_info) == 0:
            result_dic = dict()
            result_dic["old_info"] = id_max
            result_dic["info"] = [{"user_name": "系统消息", "chat_content": "欢迎来到WebChat聊天室。"}]
            result_dic["user_name"] = '系统消息'
            result_dic = json.dumps(result_dic, ensure_ascii=False)
            return JsonResponse({"dataa": result_dic})

        # 没有新的消息
        elif int(old_info) >= id_max:
            result_dic = dict()
            result_dic["old_info"] = id_max
            result_dic["info"] = [{id_max: "欢迎再次来到聊天室!"}]
            result_dic["user_name"] = ''
            result_dic = json.dumps(result_dic, ensure_ascii=False)
            return JsonResponse({"dataa": result_dic})

        # 如果有新消息更新
        else:
            result_dic = dict()
            new_info = models.ChatInfo.objects.filter(id__gt=old_info)
            print(len(new_info))
            msg_list = list()
            for info in new_info:
                msg_dic = dict()
                msg_dic["id"] = info.id
                msg_dic["user_name"] = info.user_name
                msg_dic["chat_content"] = info.chat_content
                msg_list.append(msg_dic)
            result_dic["old_info"] = id_max
            result_dic["info"] = msg_list
            result_dic = json.dumps(result_dic, ensure_ascii=False)
            print(result_dic)
            return JsonResponse({"dataa": result_dic})

        return JsonResponse({"ret": 1})
    else:
        # 否则返回登录界面
        return redirect('/login.html')
