from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_list(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_list.html', {'post': post})