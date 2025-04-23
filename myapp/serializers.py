from rest_framework import serializers
from .models import Course, Lesson, Student, Teacher, Homework, HomeworkSubmission, Payment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'bio']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher']

class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'video', 'created_at']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'courses']

class HomeworkSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = Homework
        fields = ['id', 'lesson', 'description', 'deadline']

class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    homework = HomeworkSerializer()

    class Meta:
        model = HomeworkSubmission
        fields = ['id', 'homework', 'student', 'file', 'submitted_at']

class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Payment
        fields = ['id', 'student', 'course', 'is_paid', 'created_at']
