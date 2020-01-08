from django.contrib import admin
from second.models import Post, Profile, StudentId, Attendance, Food

admin.site.register(StudentId)
admin.site.register(Attendance)
admin.site.register(Food)

admin.site.register(Post)
admin.site.register(Profile)
# Register your models here.
