from django.urls import path
from myapp.views import index, about, art_num, random_id, random_text

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('article/<int:article_number>/', art_num, name='art_num'),
    path('article/<int:article_number>/<slug:slug_text>', art_num, name='art_numtext'),
    path('random/<int:id>', random_id, name="rand_id"),
    path('random/<slug:text>', random_text, name="rand_text"),


]
