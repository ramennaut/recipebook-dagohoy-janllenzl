from django.urls import path
from .views import recipe_list, recipe_1, recipe_2

app_name = 'ledger'

urlpatterns = [
    path('', recipe_list, name='root'),
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/1', recipe_1, name='recipe-1'),
    path('recipe/2', recipe_2, name='recipe-2'),
]