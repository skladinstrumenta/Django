"""homework1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# import to exercise2
# from myapp.views import main, url_articles, url_articles_archive, url_users

# import to exercise3
from myapp.views import main, user_number, regex, ua_number

# <<<Exercise 2>>>

# urlpatterns = [
#     path('', main),
#     path('articles', url_articles),
#     path('articles/archive', url_articles_archive),
#     path('users', url_users)
# ]

# <<<Exercise 3>>>

urlpatterns = [
    path('', main),
    path('article/', include('myapp.urls')),
    path('users/<int:user_numb>', user_number, name='user_number'),
    re_path(r'^(?P<text>[0-9a-fA-F]{4}-[0-9a-fA-F]{6}$)', regex),
    re_path(r'^(?P<numb>050\d{7}|09[3,5,6,7,8,9]\d{7}|06[3,6,7,8]\d{7}|073\d{7}$)', ua_number),

]

