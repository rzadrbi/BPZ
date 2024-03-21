from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from Recipe.models import Recipe, Directions
from Recipe.serializers import RecipeSerializer, DirectionSerializer
from .pagination import StandardResultsSetPagination


class RecipeListView(APIView):
    serializer_class = RecipeSerializer

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecipeDirectionView(APIView, StandardResultsSetPagination):
    serializer_class = DirectionSerializer

    def get(self, request):
        instance = Directions.objects.all()
        paginated_instance = self.paginate_queryset(instance, request)
        serializer = DirectionSerializer(instance=paginated_instance, many=True, context={'request': request})
        return self.get_paginated_response(data=serializer.data)
