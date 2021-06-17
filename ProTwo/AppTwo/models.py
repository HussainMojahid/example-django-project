from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.fname

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic',blank = True)

    def __str__(self):
        return self.user.username