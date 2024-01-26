from django.shortcuts import render
from .models import Post
from datetime import datetime 

# Create your views here.

def home(request):
    
    return render(request, "post/home.html", {})

def post(request, year=datetime.now().year,):
    post_list = Post.objects.all()
    return render(request, 'post.html', {"post_list":post_list, "year":year,})
