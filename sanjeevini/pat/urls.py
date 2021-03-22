from django.urls import path
from . import views

urlpatterns = [
    path('', views.pat_signup, name='pat_signup'),
    path('', views.pat_log, name='pat_log'),
]