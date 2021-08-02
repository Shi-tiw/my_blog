
from django.urls import path
#from . import views
from .views import HomeViews, BlogViews,AddViews


urlpatterns = [
    path('', HomeViews.as_view() ,name ="home" ),
    path('blog/<int:pk>',BlogViews.as_view(), name="blog"),
    path('new/',AddViews.as_view(), name="new"),
    
]