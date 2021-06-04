from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200, default='Post')
    author= models.ForeignKey('auth.User',  on_delete= models.CASCADE , related_name='User', null=True)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail' , args=[str(self.id)])