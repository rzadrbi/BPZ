from django.urls import path
from Recipe import views

app_name = 'Recipe'

urlpatterns = [
    path('showlist', views.RecipeListView.as_view(), name='recipe_list'),
    path('showlistdirections', views.DirectionView.as_view(), name='direction_list'),
    path('randomrecipe', views.RandomRecipeView.as_view(), name='random_recipe'),
]

