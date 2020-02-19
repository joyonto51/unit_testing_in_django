from django.contrib import admin
from .models import SchoolClass, Student

from django.contrib.admin.sites import AdminSite

# Register your models here.
models = [SchoolClass, Student]
admin.site.register(models)

# class SchoolAdminSite(AdminSite):
#     login_form = 'admin/login.html'
#
#
# school_admin_site = SchoolAdminSite()