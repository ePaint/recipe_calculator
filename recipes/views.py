from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView, DeleteView, TemplateView,
)

from recipes.models import Recipe, RecipeIngredient


class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"


class RecipeDetail(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"


class IngredientCreate(CreateView):
    model = Recipe
    template_name = "recipes/ingredient_form.html"
    success_url = "/recipes/recipe/list/"
    fields = ["title", "price", "quantity", "unit"]


class RecipeCreate(CreateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    fields = ["title", "quantity", "unit"]

    def get_success_url(self):
        return f"/recipes/recipe/ingredient/create/{self.object.pk}/"


class RecipeUpdate(UpdateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    fields = "__all__"


class DeletedMessage(TemplateView):
    template_name = "recipes/partials/deleted_message.html"


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = "/recipes/recipe/deleted-message/"
    template_name = "/layout/fragment.html"


class RecipeIngredientCreate(CreateView):
    model = RecipeIngredient
    template_name = "recipes/recipe_ingredient_form.html"
    success_url = "/recipes/ingredient/create/"
    fields = ["recipe", "ingredient", "quantity", "unit"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = Recipe.objects.get(pk=self.kwargs["pk"])
        return context

    # prefill form so 'recipe' is preselected with pk object, make recipe not editable
    def get_initial(self):
        return {"recipe": self.kwargs["pk"]}

    # edit form so recipe field is not editable
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["recipe"].widget.attrs["readonly"] = True
        return form

