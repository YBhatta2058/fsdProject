from django.db import models


class Course(models.Model):
    name = models.CharField(max_length = 100)
    credits = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default = MALE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    courses = models.ManyToManyField(Course,related_name="students",blank=True)

    def __str__(self):
        return self.name