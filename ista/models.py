from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Image(models.Model):
    image_name=models.CharField(max_length=50)
    image=image=models.ImageField(upload_to= 'images/')
    caption = models.CharField(max_length=250, blank=True)
    date_posted=models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    
    def save_image(self):
        self.save() 
    def delete_image(self):
        self.delete()
    def total_likes(self):
        return self.likes.count()
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ["-pk"]
    def __str__(self):
        return self.image_name

class Comment(models.Model):
    class Meta:
        db_table = "comments"     
    image = models.ForeignKey(Image ,on_delete=models.CASCADE, related_name='comments')
    comment= models.TextField()
    pub_date = models.DateTimeField('Date of comment', default=timezone.now)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.content[0:200]
 
    class Meta:
        ordering = ["-pk"]