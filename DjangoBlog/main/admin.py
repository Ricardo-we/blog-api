from django.contrib import admin
from .models import Users, Posts, PostComments

# Register your models here.
admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(PostComments)