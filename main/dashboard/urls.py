from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    # ---------------workers---------------
    path('worker-create/', views.worker_create, name='worker_create'),
    path('worker-list/', views.worker_list, name='worker_list'),
    path('worker-edit/<int:id>/', views.worker_edit, name='worker_edit'),
    path('worker-delete/<int:id>/', views.worker_delete, name='worker_delete'),
    path('attendance-list/', views.attendance_list, name='attendance_list'),
    # path('worker-detail/<int:pk>/', views.worker_detail, name='worker_detail'),
    # ---------------profile----------------
    path('profile-update/', views.profile_update, name='profile_update'),
    path('password-update/', views.edit_password, name='edit_password'),
    # --------------auth------------------
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('logout-page/', views.logout_page, name='logout_page'),
]
