from django.contrib import admin

# Register your models here.
from .models import Student, People


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
        pass