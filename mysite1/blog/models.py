from email.policy import default
import imp
from operator import mod
from pyexpat import model
from unicodedata import name
from django.db import models
from django import forms
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=128)
    passwords = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

# class UserFrom(forms.ModelForm):


class UserFrom(models.Model):
    # username = models.CharField(label='用户名', max_length=128)
    # passwords = models.CharField(label='密码', max_length=128)
    # email = models.EmailField(label='邮箱',max_length=128)
    username = models.CharField(max_length=128)
    passwords = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)


class Essay(models.Model):
    title = models.CharField(max_length=32)
    essay = models.CharField(max_length=3000)


class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()


# 新建数据
#Department.objects.create(title = "销售部")
