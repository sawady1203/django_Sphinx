from django.db import models

# Create your models here.

class SampleTable(models.Model):
    """これはサンプルモデルです"""
    name = models.CharField(verbose_name="名前", max_length=20, blank=True, null=True)