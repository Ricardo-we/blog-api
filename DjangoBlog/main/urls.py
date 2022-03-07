from django.urls import path
from .views import users, posts, check_user, post_comments

urlpatterns = [
    path('users/', users, name='Users'),
    path('users/<int:id>', users),
    path('check-user/', check_user),
    path('posts/', posts, name='Posts'),
    path('posts/user/<str:username>', posts),
    path('posts/<int:id>', posts),
    path('post-comments/', post_comments, name="PostComments"),
    path('post-comments/<int:post_id>', post_comments)
]