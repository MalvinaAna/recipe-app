from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists and details
from .models import Recipe  # to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):         
   model = Recipe                        
   template_name = 'recipes/recipes_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):                       
   model = Recipe                                      
   template_name = 'recipes/recipes_details.html' 