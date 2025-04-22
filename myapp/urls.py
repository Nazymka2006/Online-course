from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/payment/', views.payment_page, name='payment_page'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

