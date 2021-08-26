from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import Post
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name='post_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class BlogDetailView(DetailView):
    model=Post
    template_name= 'post-detail.html'
    context_object_name='postd'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author' , 'text']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title' , 'text']
    
class BlogDeleteView(DeleteView):
    model=Post
    template_name = 'page_delete.html'
    success_url = reverse_lazy('home')
    
