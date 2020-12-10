from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute__url(self):
        return reverse("post_list"),

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    shcool = models.ForeignKey(School,related_name='students',on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name
