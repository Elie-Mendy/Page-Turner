from django.urls import path
from blog import views 

urlpatterns = [    
    path('', views.getPosts, name="posts"), 
    path('<str:pk>', views.getPost, name="post"), 
]