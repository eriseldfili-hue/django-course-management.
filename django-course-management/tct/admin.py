from django.contrib import admin

from tct.courses.models import Course
from tct.courses.models.course import Teacher
from tct.courses.models.course import Student

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
