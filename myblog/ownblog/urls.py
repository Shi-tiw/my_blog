from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeViews, name ="home" ),
    path('blog/<int:pk>',views.BlogViews, name="blog"),
    path('new/',views.AddViews, name="new"),
    
]