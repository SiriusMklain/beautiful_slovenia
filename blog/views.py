from django.shortcuts import render
from .models import Article


def blog(request):
    articles = Article.objects.filter(status_article="active")
    context = {"articles": articles}
    return render(request, 'blog/index.html', context=context)
