"""
common/forms.py
"""

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


# 사용자 생성 Form
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('userid', 'username', 'phone_num', 'company_name', 'company_address', 'company_tel', 'email')

    # 패스워드 검증
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 틀렸습니다.")
        return password2

    # 데이터 저장
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# 사용자 수정 Form
class UserChangeForm(forms.ModelForm):
    # 사용자의 패스워드를 read 권한으로 설정하여 수정하지 못하도록 함
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('userid', 'password', 'username', 'phone_num',
                  'company_name', 'company_address', 'company_tel', 'email', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
