from django.contrib.syndication.views import Feed
from gitcms.blog.models import BlogPost
from django.conf import settings


class LatestFeed(Feed):
    title = getattr(settings, 'GITCMS_BLOG_FEED_NAME', 'Blog RSS channel')
    link = '/rss/'
    description = 'Updates on blog and items of interesting content'

    def items(self):
        try:
            limit = settings.LIMIT_RSS_ITEMS
        except:
            limit = 20
        return BlogPost.objects.order_by('-timestamp')[:limit]

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        return post.content

    def item_link(self, post):
        return post.get_absolute_url()
