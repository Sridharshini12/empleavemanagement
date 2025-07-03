from django.contrib import admin

# Register your models here.

from .models import Employee, LeaveRequest

admin.site.register(Employee)
admin.site.register(LeaveRequest)
