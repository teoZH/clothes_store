from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('login/', views.logIN, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.log_out, name='logout'),
]
