
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, StudentRegisterForm, TeacherRegisterForm, HomeworkSubmission, CourseEnrollmentForm
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.models import User
from .models import Student, Teacher, Course, HomeworkSubmission
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

def payment_page(request, pk):
    return HttpResponse(f"Оплата курса с id {pk}")


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'home_page.html', {'courses': courses})


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
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def submit_homework(request, homework_id):
    homework = get_object_or_404(Homework, id=homework_id)
    student = get_object_or_404(Student, user=request.user)

    if request.method == 'POST':
        form = HomeworkSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.homework = homework
            submission.student = student
            submission.save()
            return redirect('home')  # можешь изменить на 'student_profile'
    else:
        form = HomeworkSubmissionForm()

    return render(request, 'submit_homework.html', {
        'form': form,
        'homework': homework,
    })

def login_register_page(request):
    login_form = AuthenticationForm()
    student_user_form = UserRegisterForm()
    teacher_user_form = UserRegisterForm()
    student_form = StudentForm()
    teacher_form = TeacherForm()
    return render(request, 'login_register.html', {
        'login_form': login_form,
        'student_user_form': student_user_form,
        'student_form': student_form,
        'teacher_user_form': teacher_user_form,
        'teacher_form': teacher_form,
    })


# views.py
from django.contrib.auth.decorators import login_required

@login_required
def enroll_courses(request):
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')  # или 'student_dashboard'
    else:
        form = CourseEnrollmentForm(instance=student)

    return render(request, 'enroll_courses.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    enrolled_courses = student.courses.all()
    return render(request, 'student_dashboard.html', {
        'student': student,
        'courses': enrolled_courses
    })

from django.contrib.auth.decorators import login_required
from .models import Teacher, Course

@login_required
def teacher_dashboard(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
        courses = Course.objects.filter(teacher=teacher)
    except Teacher.DoesNotExist:
        teacher = None
        courses = []

    return render(request, 'teacher_dashboard.html', {
        'teacher': teacher,
        'courses': courses
    })

from .forms import CourseCreateForm

@login_required
def create_course(request):
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = teacher  # автоматическая привязка
            course.save()
            return redirect('teacher_dashboard')
    else:
        form = CourseCreateForm()

    return render(request, 'create_course.html', {'form': form})






print("Hello from feature-new")
