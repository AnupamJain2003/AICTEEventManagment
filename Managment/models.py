# models.py in your app
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    num_students = models.IntegerField()
    host = models.CharField(max_length=255)  # Add host field

class Venue(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()
    booking_date = models.DateField()
    total_capacity = models.IntegerField()
    event = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=255)
    ui = models.CharField(max_length=255)
    emailId=models.EmailField()
    class_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    cgpa = models.FloatField()
    attendance = models.BooleanField()  # Add attendance field

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback_text = models.TextField()
