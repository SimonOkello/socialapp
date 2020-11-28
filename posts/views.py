from django.shortcuts import render

# Create your views here.
from .models import Post, Comment, Like


def post_comment_create_and_list_view(request):
    qs = Post.objects.all()

    return render(request, 'posts/index.html', {'qs': qs})
