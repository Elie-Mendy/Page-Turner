from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isbn = models.IntegerField(blank=False)
    content = models.CharField(max_length=180)
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)

def __str__(self):
    return f"{self.user.username} : {self.content[:35]}... {self.created_at}"
