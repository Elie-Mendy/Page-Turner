from rest_framework import serializers
from comment.models import Comment
from base.serializers import UserSerializer 
from base.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    user_fullname = serializers.SerializerMethodField(read_only=True)
    content = serializers.CharField(max_length=180)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_user_fullname(self, obj):
        return f"{obj.user.first_name}"