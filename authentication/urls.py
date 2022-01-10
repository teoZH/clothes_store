from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.logIN, name='login'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    #path('register/', views.register, name='register'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    #path('change/', views.change_password, name='change_pass'),
    path('change/', views.CustomPasswordChangeView.as_view(), name='change_pass'),
    #path('forgotten/', views.forgotten, name='forgotten'),
    path('forgotten/', views.CustomPasswordResetView.as_view(), name='forgotten'),
    path('forgotten/done/', views.CustomPasswordResetDoneView.as_view(), name='done'),
    #path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('logout/', views.log_out, name='logout'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout')
]
