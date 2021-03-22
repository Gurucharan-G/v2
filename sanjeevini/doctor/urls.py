from django.urls import path
from . import views

urlpatterns = [
    path('doctor_sinup', views.doctor_signup, name='doctor_signup'),
    path('doctor_login', views.doctor_log, name='doctor_log'),
]