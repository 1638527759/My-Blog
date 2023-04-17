from audioop import reverse
import email
from pickletools import read_uint1
import re
# from tkinter.tix import Form
from django.contrib.auth.models import User
from tabnanny import check
# from turtle import title
from urllib import response
from webbrowser import get
from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.views import View
from blog import models
from django.contrib.auth import login ,authenticate
import requests

# Create your views here.s import UserI


class View_1(View):
    def get(self,request):
        data_list = models.UserInfo.objects.all()
        # print(data_list)
        return render(request, 'view1.html')


class View_2(View):
    # if request.method == "GET":
    def get(self,request):
        return render(request, 'view2.html')
    def post(self,request):
        # 登陆
        account = request.POST.get("account")
        password_up = request.POST.get("password_up")
        # form = AuthenticationForm(data=request.POST)
        # 登陆检测
        if account and password_up:
            check_user = models.UserInfo.objects.filter(username=account)
            check_password = models.UserInfo.objects.filter(
                passwords=password_up)
            if check_user:
                if check_password:
                    user = authenticate(request, username=account, passwords=password_up)
                    if user.is_authenticated:

                        # login(request, user)
                        response = redirect('/view3/')
                        login(request,user)
                        return response 
                else:
                    return render(request, 'view2.html', {"wrong": "密码错误!!"})
            else:
                # print (request.POST)
                return render(request, 'view2.html', {"wrong": "用户不存在！！"})
                # return HttpResponse("登陆失败")
        if account == '' or password_up == "":
            return render(request, 'view2.html', {"wrong": "账号或密码不能为空"})

        # 注册
        email = request.POST.get("email")
        username = request.POST.get("username")
        password_in = request.POST.get("password_in")
    
        # 添加到数据库
        if email and username and password_in:
            user = models.UserInfo.objects.create(username=username, email=email, passwords=password_in)
            user.save
            return render(request, 'view2.html', {"succese": "账号注册成功"})
        else:
            return render(request, "view2.html")

# def register(request):
#     if request.is_ajax():



class View_3(View):
    # def view_3(request):
    def get(self, request):
        # if request.method =="Get":
        return render(request, 'view3.html')
    # else:
    def post(self,request):
        title = request.POST.get("title")
        essay = request.POST.get("essay")
        if title and essay:
            user = models.Essay.objects.create(title=title, essay=essay)
            user.save
            return render(request, 'view3.html')
        else:
            return render(request, 'view3.html')

class Test(View):
    def get(self,request):
        return render(request,'test.html')
