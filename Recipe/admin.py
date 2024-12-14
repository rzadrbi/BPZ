from django.contrib import admin
from Recipe.models import *


class DirInline(admin.TabularInline):
    model = Directions
    fields = ('title', 'body', 'image')


class NutInline(admin.TabularInline):
    model = Nutrition_amount
    fields = ('nutrition', 'amount',)


class IngInline(admin.TabularInline):
    model = ingredients_amount
    fields = ('ingredient', 'amount',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cook_time',)
    search_fields = ('ingredients', 'name', 'cook_time')
    list_filter = ('cook_time',)
    inlines = [DirInline, NutInline, IngInline]


@admin.register(Ingredients)
class ModelNameAdmin(admin.ModelAdmin):
    list_filter = ('name',)


admin.site.register(Nutrition)

