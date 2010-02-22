from gitcms.simpletagging.models import Tag
from gitcms.simplecms.models import Article
from django.shortcuts import get_object_or_404, render_to_response

def bytag(request, tag):
    tag = get_object_or_404(Tag, slug=tag)
    articles = Article.objects.filter(tags=tag)
    return render_to_response(
                'simplecms/list.html',
                {
                    'pagetitle' : ('Articles tagged %s' % tag.name),
                    'articles' : articles,
                })

def article(request, url):
    article = get_object_or_404(Article, url=url)
    return render_to_response(
                'simplecms/article.html',
                {
                    'article' : article,
                })
