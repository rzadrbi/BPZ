from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from Recipe.models import Recipe
from Recipe.serializers import RecipeSerializer


class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(instance=recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecipeDetailView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = []
