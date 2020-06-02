from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    address=models.CharField(max_length=50 ,blank=True,null=True)
    bio=models.CharField(max_length=100,blank=True,null=True)
    
    
    
    @classmethod
    def search_user(cls,username):
        return User.objects.filter(username__icontains = username)

    def save_profile(self):
        self.save()
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
class Follower(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User,on_delete=models.CASCADE,  related_name='followers')
    
    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)            