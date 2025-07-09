"""
URL configuration for leave_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views  # ✅ Required for login/logout

from leave_app.views import view_requests, login_view, approve_leave, reject_leave
from leave_app.views import submit_leave_request  # ✅ Actual view name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),
    path('submit/', submit_leave_request, name='submit_leave'),
    path('requests/', view_requests, name='view_requests'),
    path('login/', login_view, name='login'),
    path('approve/<int:leave_id>/', approve_leave, name='approve_leave'),
    path('reject/<int:leave_id>/', reject_leave, name='reject_leave'),

    # ✅ Django built-in login view
    path('accounts/login/', auth_views.LoginView.as_view(template_name='leave_app/login.html'), name='login'),
]
