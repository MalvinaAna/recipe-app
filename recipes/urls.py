from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailView
from .views import RecipeCreateView
from .views import about_me

app_name = 'recipes'

urlpatterns = [
   path('', home),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('about/', about_me, name='about'),
   path('add/', RecipeCreateView.as_view(), name='add')
]