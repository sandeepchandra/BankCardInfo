from django.db import models

# Create your models here.

class Card(models.Model):
    scheme = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    brand = models.CharField(max_length=40)
    prepaid = models.BooleanField()
    country = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    name = models.CharField(max_length=125)
    url = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


