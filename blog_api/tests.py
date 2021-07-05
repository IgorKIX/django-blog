from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Category


class PostTest(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, format='json')

        self.test_category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create_user(username='test_user1', password='123456789')
        data = {'title': 'Post title', 'author_id': 1, 'excerpt': 'Post excerpt', 'content': 'Post content'}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
