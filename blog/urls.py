from django.urls import path
from blog.views import home, page1, page2, page3, page4, page5, page6

urlpatterns = [
    path('', home, name='home'),
    path('1', page1, name="page1"),
    path('2', page2, name="page2"),
    path('3', page3, name="page3"),
    path('4', page4, name="page4"),
    path('5', page5, name="page5"),
    path('6', page6, name="page6"),

]