from django.db import models
from django.db import models
from datetime import date
from django.contrib.auth.models import  User

#lines = [('EP-1','EP-1'),('EP-2A','EP-2A'),('EP-2B','EP-2B'),('EP-3A','EP-3A'),('EP-3B','EP-3B'),('EP-4','EP-4'),('EP-5A','EP-5A'),('EP-5B','EP-5B'),('EP-6','EP-6'),('EP-7A','EP-7A'),('EP-7B','EP-7B'),('EP-8A','EP-8A'),('EP-8B','EP-8B'),('EP-9','EP-9'),('EP-10','EP-10'),('EP-11A','EP-11A'),('EP-11B','EP-11B'),('EP-12','EP-12'),('EP-13','EP-13'),('EP-14A','EP-14A'),('EP-14B','EP-14B'),('EP-15A','EP-15A'),('EP-15B','EP-15B'),('EP-16A','EP-16A'),('EP-16B','EP-16B'),('EP-17','EP-17'),('EP-18','EP-18'),('EP-19','EP-19'),('EP-20','EP-20'),('EP-21','EP-21'),('EP-22','EP-22')]



class ie(models.Model):
    month = models.CharField(max_length = 20, default =0)
    year = models.IntegerField(default =0 )
    day = models.IntegerField(default =0)

    shift_hours = models.FloatField(default =0)
    description = models.CharField(max_length= 100,default =0)
    project = models.CharField(max_length= 100,default = 0)

class total(models.Model):
    year = models.IntegerField(default =0)
    january =  models.IntegerField(default =0)
    feb = models.IntegerField(default =0)
    march = models.IntegerField(default =0)
    april = models.IntegerField(default=0)
    may = models.IntegerField(default=0)
    june = models.IntegerField(default=0)
    july = models.IntegerField(default=0)
    august = models.IntegerField(default=0)
    september = models.IntegerField(default=0)
    octuber = models.IntegerField(default=0)
    november = models.IntegerField(default=0)
    december = models.IntegerField(default=0)


# Create your models here.
