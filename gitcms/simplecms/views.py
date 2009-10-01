from .models import Article, Category
from django.shortcuts import get_object_or_404, render_to_response

def article(request, url):
    article = get_object_or_404(Article, url=url)
    return render_to_response(
                'simplecms/article.html',
                {
                    'article' : article,
                })
