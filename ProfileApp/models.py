from django.db import models
from home.models import Post, Story
from django.contrib.auth.models import User
from  django.db.models.signals import post_save
from django.utils import timezone
from PIL import Image


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True , blank = True)
    profile_stories = models.ForeignKey(Story, on_delete=models.CASCADE, null=True , blank = True)
    profile_image = models.ImageField(upload_to='profile_imgs' , default='profile_imgs/profile_defualt.png')
    bio = models.TextField(max_length=200, null=True , blank = True)
    following = models.ManyToManyField('Profile', blank=True ,symmetrical=False ,related_name='Following')
    followers = models.ManyToManyField('Profile', blank=True ,symmetrical=False , related_name='number_followers')

   
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)
        if img.width > 300 or img.height > 300:
            img.thumbnail((300,300))
            img.save(self.profile_image.path)




def creat_profile(sender, instance, created ,*args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(creat_profile,sender=User)

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.SET_NULL, null=True)
    influncer = models.ForeignKey(User, related_name='influncer', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.follower} follows {self.influncer}"
