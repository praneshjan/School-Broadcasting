from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from staff.validators import alpha, valuelength, highvaluelength
# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default= False)
    is_parent = models.BooleanField(default= False)
    bio = models.TextField(validators=[highvaluelength])
    birth_date = models.DateField(default=None)
    address = models.CharField(max_length=100, default=None, validators=[highvaluelength])

class Grade(models.Model):
    garde_name = models.CharField(max_length=10, validators=[valuelength])
    description = models.TextField(validators=[highvaluelength])
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact",)
    def __str__(self):
        return self.garde_name
class Student(models.Model):
    student_name = models.CharField(max_length=10, validators=[alpha, valuelength])
    grade_id = models.ForeignKey(Grade,on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()
    mother_tongue = models.CharField(max_length=10, validators=[valuelength])
    nationality = models.CharField(max_length=10, validators=[alpha, valuelength])
    def __str__(self):
        return self.student_name
class Staff(models.Model):
    grade_id = models.OneToOneField(Grade,on_delete=models.CASCADE)
    staff_id = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    subject_handling = models.CharField(max_length=10, validators=[valuelength])
    def __str__(self):
        return self.staff_id
class Parent(models.Model):
    parent_id = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
    monthly_income = models.PositiveIntegerField()
    occupation = models.CharField(max_length=10, validators=[valuelength])
    def __str__(self):
        return self.parent_id
class Message(models.Model):
    grade_id = models.ForeignKey(Grade,on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='documents/')
    pub_date = models.DateField()
    topic_body = models.TextField(validators=[highvaluelength])
    topic_title = models.CharField(max_length=50, validators=[valuelength])

    def save(self):
        self.pub_date = date.today()
        super(Message,self).save()
    def __str__(self):
        return self.topic_title
class Status(models.Model):
    status_name= models.CharField(max_length=10, validators=[valuelength])
    def __str__(self):
        return self.status_name
class Message_track(models.Model):
    grade_id = models.ForeignKey(Grade,on_delete=models.CASCADE)
    message_id = models.ForeignKey(Message,on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    def __str__(self):
        return self.message_id
class UserProxy(User):
    class Meta:
        proxy =True
        app_label = 'staff'
        verbose_name = 'New Request'
        verbose_name_plural = 'New Requests'