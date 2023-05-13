from django.urls import path
from recommandation import views 

urlpatterns = [    
    path('', views.trigger_recommandation, name="recommandation"), 
    path('<str:book_title>', views.trigger_recommandation, name="recommandation"), 
]