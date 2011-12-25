from gitcms.tagging.models import Tag
from gitcms.pages.models import Article
from django.shortcuts import get_object_or_404, render_to_response

def bytag(request, tag):
    tag = get_object_or_404(Tag, slug=tag)
    articles = Article.objects.filter(tags=tag)
    return render_to_response(
                'pages/list.html',
                {
                    'pagetitle' : ('Articles tagged %s' % tag.name),
                    'articles' : articles,
                })

def article(request, url):
    if len(url) and url[-1] == '/': url = url[:-1]
    article = get_object_or_404(Article, url=url)
    return render_to_response(
                'pages/article.html',
                {
                    'article' : article,
                })
