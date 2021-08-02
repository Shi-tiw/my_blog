from .forms import PostForm
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView



# Create your views here.
#def home(request):
#    return render(request , 'home.html', {})

class HomeViews(ListView):
    model = Post
    template_name = 'home.html'

class BlogViews(DetailView):
    model= Post
    template_name = 'blog_details.html'

class AddViews(CreateView):
    model = Post
    form_class= PostForm
    template_name= 'add_blog.html'
    #fields = '__all__'
