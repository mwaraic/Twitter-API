from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Messages, Tweet
from django.test import TestCase
from django.test import Client

class LoginRegistrationTest(TestCase):
    
    """
    Ensure we can create a new user object and log it in.
    """
    
    def test_login_registration(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertTrue(logged_in) 
        
class MessageTests(APITestCase):
    def test_create_message(self):
        
        """
        Ensure we can create a new message object.
        """
        
        self.client.force_login(User.objects.get_or_create(username='test')[0])
        url = reverse('message', kwargs={'senderid':'1'})
        data = {'message': 'DabApps'}
        response = self.client.post(url, data, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Messages.objects.count(), 1)
        self.assertEqual(Messages.objects.get().message, 'DabApps')
        
class TweetTests(APITestCase):
    
    def test_create_tweet(self):
        
        """
        Ensure we can create a new tweet object.
        """
        
        self.client.force_login(User.objects.get_or_create(username='test')[0])
        url = reverse('tweet')
        data = {'body': 'DabApps'}
        response = self.client.post(url, data, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().body, 'DabApps')
        
    def test_read_tweet(self):
        
        """
        Ensure we can read an existing tweet object.
        """
        
        tweet=Tweet.objects.get_or_create(user=User.objects.get_or_create(username='test')[0], id=1)[0]
        self.client.force_login(User.objects.get_or_create(username='test')[0])
        response = self.client.get(reverse('tweet-detail', kwargs={'pk': tweet.id}), format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_update_tweet(self):
        
        """
        Ensure we can update an existing tweet object.
        """
        
        tweet=Tweet.objects.get_or_create(user=User.objects.get_or_create(username='test')[0], id=1)[0]
        self.client.force_login(User.objects.get_or_create(username='test')[0])
        data={'body':'DabApps'}
        response = self.client.put(reverse('tweet-detail', kwargs={'pk': tweet.id}),data, format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tweet.objects.get_or_create(user=User.objects.get_or_create(username='test')[0], id=1)[0].body, 'DabApps')

    def test_delete_tweet(self):
        
        """
        Ensure we can delete an existing tweet object.
        """
        
        tweet=Tweet.objects.get_or_create(user=User.objects.get_or_create(username='test')[0], id=1)[0]
        self.client.force_login(User.objects.get_or_create(username='test')[0])
        data={'body':'DabApps'}
        response = self.client.delete(reverse('tweet-detail', kwargs={'pk': tweet.id}),data, format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
