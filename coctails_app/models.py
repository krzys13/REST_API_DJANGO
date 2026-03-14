from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_alcoholic = models.BooleanField(default=False)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToOneRel(
        Category,
        on_delete=models.CASCADE
    )
    instructions = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='CocktailIngredient',
        related_name='cocktails'
    )

    class Meta:
        verbose_name = "koktajl"
        verbose_name_plural = "koktajle"

    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.CASCADE,
        related_name='cocktail_ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient_cocktails'
    )
    amount = models.CharField(max_length=100, help_text='np. 50 ml, 2 plasterki, 1/2 szklanki')

    class Meta:
        verbose_name = "składnik koktajlu"
        verbose_name_plural = "składniki koktajli"
        unique_together = ('cocktail', 'ingredient')

    def __str__(self):
        return f"{self.ingredient.name} dla {self.cocktail.name}: {self.amount}"
