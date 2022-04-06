from django.db import models

# Create your models here.
# Create your views here.

class Newton(models.Model):
    title = models.CharField(max_length=200)
    # body = models.TextField

