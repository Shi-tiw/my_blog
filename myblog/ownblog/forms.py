from django.db import models
from django.forms import fields, widgets
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('title', 'desc', 'author', 'content', 'header_img')

        widgets ={
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'This area is for Title'}),
            'desc': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'This area is for Short Description'}),
            'author': forms.TextInput(attrs= {'class': 'form-control', 'value':'', 'id':'shivam', 'type':'hidden'}),
            'content': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'This area is for Content'}),
        }