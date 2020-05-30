from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Image(models.Model):
    image_name=models.CharField(max_length=50)
    image=image=models.ImageField(upload_to= 'images/')
    caption = models.CharField(max_length=250, blank=True)
    date_posted=models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    
    def save_image(self):
        self.save() 
    def delete_image(self):
        self.delete()
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ["-pk"]
    def __str__(self):
        return self.image_name
class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following')
    following = models.ForeignKey(User, related_name='followers')
    
    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)       