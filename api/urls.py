from django.urls import path
from . import views

urlpatterns = [
    path('staff-list/', views.worker_list, name='staff-list'),
    path('attendance-create/', views.attendace_create, name='attendance-create'),
]