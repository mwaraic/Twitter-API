from rest_framework import serializers
from .models import Friends, Messages, Thread, Tweet, Like, ThreadTweet


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields=['sender','message', 'when']

class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model= Tweet
        fields= ['id', 'body','date']

class RetweetSerializer(serializers.ModelSerializer):

    class Meta:
        model= Tweet
        fields= ['id']

class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model= Tweet
        fields= '__all__'

class FriendsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Friends
        fields= ['handle2', 'since']

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Like
        fields=['id', 'user', 'tweet']

class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
         model=Thread
         fields=['id']

class ThreadTweetSerializer(serializers.ModelSerializer):

    class Meta:
        model=ThreadTweet
        fields=['tweet']