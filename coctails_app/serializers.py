from rest_framework import serializers, generics
from .models import Category, Ingredient, Cocktail, CocktailIngredient
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class CocktailIngredientSerializer(serializers.ModelSerializer):

    ingredient = IngredientSerializer(read_only=True)

    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(),
        source="ingredient",
        write_only=True
    )

    class Meta:
        model = CocktailIngredient
        fields = [
            "id",
            "ingredient",
            "ingredient_id",
            "amount"
        ]

class UserSerializer(serializers.ModelSerializer):
    cocktails = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())
    
    class Meta:
        model = User
        fields = ["id", "username", "cocktails"]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    

class CocktailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        allow_null=True,
        required=False
     )

    ingredients = CocktailIngredientSerializer(
        source = "cocktailingredient_set",
        many=True,
        read_only=True
    )

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Cocktail
        fields = "__all__"
        # [
        #     "id",
        #     "name",
        #     "category",
        #     "category_id",
        #     "instructions",
        #     "is_alcoholic",
        #     "ingredients"
        # ]



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer