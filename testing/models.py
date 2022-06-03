from djongo import models

class Testing(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email =models.CharField(max_length=255)
    number = models.CharField(max_length=50)