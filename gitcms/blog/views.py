from gitcms.tagging.models import Tag
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from gitcms.blog.models import BlogPost


def bytag(request, tag):
    tag = get_object_or_404(Tag, slug=tag)
    posts = BlogPost.objects.exclude(status='draft').filter(tags=tag).order_by('-timestamp')
    return render_to_response(
                'blog/tag_list.html',
                RequestContext(request, {
                    'tag' : tag,
                    'posts' : posts,
                }))

def post(request, year, month, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render_to_response(
                'blog/post.html',
                RequestContext(request, {
                    'post' : post,
                }))

def mostrecent(request):
    posts = BlogPost.objects.exclude(status='draft').order_by('-timestamp')
    return render_to_response(
                'blog/list.html',
                RequestContext(request, {
                    'title' : 'New posts',
                    'pagetitle' : 'Latest posts',
                    'posts' : posts,
                }))
