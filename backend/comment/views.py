import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework import serializers
from base.models import User

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
        user_id = request.data['user']["id"]
        user_instance = User.objects.get(id=user_id)
        isbn = request.data['isbn']  # Obtient l'ISBN à partir des paramètres d'URL
        content = request.data['content']  # Obtient le contenu à partir des données de la requête
        
        serializer = CommentSerializer(data={'user': user_id, 'isbn': isbn, 'content': content})
        if serializer.is_valid():
            print("SERIALISER IS VALID")
            content = serializer.validated_data.get('content')
            if 'gros_mot' in content:
                raise serializers.ValidationError("Attention. Le commentaire contient un gros mot.")
            serializer.save(user=user_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, isbn=None):
        print("REQUESRT", request.data)
        id = request.data["id"]
        comment = Comment.objects.get(id=id)
        comment.deleted_at=datetime.datetime.now()
        comment.save()
        return Response(status=status.HTTP_202_ACCEPTED) 

