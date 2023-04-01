from django.db import models

# Create your models here.


class Data(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    date_of_enrolment = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    date_of_graduation = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name
