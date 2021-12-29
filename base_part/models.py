from django.db import models
import uuid
from django.utils import timezone


class Clothes(models.Model):
    cloth_type = models.CharField(max_length=20)
    image = models.ImageField(upload_to='base/')
    pub_date = models.DateTimeField('date published', default=timezone.now())
    description = models.TextField(max_length=200)
    price = models.FloatField(blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.cloth_type
