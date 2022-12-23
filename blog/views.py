from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
# Creating a dummy data


def home_page(request):
    datainfo = {
        'datainfo':Post.objects.all()
    }
    return render(request,'blog/home.html',context=datainfo)

def about_page(request):
    return render(request, 'blog/about.html')