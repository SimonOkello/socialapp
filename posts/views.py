from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm, CommentModelForm


def post_comment_create_and_list_view(request):
    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    p_form = PostModelForm()
    c_form = CommentModelForm()
    if request.method == 'POST' and 'new_post' in request.POST:
        form = PostModelForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
    if request.method == 'POST' and 'new_comment' in request.POST:
        form = CommentModelForm(request.POST)
        post_id=request.POST.get('post_id')
        post=Post.objects.get(id=post_id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.post=post
            instance.save()
            p_form = PostModelForm()
    context = {
        'posts': posts, 'profile': profile, 'p_form': p_form, 'c_form': c_form
    }
    return render(request, 'posts/index.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post.liked.all():
            post.liked.remove(profile)
        else:
            post.liked.add(profile)
        like, created = Like.objects.get_or_create(
            user=profile, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
            post.save()
            like.save()
        return redirect('posts:post-list')
