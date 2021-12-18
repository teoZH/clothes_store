from django.db import models


class Clothes(models.Model):
    cloth_type = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=200)
    price = models.FloatField()

