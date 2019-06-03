# -*- coding:utf-8 -*-
from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Person(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length=20)
    cellphone_number = models.CharField(max_length=20)
    #Dans un cas réel, nous ne devrions pas stocker le mot de passe en clair.
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', on_delete=models.PROTECT)
    person_type = 'generic'
    def __str__(self):
        return self.first_name + " " + self.last_name

class Message(models.Model):
    author = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    publication_date = models.DateField()
    def __str__(self):
        if len(self.content) > 20:
            return self.content[:19] + "..."
        else:
            return self.content

class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Cursus(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)
    person_type = 'employee'

class Student(Person):
    cursus = models.ForeignKey('Cursus', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    person_type = 'student'
