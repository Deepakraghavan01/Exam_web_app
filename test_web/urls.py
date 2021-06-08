"""test_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_test import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path(r'',views.home),
    path(r'Admin/',views.Admin),
    path(r'Admin/question_dash/',views.question_dash),
    path(r'Admin/add_student/',views.add_student),
    path(r'Admin/stu_det/',views.stu_det),
    path(r'Admin/question_add/',views.question_add),
    path(r'Admin/add/',views.add),
    path(r'Admin/db/',views.db),
    path(r'Admin/view_question/',views.view_question),
    path(r'Admin/Exam/',views.Exam),
    path(r'Admin/save_exam/',views.save_exam),
    path(r'Student/',views.Student),
    path(r'Student/student_dash/',views.student_dash),
    path(r'Student/student_exam/',views.student_exam),
    path(r"Student/student_mark/",views.student_mark),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
