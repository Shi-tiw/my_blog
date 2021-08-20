from django.forms import models
from .forms import PostForm
from .models import Post
from . import forms
from django.shortcuts import render, redirect




# Create your views here.
#def home(request):
#    return render(request , 'home.html', {})

def HomeViews(request):
    posts= Post.objects.all()
    context={
        'Post_list': posts,
    }
    return render(request, "home.html", context)

def BlogViews(request, pk):
    posts = Post.objects.get(pk=pk)
    context ={
        'post': posts,
    }
    return render(request, "blog_details.html", context)

def AddViews(request):
    if request.method=='POST':
        form= forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog= form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form= forms.PostForm()
    return render(request, 'add_blog.html',{'form':form})