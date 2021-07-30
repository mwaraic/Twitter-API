from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Messages(models.Model):
    
    sender= models.ForeignKey(User, models.DO_NOTHING, db_column='user1', related_name='sender')
    to= models.ForeignKey(User, models.DO_NOTHING, db_column='user2',related_name='to')
    message=models.CharField(max_length=250, blank=False) 
    when= models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):

    user = models.ForeignKey(User, models.DO_NOTHING, db_column='username')
    body = models.CharField(max_length=250, blank=False) 
    date= models.DateTimeField(auto_now_add=True)


class Friends(models.Model):

    handle1= models.ForeignKey(User, models.DO_NOTHING, db_column='user1', related_name='handle1')
    handle2= models.ForeignKey(User, models.DO_NOTHING, db_column='user2',related_name='handle2')
    since= models.DateTimeField(auto_now_add=True)
    
    class Meta:
          unique_together = (('handle1', 'handle2'),)

class Like(models.Model):

    user = models.ForeignKey(User, models.DO_NOTHING)
    tweet = models.ForeignKey(Tweet, models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
         unique_together = (('user', 'tweet'),)

class Thread(models.Model):
      
    user=models.ForeignKey(User, models.DO_NOTHING)


class ThreadTweet(models.Model):

   threadid=models.ForeignKey(Thread, models.DO_NOTHING)
   user=models.ForeignKey(User, models.DO_NOTHING)
   tweet=models.ForeignKey(Tweet, models.DO_NOTHING)
