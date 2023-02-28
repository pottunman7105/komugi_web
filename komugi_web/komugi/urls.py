from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:page_id>/',views.page,name='page'),
    path('article/',views.article,name='article'),
    path('article/<int:article_id>/',views.article,name = 'article'),
]