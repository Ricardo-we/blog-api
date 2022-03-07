from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=240, unique=True)
    password = models.CharField(max_length=240)
    gmail = models.CharField(max_length=240, unique=True)
    administrator_permissions = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Posts(models.Model):
    heading = models.CharField(max_length=200)
    image = models.ImageField(upload_to='dj-blog/posts-headings/', null=True)
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='username')
    last_update = models.DateField(auto_now=True)
    likes = models.IntegerField(default=0);

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class PostComments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateField(auto_now=True, null=True)

    class Meta:
        verbose_name  = "Post comment"
        verbose_name_plural = "Post comments"