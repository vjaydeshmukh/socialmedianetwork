from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  django.db.models.signals import post_save
from PIL import Image


# # Create your models here.

COLLOR_AFTER_WHATCH =(
    ('R','red'),
    ('B','grey')
)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    po = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', null = True , blank = True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} comments on {self.po.author}\'s image"
    class Meta:
        ordering = ('-date',)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    po = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes_related_name', null = True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user} Likes {self.po}"
    class Meta:
        ordering = ('-date',)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_imgs' )
    discription = models.TextField(max_length=1000)
    post_likes_number = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author.username} post"

    class Meta:
        ordering = ('-date',)

def add24hs():
    return timezone.now() + timezone.timedelta(days=1)
        
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_imgs', null=True,blank=True )
    discription = models.TextField(max_length=1000, null=True,blank=True)
    views = models.IntegerField(default=0)
    collor = models.CharField(max_length=1,choices=COLLOR_AFTER_WHATCH,default='R')
    posting_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=add24hs)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author.username} story"


    class Meta:
        ordering = ('-posting_date',)
        
