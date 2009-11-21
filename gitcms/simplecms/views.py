from .models import Article, Category
from django.shortcuts import get_object_or_404, render_to_response

def bycategory(request, category):
    category =get_object_or_404(Category, slug=category)
    articles = Article.objects.filter(categories=category)
    return render_to_response(
                'simplecms/list.html',
                {
                    'pagetitle' : ('Articles in category %s' % category.name),
                    'articles' : articles,
                })

def article(request, url):
    article = get_object_or_404(Article, url=url)
    return render_to_response(
                'simplecms/article.html',
                {
                    'article' : article,
                })
