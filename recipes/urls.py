from django.urls import path

from recipes.views import (
    DeletedMessage,
    IngredientCreate,
    RecipeCreate,
    RecipeDelete,
    RecipeDetail,
    RecipeIngredientCreate,
    RecipeList,
    RecipeUpdate,
)

urlpatterns = [
    path("recipe/list/", RecipeList.as_view(), name="recipes-recipe-list"),
    path("recipe/<int:pk>/", RecipeDetail.as_view(), name="recipes-recipe-detail"),
    path(
        "recipe/ingredient-create/",
        IngredientCreate.as_view(),
        name="recipes-recipe-ingredient-create",
    ),
    path("recipe/recipe-create/", RecipeCreate.as_view(), name="recipes-recipe-create"),
    path(
        "recipe/update/<int:pk>/", RecipeUpdate.as_view(), name="recipes-recipe-update"
    ),
    path(
        "recipe/deleted-message/",
        DeletedMessage.as_view(),
        name="recipes-deleted-message",
    ),
    path(
        "recipe/delete/<int:pk>/", RecipeDelete.as_view(), name="recipes-recipe-delete"
    ),
    path(
        "recipe/ingredient/create/<int:pk>/",
        RecipeIngredientCreate.as_view(),
        name="recipes-recipe-ingredient-create",
    ),
]
