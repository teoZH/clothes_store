from django.urls import path

from base_part import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<uuid:cloth_id>/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('edit/<uuid:cloth_id>/', views.edit, name='edit'),
    path('delete/<uuid:cloth_id>/',views.delete, name='delete')
]
