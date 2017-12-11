from django.db import models

# Create your models here.
class Files_from_client(models.Model):
#Тестовая модель для возможности передачи тектста и файла
    name = models.CharField(max_length=100)
    file = models.FileField()

