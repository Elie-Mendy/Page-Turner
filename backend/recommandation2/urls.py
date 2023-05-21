from django.urls import path
from recommandation2 import views 

urlpatterns = [    
    path('', views.trigger_recommandation2, name="recommandation2"),
    path('<str:user_id>', views.trigger_recommandation2, name="recommandation2-id"), 
]