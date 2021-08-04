from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from .serializers import MessagesSerializer, TweetSerializer,ThreadTweetSerializer, ThreadSerializer, RetweetSerializer,LikeSerializer, FriendsSerializer, HomeSerializer
from .models import Messages, ThreadTweet, Tweet, Friends, Like, Thread
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import json

# Unit Tests remaining

class MessagesViewSet(viewsets.ModelViewSet):

    """

    Calls Messages method which serves the puropse of sending and
    recieving message from a user.

    Send a GET request on messages/<:userID> to retrieve a list
    of messages

    Send a POST request on messages/<:userID> with message property
    to send a message
    
    """

    serializer_class=MessagesSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]


    def get_queryset(self):

# A custome query on Messages model to filter incoming and outgoing messages
# by sender and reciever.
 
        list1=list(User.objects.filter(pk=self.kwargs['senderid']))
        list2=list(User.objects.filter(username=self.request.user))
        return Messages.objects.filter(sender__in=list1.__add__(list2), to__in=list1.__add__(list2)).order_by('when')
       
    
    def create(self, request,senderid):
        message=json.loads(json.dumps(request.data))['message']
        Messages.objects.create(sender=request.user, to=User.objects.get(id=senderid), message=message)
        return Response(status=status.HTTP_201_CREATED)

class MyTweetsViewSet(viewsets.ModelViewSet):

    """

    Calls My Tweets method which serves the purpose 
    of managing tweets of user. 
    Tweets can be created, updated, deleted, 
    and retireved.

    Send a GET request on mytweets/ to 
    retrieve the list of tweets

    Send a POST request with body property on mytweets/ to 
    create a tweet

    Send a PUT request on mytweets/<:tweetID> with
    updated tweet data to update the tweet

    Send a DELETE request on mytweets/<:tweetID> to
    delete a tweet

    """

    serializer_class=TweetSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Tweet.objects.filter(user=self.request.user).order_by('-date')
        
    
    def create(self, request):
      body=json.loads(json.dumps(request.data))['body']
      if(body==''):
        return Response(status=status.HTTP_204_NO_CONTENT)
      else:
        Tweet.objects.create(user=request.user, body=body)
        return Response(status=status.HTTP_201_CREATED)



class RetweetViewSet(viewsets.ModelViewSet):

    """

    Calls Retweet method which serves the purpose of 
    retweeting a tweet.

    Send a POST request on retweet/<:tweetID>
    to retweet a tweet.

    """

    serializer_class=RetweetSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    def get_queryset(self):
        return Tweet.objects.filter(pk=self.kwargs['pk'])
    
    def create(self,request, pk):
      rt=Tweet.objects.get(pk=pk)
      Tweet.objects.create(user=request.user, body="RT: "+str(rt.user)+" \n "+str(rt.body)+" \n "+str(rt.date))
      return Response(status=status.HTTP_201_CREATED)




class HomeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    """

    Calls Home method serves the purpose of 
    listing a user and his friends tweets
    
    Send a GET request on home/ to get the list
    of tweets

    """

    serializer_class=HomeSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):

# Two lists are passed into Tweet model. List1 is current user's friends
# and list2 is current user himself. This way a current user can view his and 
# his friend's tweets through home/ endpoint

        list1=list(Friends.objects.filter(handle1=self.request.user).values_list('handle2'))
        list2=list(User.objects.filter(username=self.request.user))
        return Tweet.objects.filter(user__in=list1.__add__(list2)).order_by('-date')



class FriendsViewSet(viewsets.ModelViewSet):
    """

    Calls Friends method which serves 
    the purpose of adding and removing 
    user's friends.
    
    Send a POST request with UserID 
    value against handle2 property
    to add a friend on friends/ 
    
    Send a DELETE request on    
    friends/<:userID> to remove a 
    friend
    
    """
    serializer_class=FriendsSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    lookup_field='handle2'

    def get_queryset(self):
        return Friends.objects.filter(handle1=self.request.user)

    def create(self, request):


        handle2=json.loads(json.dumps(request.data))['handle2']

#Checks whether friend is equal to current user or not

        if User.objects.get(pk=handle2)== request.user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
           Friends.objects.create(handle1=request.user, handle2=User.objects.get(pk=handle2))  
        except:
           return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

 

class LikeUnlikeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
  
    """

    Calls Like Unlike method which serves the purpose of 
    liking/unliking a tweet

    Send a POST request on likes/<:tweetID>
    to like a tweet

    Send a DELETE request on likes/<:tweetID>
    to delete a tweet
    
    """

    serializer_class=RetweetSerializer
    authentication_classes={SessionAuthentication, BasicAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Tweet.objects.filter(pk=self.kwargs['pk'])
    
    def create(self, request, pk):
        Like.objects.create(user=request.user, tweet=Tweet.objects.get(pk=pk))
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        a=Like.objects.get(user=request.user,tweet=Tweet.objects.get(pk=pk))
        a.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    
    """

    Calls Likes method which serves the purpose
    of getting the list of tweets user has liked.

    Send a GET request on likes/ to retrieve the 
    list of tweets user has liked.

    """

    serializer_class=LikeSerializer
    authentication_classes={SessionAuthentication, BasicAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)



class ProfileViewSet(viewsets.ModelViewSet):
   
    """

    Calls Profile which serves the purpose of 
    listing tweet timeline of any user.
    
    Send a GET request on profile/<:userID>
    to get the tweet timeline of user.

    """

    serializer_class=TweetSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Tweet.objects.filter(user=self.kwargs['id']).order_by('-date')

class ThreadViewSet(viewsets.ModelViewSet):
    """
    
    Calls Thread method which serves the purpose 
    of creating a new thread.

    Send a POST request on thread/ to create
    a new thread.

    Send a GET request on thread/ to retrieve the 
    list of threads.

    """
    serializer_class=ThreadSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return Thread.objects.filter(user=self.request.user)  

    def create(self, request):
        Thread.objects.create(user=request.user)
        return Response(status=status.HTTP_201_CREATED)   

class ThreadTweetViewSet(viewsets.ModelViewSet):
    """
    
    Calls Thread Tweet method which serves the purpose 
    of creating new tweets on a thread.

    Send a POST request on thread/<:threadID> with 
    body property to create a new tweet on a thread.

    Send a GET request on thread/<:threadID> to
    retrieve the list of tweets on a thread.

    """
    serializer_class=ThreadTweetSerializer
    authentication_classes={SessionAuthentication}
    permission_classes= [IsAuthenticated]
    
    def get_queryset(self):
        return ThreadTweet.objects.filter(threadid=self.kwargs['threadid'],user=self.request.user)  

    def create(self, request, threadid):
        body=json.loads(json.dumps(request.data))['tweet']
        if(body==''):
           return Response(status=status.HTTP_204_NO_CONTENT)
        else:
           tweet=Tweet.objects.create(user=request.user, body=body)
        ThreadTweet.objects.create(threadid=Thread.objects.get(pk=threadid), user=request.user, tweet=Tweet.objects.get(id=tweet.id))
        return Response(status=status.HTTP_201_CREATED)   

        
