from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200)
    shared_post = models.ForeignKey('self', on_delete=models.CASCADE, related_name="shared_id", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamers_posts")
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamers_shared", blank=True, null=True)
    updated_on = models.DateTimeField(default=timezone.now)
    shared_content = models.TextField(blank=True, null=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(default=timezone.now)
    shared_on = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name="gamers_likes", blank=True)

    class Meta:
        ordering = ["-created_on", "-shared_on"]

    def __str__(self):
        return self.title

    def num_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gamers_comments", default=None)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} made by {self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, symmetrical=False, related_name='followers', blank=True)

    def num_of_followers(self):
        return self.following.count
