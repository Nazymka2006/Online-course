from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='home'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/payment/', views.payment_page, name='payment_page'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit_homework/<int:homework_id>/', views.submit_homework, name='submit_homework'),
    path('enroll/', views.enroll_courses, name='enroll_courses'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),



]

