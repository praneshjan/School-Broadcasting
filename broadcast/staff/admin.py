from django.contrib import admin
from staff.models import User, Parent, Staff, Status, Message, Message_track, Grade, Student
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Status)
admin.site.register(Staff)
admin.site.register(Message)
admin.site.register(Message_track)
admin.site.unregister(Group)
admin.site.register(Grade)
admin.site.register(Student)