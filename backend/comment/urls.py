from django.urls import path
from comment.views import CommentView

urlpatterns = [    
    path('', CommentView.as_view(), name="comments"), 
    path('<int:isbn>', CommentView.as_view(), name="comments-isbn"), 
]