from django.contrib import admin
from .models import Friends, Like, Messages, Tweet
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Friends)
admin.site.register(Like)
admin.site.register(Messages)