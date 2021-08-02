"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Task1.views import MessagesViewSet, ThreadViewSet,ThreadTweetViewSet,FriendsViewSet,RetweetViewSet,LikesViewSet, MyTweetsViewSet, HomeViewSet, LikeUnlikeViewSet, ProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/<int:senderid>', MessagesViewSet.as_view({'get':'list','post':'create'}), name='message'),
    path('retweet/<int:pk>', RetweetViewSet.as_view({'get':'list', 'post': 'create'})),
    path('mytweets/', MyTweetsViewSet.as_view({'get':'list', 'post': 'create'}),name='tweet'),
    path('mytweets/<int:pk>/', MyTweetsViewSet.as_view({'get':'retrieve', 'put': 'update', 'delete':'destroy'}), name='tweet-detail'),
    path('friends/', FriendsViewSet.as_view({'get':'list','post': 'create'})),
    path('friends/<int:handle2>/', FriendsViewSet.as_view({'get':'retrieve','delete': 'destroy'})),
    path('home/', HomeViewSet.as_view({'get':'list'})),
    path('thread/', ThreadViewSet.as_view({'get':'list', 'post':'create'})),
    path('thread/<int:threadid>', ThreadTweetViewSet.as_view({'get':'list', 'post': 'create'})),
    path('profile/<int:id>/', ProfileViewSet.as_view({'get':'list'})),
    path('likes/', LikesViewSet.as_view({'get':'list'})),
    path('likes/<int:pk>/', LikeUnlikeViewSet.as_view({'post':'create','delete':'destroy'})),
    path('account/', include('dj_rest_auth.urls')),
    path('account/signup/', include('dj_rest_auth.registration.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
