from django.db import models


# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    jmbg = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f' {self.name} - {self.surname}'


class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=100)
    jmbg = models.CharField(max_length=20)
    indexNumber = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name} - {self.surname} - {self.indexNumber}'
