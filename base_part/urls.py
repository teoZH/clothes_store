from django.urls import path

from base_part import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('details/<uuid:cloth_id>/', views.DetailsView.as_view(), name='details'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('edit/<uuid:cloth_id>/', views.EditView.as_view(), name='edit'),
    path('delete/<uuid:cloth_id>/',views.DeleteView.as_view(), name='delete')
]
