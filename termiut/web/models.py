from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    course_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class C_Time(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    ex_time = models.DateTimeField()
    sec_time = models.DateTimeField()
    teacher = models.CharField(max_length=30)

