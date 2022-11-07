from django.shortcuts import render
from blog.models import Comment, Writer, Article


def home(request):
    return render(request, 'home.html')

def page1(request):
    comment_list = Comment.objects.order_by("-date_comm")[:5]
    return render(request, 'page1.html', {'comment_list': comment_list})

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def page4(request):
    return render(request, 'page4.html')

def page5(request):
    return render(request, 'page5.html')

def page6(request):
    write = Writer.objects.order_by("-last_name")[0]
    comment_list = Comment.objects.filter(article__writer=write).order_by('date_comm')[:2]
    return render(request, 'page6.html', {"comment_list": comment_list})
