from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course_search/', views.course_search, name='course_search'),
    path('course_detail/', views.course_detail, name='course_detail'),
]