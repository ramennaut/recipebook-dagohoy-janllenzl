from django.urls import path
from .views import recipe_data

app_name = 'ledger'

urlpatterns = [
    path('', recipe_data, name='recipe-data')
]