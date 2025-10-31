from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
