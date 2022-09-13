from django.db import models

# Create your models here.

class HadishModel(models.Model):
    hadish_name=models.TextField()
    narated_by=models.CharField(max_length=100)
    created_at=models.DateField()

