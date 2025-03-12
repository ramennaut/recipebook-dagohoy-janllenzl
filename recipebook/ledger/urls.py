from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

app_name = "ledger"
