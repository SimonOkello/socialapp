from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
from profiles.models import Profile


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='posts', validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    liked = models.ManyToManyField(
        to=Profile, blank=True, related_name='likes')
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.content[:20])

    def likes_count(self):
        return self.liked.all().count()
    
    def comments_count(self):
        return self.comment_set.all().count()

    # def posts_count(self):
    #     return self.comment_set.all().count()

    


class Comment(models.Model):

    body = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
