from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet,
    IngredientViewSet,
    CocktailViewSet,
    CocktailIngredientViewSet,
    UserList,
    UserDetail
    
)
from django.urls import path, include


router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("ingredients", IngredientViewSet)
router.register("cocktails", CocktailViewSet)
router.register("cocktail-ingredients", CocktailIngredientViewSet)

urlpatterns = router.urls + [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    ]