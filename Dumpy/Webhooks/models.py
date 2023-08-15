from django.db import models

# Create your models here.

class WardDetails(models.Model):
    ward_no = models.IntegerField()
    area = models.CharField(max_length=100)
    sanitary_inspector = models.CharField(max_length=150)
    sanitary_supervisor = models.CharField(max_length=150)

    def __str__(self):
        return f"Ward {self.ward_no} - {self.area}"