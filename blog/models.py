from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    video = models.FileField(upload_to='media/videos/', null=True, blank=True)
    content = models.TextField()
    link = models.URLField(null=True, blank=True)
    puplish = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ('-puplish',)
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title



class Post_Like(models.Model):
    post = models.IntegerField(default=0)
    user = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Post_Like"
        verbose_name_plural = "Post_Likes"


class Post_Comment(models.Model):
    post = models.IntegerField(default=0)
    user = models.CharField(max_length=150)
    comment = models.CharField(max_length=1000)


    class Meta:
        verbose_name = "Post_Comment"
        verbose_name_plural = "Post_Comments"


