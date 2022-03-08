from .models import PostComments, Posts, Users
from rest_framework import serializers, viewsets

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'gmail']


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'heading', 'body', 'author', 'image', 'last_update', 'likes']

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['id', 'comment', 'post', 'comment_date']
