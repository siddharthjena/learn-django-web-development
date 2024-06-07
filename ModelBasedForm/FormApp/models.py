from django.db import models

# Create your models here.
class RedgModel(models.Model):
    name = models.CharField(max_length = 30)
    dept = models.CharField(max_length = 30)
    mark = models.IntegerField()
    email = models.EmailField()