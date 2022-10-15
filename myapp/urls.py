from django.urls import path
from myapp.views import article_number, article_number_arc, art_numb_slug, user_number

urlpatterns = [
    path('<int:article_number>', article_number, name='article_number'),
    path('<int:article_number>/archive', article_number_arc, name='article_number_arc'),
    path('<int:article_number>/<slug:slug_text>', art_numb_slug, name='art_numb_slug')
]