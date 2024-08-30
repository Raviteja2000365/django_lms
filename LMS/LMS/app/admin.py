from django.contrib import admin
from .models import quiz,Courses,assignments,announcements
# Register your models here.

admin.site.register(Courses)
admin.site.register(assignments)
admin.site.register(announcements)
admin.site.register(quiz)
