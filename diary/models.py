from django.db import models

class Data(models.Model):
    title=models.CharField(max_length=50)
    page=models.CharField(max_length=500)
    datetime=models.TimeField(auto_now=True)