from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just as test')
        
    def test_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just as test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='another test')
        
    def test_view_url(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        
    def test_templates(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'home.html')
        
class SimpleTests(SimpleTestCase):
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

class BlogTests(TestCase):
    def setUp(self) :
        self.user  = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        
        self.post = Post.objects.create(
            title='My Title',
            text='Nice view',
            author=self.user
        )
        
    def test_representation(self):
        post= Post(title='new title')
        self.assertEqual(str(post), post.title)
                
    def test_get_absolute(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')
        
    # def test_post_content(self):
    #     self.assertEqual
    