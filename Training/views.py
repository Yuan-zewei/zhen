from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post_list(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_list.html', {'post': post})


class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'publish', 'body')
    template_name = 'post_update.html'
    success_url = reverse_lazy('select')


class PostCreate(CreateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'post_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.publish = timezone.now()
        return super().form_valid(form)
