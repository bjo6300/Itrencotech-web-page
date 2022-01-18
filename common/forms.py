from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    userid = forms.CharField(max_length=32, label='아이디')  # username(userid)와 name을 헷갈리지 말 것
    phone_num = forms.CharField(max_length=32, label='휴대전화')
    company_name = forms.CharField(max_length=32, label='회사명')
    company_address = forms.CharField(max_length=64, label='회사 주소')
    company_tel = forms.CharField(max_length=128, label='회사 전화')
    email = forms.EmailField(max_length=128, label='이메일')

    class Meta:
        model = User
        fields = ('id', 'username', 'password1', 'email')
