from django import forms
from .models import Task
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='이름')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='이름')
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'file_upload']
        labels = {
            'title': '제목',
            'description': '설명',
            'complete': '완료',
            'file_upload': '첨부파일 업로드',
        }
