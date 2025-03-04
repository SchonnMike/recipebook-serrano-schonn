from django.db import models

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50, default="")
    otherRemarks = models.CharField(max_length=50, default="")

class MyNewTable(models.Model):
    custom_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)