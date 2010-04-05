from gitcms.simpletagging.models import Tag
from gitcms.blog.models import BlogPost
from django.shortcuts import get_object_or_404, render_to_response

def bytag(request, tag):
    tag = get_object_or_404(Tag, slug=tag)
    posts = BlogPost.objects.filter(tags=tag).order_by('-timestamp')
    return render_to_response(
                'blog/list.html',
                {
                    'title' : 'Posts in %s' % tag,
                    'pagetitle' : 'Latest posts in %s' % tag,
                    'posts' : posts,
                })

def post(request, year, month, slug):
    post = get_object_or_404(BlogPost, year_month_slug=path.join(year, month, slug))
    return render_to_response(
                'blog/post.html',
                {
                    'post' : post,
                })

def mostrecent(request):
    posts = BlogPost.objects.order_by('-timestamp')
    return render_to_response(
                'blog/list.html',
                {
                    'title' : 'New posts',
                    'pagetitle' : 'Latest posts',
                    'posts' : posts,
                })
