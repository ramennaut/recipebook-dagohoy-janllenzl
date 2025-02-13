from django.urls import path
from .views import index
from .views import recipes_list
from .views import recipe_1
from .views import recipe_2

urlpatterns = [
    path('', index, name='index'),
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/1', recipe_1, name='recipe_1'),
    path('recipe/2', recipe_2, name='recipe_2'),
]

app_name = "ledger"