from django.urls import path 
from blog.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete
from django.contrib.auth.decorators import login_required

app_name = "posts" #définir un espace de noms -- le nom des urls

urlpatterns = [   
    path('', BlogHome.as_view(), name='home'), 
    path('create', login_required(BlogPostCreate.as_view()), name='create'),     
    path('edit/<str:slug>/', login_required(BlogPostUpdate.as_view()), name='edit'), 
    path('<str:slug>/', BlogPostDetail.as_view(), name='post'),   
    path('delete/<str:slug>/', login_required(BlogPostDelete.as_view()), name='delete'),   
]