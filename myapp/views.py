
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, StudentRegisterForm, TeacherRegisterForm
from django.contrib.auth.models import User
from .models import Student, Teacher, Course
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

def payment_page(request, pk):
    return HttpResponse(f"Оплата курса с id {pk}")


def home_page(request):
    return render(request, 'home.html')

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def register_student(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            Student.objects.create(user=user)
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        student_form = StudentRegisterForm()
    return render(request, 'register_student.html', {'user_form': user_form, 'student_form': student_form})

def register_teacher(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        teacher_form = TeacherRegisterForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        teacher_form = TeacherRegisterForm()
    return render(request, 'register_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

print("Hello from feature-new")
