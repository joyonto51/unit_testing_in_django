from django.contrib import admin
from .models import SchoolClass, Student

# Register your models here.
models = [SchoolClass, Student]
admin.site.register(models)