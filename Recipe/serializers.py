from rest_framework import serializers
from Recipe.models import Recipe, Directions


class DirectionSerializer(serializers.ModelSerializer):
    Recipe = serializers.ReadOnlyField(source='Recipe.name')
    image = serializers.SerializerMethodField()
    class Meta:
        model = Directions
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)


class RecipeSerializer(serializers.ModelSerializer):
    directions = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('name', 'description', 'image', 'cook_time', 'directions')

    def get_directions(self, obj):
        serializer = DirectionSerializer(instance=obj.directions.all(), many=True,
                                         context={'request': self.context.get('request')})
        return serializer.data

    def get_image(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url)



