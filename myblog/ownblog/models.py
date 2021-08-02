from datetime import datetime, date
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=255)
    header_img=models.ImageField(null= False, blank= False, upload_to="images/")
    desc = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content= models.TextField()
    date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')