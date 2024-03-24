from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from Recipe.models import Recipe, Directions
from Recipe.serializers import RecipeSerializer, DirectionSerializer
import random


class RecipeListView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DirectionView(APIView):

    def get(self, request):
        queryset = Directions.objects.all()
        serializer = DirectionSerializer(instance=queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class RandomRecipeView(APIView):
    def get(self, request, *args, **kwargs):
        count = Recipe.objects.count()  # Get the total count of recipes
        if count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        random_idx = random.randint(0, count - 1)  # Generate a random index
        recipe = Recipe.objects.all()[random_idx]  # Retrieve a random object
        serializer = RecipeSerializer(recipe, context={'request': request})
        return Response(serializer.data)


class RecipeByTimeView(APIView):
    def get(self, request, max_time=1000, min_time=0):
        queryterms = Q(cook_time__gte=min_time) & Q(cook_time__lte=max_time)
        recipes = Recipe.objects.filter(queryterms)
        serializer = RecipeSerializer(instance=recipes, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)




