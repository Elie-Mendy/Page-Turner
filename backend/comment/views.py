import datetime
import pickle
import numpy as np
import tensorflow as tf

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework import serializers
from base.models import User

# import text vectorization layer
from_disk = pickle.load(open("./comment/utils/tv_layer.pkl", "rb"))
vectorizer = tf.keras.layers.TextVectorization.from_config(from_disk['config'])

# vectorizer adaptation with some dummy data (BUG in Keras)
vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
vectorizer.set_weights(from_disk['weights'])

# model instatiation
model = tf.keras.models.load_model('./comment/utils/newModel.h5')




class CommentView(APIView):

    def get(self, request, isbn=None):
        if(isbn is not None):
            try:
                comments = Comment.objects.filter(isbn=isbn, deleted_at__isnull=True)
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

            # comment checking
            input_str = vectorizer(content)
            results = model.predict(np.expand_dims(input_str,0))[0]
            # Convert from float32 to float64 pour la sérialisation JSON
            print("RESULT BEFORE : ", results)
            print("TOXIC BEFORE : ", results[0] > 0.5)

            results = results.astype(np.float64)
            print("RESULT AFTER : ", results)
            print("TOXIC AFTER : ", results[0] > 0.5)


            if results[0] < 0.5:
                serializer.save(user=user_instance)
            
            return JsonResponse(
                {
                    "toxic": results[0],
                    "severe_toxic": results[1],
                    "obscene": results[2],
                    "threat": results[3],
                    "insult": results[4],
                    "identity_hate": results[5],
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, isbn=None):
        print("REQUESRT", request.data)
        id = request.data["id"]
        comment = Comment.objects.get(id=id)
        comment.deleted_at=datetime.datetime.now()
        comment.save()
        return Response(status=status.HTTP_202_ACCEPTED) 

