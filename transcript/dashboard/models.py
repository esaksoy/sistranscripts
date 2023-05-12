from django.db import models
from django.db.models import ImageField
# Create your models here.
class Class(models.Model):
    classid = models.IntegerField(primary_key=True)
    classname = models.CharField(max_length=50)
    classyear = models.CharField(max_length=10)
    classgrade = models.CharField(max_length=100, default='A')

    def __str__(self):
        return self.classname


class Student(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    dateofenrolment = models.DateField()
    nationality = models.CharField(max_length=50)
    dateofgraduation = models.DateField(null=True, blank=True)
    photo = ImageField(upload_to='images/', null=True, blank=True)
    classes = models.ManyToManyField(Class, related_name='students')


    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class grades_pdf(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
