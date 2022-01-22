""" common.forms.py """

# django의 관리자 페이지에서 사용하는 Form을 수정하기 위해
# 자체적으로 Custom User Model에 맞는 Form을 생성

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


# 사용자 생성 Form
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'phone_num', 'company_name',
                  'company_address', 'company_tel', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다!!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


# 사용자 수정 Form
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('user_id', 'password', 'user_name', 'phone_num', 'company_name',
                  'company_address', 'company_tel', 'email', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class SignupForm(UserCreationForm):
    user_id = forms.CharField(max_length=50, help_text='Required. Add a velid user id.')

    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'password1', 'password2')



