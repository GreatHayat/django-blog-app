from django import template
register = template.Library()
from ..models import Post, Reply

def count_published(posts):
    return posts.filter(published=True).count()

def count_pending(posts):
    return posts.filter(published=False).count()

def count_category(category_name):
    return Post.objects.filter(category__name=category_name).count()

def replies_to_comment(comment):
    return Reply.objects.filter(comment__id=comment)

register.filter("published", count_published)
register.filter("pending", count_pending)
register.filter("post_count", count_category)
register.filter("related_replies", replies_to_comment)
