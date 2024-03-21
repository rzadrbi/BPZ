from django.urls import path
from rest_framework.routers import DefaultRouter

from Recipe import views

app_name = 'Recipe'

urlpatterns = [
    path('showlist', views.RecipeListView.as_view(), name='recipe_list')
]

router = DefaultRouter()
router.register(r'recipe/list', views.RecipeDetailView, basename='RecipeDetailView')
urlpatterns += router.urls
