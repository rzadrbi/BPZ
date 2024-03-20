from django.db import models
from django.utils.html import format_html


class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients, blank=True, )
    image = models.ImageField(upload_to='img/recipes/')
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="100px" height="52.25px">')


class Directions(models.Model):
    Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/directions/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="100px" height="52.25px">')


class Nutrition(models.Model):
    Recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.name


class ingredients_amount(models.Model):
    Recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING)
    ingredient = models.OneToOneField(Ingredients, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()

    def __str__(self):
        return self.ingredient.name