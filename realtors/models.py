from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_mvp = models.BooleanField(default=False)
    hiredate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
