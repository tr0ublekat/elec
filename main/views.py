from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'О нашем проекте'})