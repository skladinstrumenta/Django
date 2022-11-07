from django.urls import path
from library.views import home3_4

urlpatterns = [
    path('', home3_4, name='index'),
]