from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Article


class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'

    def get_quaryset(self):
        return Article.objects.order_by('created_at')[:5]


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'

index = IndexView.as_view()
article = ArticleView.as_view()