from django.db import models
from django.utils.html import format_html


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='img/recipes/')
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="100px" height="52.25px">')


class Directions(models.Model):
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='directions')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/directions/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="100px" height="52.25px">')


class Nutrition_amount(models.Model):
    Recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    nutrition = models.ManyToManyField(Nutrition,)
    amount = models.IntegerField()

    def __str__(self):
        return self.Recipe.name


class ingredients_amount(models.Model):
    Recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    ingredient = models.ManyToManyField(Ingredients,)
    amount = models.IntegerField()

    def __str__(self):
        return self.Recipe.name







