from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import Post
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name='post_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'