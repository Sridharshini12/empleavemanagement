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
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Required for login/logout

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ All app views like /submit, /requests will be handled inside leave_app.urls
    path('', include('leave_app.urls')),

    # ✅ Django built-in login/logout views
    path('accounts/login/', auth_views.LoginView.as_view(template_name='leave_app/login.html'), name='login'),
    
]