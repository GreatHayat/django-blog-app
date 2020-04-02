from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.utils.html import mark_safe
from markdown import markdown
from .validators import validate_file_size
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    title = models.CharField(max_length=30, blank=False, null=False)
    profile_image = models.ImageField(upload_to="profile_images/", validators=[validate_file_size])
    status = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.user}"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    post_content = models.TextField(blank=False, null=False)
    feature_image = models.ImageField(upload_to="feature_images/", validators=[validate_file_size])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="updated_by")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    def get_post_content_as_markdown(self):
        return mark_safe(markdown(self.post_content, safe_mode='escape'))

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_by")
    comment_msg = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username, self.comment_msg[:50]}"

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reply_user")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reply_comment")
    reply_msg = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment.comment_msg[:50]}"
