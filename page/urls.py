from django.urls import path
from .views import HomePageView , AboutPageView , BlogDetailView , BlogCreateView , BlogUpdateView , BlogDeleteView

urlpatterns = [
                path('post/<int:pk>/edit/' , BlogUpdateView.as_view(), name='post_edit'),
                path('post/<int:pk>/delete/' , BlogDeleteView.as_view(), name='page_delete'),
                path('', HomePageView.as_view(), name='home'),
                path('about/', AboutPageView.as_view(), name = 'about'),
                path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
                path('post/new/', BlogCreateView.as_view(),name = 'post_new'),
                
            ]
