from django.urls import path
from Recipe import views

app_name = 'Recipe'

urlpatterns = [
    path('showlist', views.RecipeListView.as_view(), name='recipe_list'),
    path('showlistdirections', views.RecipeDirectionView.as_view(), name='direction_list'),
]

