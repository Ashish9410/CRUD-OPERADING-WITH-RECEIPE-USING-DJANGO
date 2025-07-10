from django.db import models

# Create your models here.
class recepi(models.Model):
    recepi_name=models.CharField(max_length=100)
    recepi_description=models.TextField()
    recepi_image=models.ImageField(upload_to="recepi")
