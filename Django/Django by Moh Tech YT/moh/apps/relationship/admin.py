from django.contrib import admin
from .models import User, Profile, Category, Products, Course, Student

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Course)
admin.site.register(Student)
