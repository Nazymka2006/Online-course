from django import forms
from django.contrib.auth.models import User
from .models import Student, Teacher, HomeworkSubmission, Course


from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = []

class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['bio']


class HomeworkSubmissionForm(forms.ModelForm):
    class Meta:
        model = HomeworkSubmission
        fields = ['file']

# для выбора курсов
class CourseEnrollmentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Выберите курсы"
    )

    class Meta:
        model = Student

        fields = ['courses']


