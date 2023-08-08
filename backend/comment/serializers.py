from rest_framework import serializers
from comment.models import Comment
from base.serializers import UserSerializer 
from base.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    content = serializers.CharField(max_length=180)

    class Meta:
        model = Comment
        fields = '__all__'