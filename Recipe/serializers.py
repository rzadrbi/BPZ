from rest_framework import serializers
from Recipe.models import Recipe, Directions


class DirectionSerializer(serializers.ModelSerializer):
    Recipe = serializers.ReadOnlyField(source='Recipe.name')
    class Meta:
        model = Directions
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    directions = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'image', 'cook_time', 'directions')

    def get_directions(self, obj):
        serializer = DirectionSerializer(instance=obj.directions.all(), many=False)
        return serializer.data
