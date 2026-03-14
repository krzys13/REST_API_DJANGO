from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    instructions = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='CocktailIngredient'
    )
    is_alcoholic = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Cocktails"
    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.CharField(max_length=100, help_text='np. 50 ml, 2 plasterki, 1/2 szklanki')


    def __str__(self):
        return f"{self.ingredient.name} dla {self.cocktail.name}: {self.amount}"
