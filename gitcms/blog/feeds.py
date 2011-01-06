from django.contrib.syndication.views import Feed
from gitcms.blog.models import BlogPost

class LatestFeed(Feed):
    title = 'pythonvision.org blog feed'
    link = '/blog/feed'
    description = 'Updates on pythonvision.org and items of interest for computer vision in Python'

    def items(self):
        return BlogPost.objects.order_by('-timestamp')[:20]

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        return post.content

    def item_link(self, post):
        return '/blog/' + post.year_month_slug
