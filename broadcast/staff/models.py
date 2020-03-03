from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default= False)
    is_parent = models.BooleanField(default= False)
    bio = models.TextField()
    birth_date = models.DateField(default=None)
    address = models.CharField(max_length=100,default=None)

class Grade(models.Model):
    garde_name = models.CharField(max_length=10)
    description = models.TextField()

class Student(models.Model):
    student_name = models.CharField(max_length=10)
    grade_id = models.ForeignKey(Grade,on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()
    mother_tongue = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)

class Staff(models.Model):
    grade_id = models.OneToOneField(Grade,on_delete=models.CASCADE)
    staff_id = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    subject_handling = models.CharField(max_length=10)

class Parent(models.Model):
    parent_id = models.OneToOneField(User,on_delete=models.CASCADE)
    student_id = models.OneToOneField(Student,on_delete=models.CASCADE)
    monthly_income = models.IntegerField()
    occupation = models.CharField(max_length=10)

class Message(models.Model):
    grade_id = models.ForeignKey(Grade,on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    file_path = models.FileField()
    pub_date = models.DateField()
    topic_body = models.TextField()
    topic_title = models.CharField(max_length=50)

class Status(models.Model):
    status_name= models.CharField(max_length=10)

class Message_track(models.Model):
    grade_id = models.ForeignKey(Grade,on_delete=models.CASCADE)
    message_id = models.ForeignKey(Message,on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)