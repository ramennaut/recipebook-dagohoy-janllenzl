from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    context_object_name = 'recipe'
