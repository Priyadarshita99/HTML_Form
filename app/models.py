from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(primary_key=True,max_length=50)
    Slocation=models.CharField(max_length=50)
    Sprincipal=models.CharField(max_length=50)

    def __str__(self):
        return self.Sname