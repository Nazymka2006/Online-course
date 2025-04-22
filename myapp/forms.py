from django import forms
from django.contrib.auth.models import User
from .models import Student, Teacher

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = []

class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['bio']