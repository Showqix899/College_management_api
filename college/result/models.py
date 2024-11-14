from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
from student.models import Student
from teacher.models import Teacher
from teacher.models import Subject


class StudentResult(models.Model):
    student_name=models.CharField(max_length=200,default="blank")
    student_id=models.CharField(max_length=200 ,default="blank")
    teacher_name=models.CharField(max_length=200,default="blank")
    subject_name=models.CharField(max_length=200,default="blank")
    marks=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student_name} marks"