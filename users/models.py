from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=100)
    email=models.EmailField()
    
    @classmethod
    def search_user(cls,username):
        return User.objects.filter(username__icontains = username)

    def save_profile(self):
        self.save()
    def __str__(self):
        return f'{self.user.username} Profile'

