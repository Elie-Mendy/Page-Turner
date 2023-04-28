from blog.models import BlogPost

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.serializers import BlogPostSerializer

@api_view(['GET'])
def getPosts(request):
    posts = BlogPost.objects.all().order_by("id")
    serializer = BlogPostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request, pk):
    post = BlogPost.objects.get(id=pk)
    serializer = BlogPostSerializer(post, many=False)
    return Response(serializer.data)
