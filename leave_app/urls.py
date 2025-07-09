from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('submit/', views.submit_leave_request, name='submit_leave'),
    path('requests/', views.view_leave_requests, name='view_requests'),
    path('login/', auth_views.LoginView.as_view(template_name='leave_app/login.html'), name='login'),
    path('approve/<int:leave_id>/', views.approve_leave, name='approve_leave'),
    path('reject/<int:leave_id>/', views.reject_leave, name='reject_leave'),
]


