from rest_framework import serializers
from comment.models import Comment
from base.serializers import UserSerializer   

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    content = serializers.CharField(max_length=180)

    class Meta:
        model = Comment
        fields = '__all__'