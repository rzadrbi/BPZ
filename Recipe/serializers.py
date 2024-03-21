from PIL.ImageCms import Direction
from rest_framework import serializers
from Recipe.models import Recipe


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    direction = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_direction(self, obj):
        serializer = DirectionSerializer(data=obj.directions.all(), many=True)
        return serializer
