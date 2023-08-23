from django.urls import path
from recommandation import views 

urlpatterns = [     
    path('<str:searchValue>', views.trigger_recommandation, name="recommandation"), 
]