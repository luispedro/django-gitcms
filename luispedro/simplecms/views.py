from .models import Article, Category
from django.shortcuts import get_object_or_404, render_to_response

def article(request, url):
    art = get_object_or_404(Article, url=url)
    return render_to_response(
                'article/article.html',
                {
                    'article' : article,
                })
