from django.urls import path
from recommandation2 import views 

urlpatterns = [
    path('<str:user_id>', views.trigger_recommandation2, name="recommandation2"), 
]