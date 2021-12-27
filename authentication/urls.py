from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.logIN, name='login'),
    path('register/', views.register, name='register'),
    path('change/', views.change_password, name='change_pass'),
    path('forgotten/', views.forgotten, name='forgotten'),
    path('forgotten/done/', views.done, name='done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('logout/', views.log_out, name='logout'),
]
