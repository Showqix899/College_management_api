from django.contrib import admin
from .models import Student,Department


# Register your models here.
admin.site.register(Department)
admin.site.register(Student)