from django.db import models

# Create your models here.
class Image(models.Model):
    image_name=models.CharField(max_length=50)
    image=image=models.ImageField(upload_to= 'images/')
    caption = models.CharField(max_length=250, blank=True)

