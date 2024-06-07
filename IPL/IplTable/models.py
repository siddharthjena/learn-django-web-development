from django.db import models

# Create your models here.
class Table(models.Model):
    tid = models.IntegerField()
    tname = models.CharField(max_length = 50)
    p = models.IntegerField()
    w = models.IntegerField()
    l = models.IntegerField()
    d = models.IntegerField()
    points = models.IntegerField()

    