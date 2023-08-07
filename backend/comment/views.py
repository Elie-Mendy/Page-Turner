# from comment.models import Comment
# from rest_framework.generics import ListCreateAPIView
# from rest_framework import serializers
# from comment.serializers import CommentSerializer

# #  test isbn : 9780590353403
# class CommentView(ListCreateAPIView, id=None):
#     if id is not None : 
#         queryset = Comment.objects.get(id=id)
#         serializer_class = CommentSerializer
#     else :
#         queryset = Comment.objects.all()
#         serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         content = serializer.validated_data.get('content')
#         if 'gros_mot' in content:
#             raise serializers.ValidationError("Attention. Le commentaire contient un gros mot.")
#         serializer.save()


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework import serializers

class CommentView(APIView):
    def get(self, request, isbn=None):
        if(isbn is not None):
            try:
                comments = Comment.objects.filter(isbn=isbn)
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
            except Comment.DoesNotExist:
                return Response({"error": "L'isbn n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
        else:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    def post(self, request):
        print("REQUEST ==>", request.data)
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            print("SERIALISER IS VALID")
            content = serializer.validated_data.get('content')
            if 'gros_mot' in content:
                raise serializers.ValidationError("Attention. Le commentaire contient un gros mot.")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

