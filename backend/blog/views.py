from django.shortcuts import render
from django.views.generic import ListView # permet de récupérer toutes les données du modèle 
from django.views.generic import CreateView # permet de créer une vue
from django.views.generic import UpdateView # permet de créer une vue
from django.views.generic import DetailView # permet de créer une vue
from django.views.generic import DeleteView # permet de créer une vue
from blog.models import BlogPost
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class BlogHome(ListView) :
  model = BlogPost      # récupère tous les articles du blog crées dans notre modèle BlogHome
  context_object_name = "posts" # spécifie un nom pour la var à utiliser à l'intérieur du fichier du template
  template_name = "posts/blogpost_list.html"

  # ajouter des modifications dans notre template
  def get_queryset(self):
    queryset = super().get_queryset()
    if self.request.user.is_authenticated:
      return queryset
    return queryset.filter(published=True)
  
  
@method_decorator(login_required, name="dispatch")
class BlogPostCreate(CreateView) :
  model = BlogPost      # récupère tous les articles du blog crées dans notre modèle BlogHome
  template_name = "posts/blogpost_create.html"
  fields = ['title', 'content',]


@method_decorator(login_required, name="dispatch")
class BlogPostUpdate(UpdateView) :
  model = BlogPost      # récupère tous les articles du blog crées dans notre modèle BlogHome
  context_object_name = "post" # éviter d'utiliser la var de base object
  template_name = "posts/blogpost_edit.html"
  fields = ['title', 'content', 'published']


class BlogPostDetail(DetailView) :
  model = BlogPost      # récupère tous les articles du blog crées dans notre modèle BlogHome
  context_object_name = "post" # éviter d'utiliser la var de base object
  template_name = "posts/blogpost_detail.html"


@method_decorator(login_required, name="dispatch")
class BlogPostDelete(DeleteView) :
  model = BlogPost      # récupère tous les articles du blog crées dans notre modèle BlogHome
  context_object_name = "post" # éviter d'utiliser la var de base object
  success_url = reverse_lazy("posts:home")
  template_name = "posts/blogpost_confirm_delete.html"
