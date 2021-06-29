from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Post,Category


"""REST API Views Testing"""

class PostTests(APITestCase):


    def test_view_posts(self):

        url = reverse('api:listcreate')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_post(self):

        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_superuser(username='test_user1',password='password1')

        self.client.login(username = self.testuser1.username,password='password1')
        data = {"title":"Post1","author":1,"category":1,"content":"New Post"}

        url = reverse('api:listcreate')
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_post_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username = 'test_user1',password='password1')
        self.testuser2 = User.objects.create_user(username = 'test_user2',password='password2')
        test_post = Post.objects.create(category_id=1,title='Post1',slug='post1',author_id=1,content='First Post',status='published')

        client.login(username=self.testuser1.username,password='password1')

        url = reverse(('api:detailcreate'), kwargs={'pk':1})

        response  = client.put(
            url,{
               "title":"Post 1",
               "content":"Post Update",
               "'author":1,
               "status":"draft"
            },
            format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




"""
# Model Testing

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username='test_user1',password='password1')
        test_post = Post.objects.create(
        category_id=1,title='Post1',slug='post1',author_id=1,content='First Post',status='published'
        )

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post1')
        self.assertEqual(content, 'First Post')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post1')
        self.assertEqual(str(category), 'django')
"""