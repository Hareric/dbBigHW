# coding=utf-8
"""
Author = Eric_Chan
Create_Time = 2016/02/19
Introduction
    记录提交的表格的格式
"""

from django import forms


class LoginForm(forms.Form):
    """
    系统所提交的表单格式
    """
    ID_number = forms.CharField(max_length=11)  # 学号
    password = forms.CharField(widget=forms.PasswordInput())  # 密码

