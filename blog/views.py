from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
