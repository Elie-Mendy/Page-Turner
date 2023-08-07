from rest_framework import serializers
from comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=180)

    class Meta:
        model = Comment
        fields = '__all__'