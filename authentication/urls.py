from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.login, name='register'),
    path('logout/', views.login, name='logout'),
]
