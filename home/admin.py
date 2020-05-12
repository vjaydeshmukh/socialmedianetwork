from django.contrib import admin
from .models import Comments, Post,  Like, Story

# Register your models here.

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Story)
