from django.contrib import admin
from .models import Category, Post, Profile, Comment, Reply
from django.contrib import messages
from django.core.mail import send_mail
# Register your models here.

def publish_posts(modeladmin, request, queryset):
    queryset.update(published=True)
    messages.info(request, f"Your post has been approved!")
def draft_posts(modeladmin, request, queryset):
    queryset.update(published=False)

publish_posts.short_description = "Published Selected Posts"
draft_posts.short_description = "Draft Selected Posts"
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'published',)
    list_filter = ('published',)
    actions = [publish_posts, draft_posts]
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Reply)
