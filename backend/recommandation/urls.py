from django.urls import path
from recommandation import views 

urlpatterns = [    
    path('', views.trigger_recommandation, name="recommandation"), 
]