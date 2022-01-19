from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    # userid = forms.CharField(max_length=32, required=True, label='아이디')  # username(실제 userid)와 여기서의 userid를 헷갈리지 말 것
    # phone_num = forms.CharField(max_length=32, required=True, label='휴대전화')
    email = forms.EmailField(max_length=128, required=True, label='이메일')
    # company_name = forms.CharField(max_length=32, required=True, label='회사명')
    # company_address = forms.CharField(max_length=64, required=True, label='회사 주소')
    # company_tel = forms.CharField(max_length=128, required=True, label='회사 전화')

    class Meta:
        model = User
        fields = (
                  # 'id',
                  # 'userid',
                  'username',
                  'password1',
                  'email',
                  # 'phone_num',
                  # 'company_name',
                  # 'company_address',
                  # 'company_tel'
                  )
