from django.db import models
from model_utils import Choices

UNITS = Choices(
    ("unit", "Unit"),
    ("g", "Grams"),
    ("kg", "Kilograms"),
    ("ml", "Milliliters"),
    ("l", "Liters"),
    ("tsp", "Teaspoon"),
    ("tbsp", "Tablespoon"),
    ("cup", "Cup"),
    ("pint", "Pint"),
    ("quart", "Quart"),
    ("gallon", "Gallon"),
    ("oz", "Ounce"),
    ("lb", "Pound"),
)

WEIGHT_UNITS = {
    "g": 1,
    "kg": 1000,
    "oz": 28.3495,
    "lb": 453.592,
}
VOLUME_UNITS = {
    "ml": 1,
    "l": 1000,
    "tsp": 5,
    "tbsp": 15,
    "cup": 240,
    "pint": 473.176,
    "quart": 946.353,
    "gallon": 3785.41,
}


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    address = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=6, choices=UNITS, default=UNITS.g)
    ingredients = models.ManyToManyField(
        'self',
        through='RecipeIngredient',
        symmetrical=False,
        related_name='used_in',
    )

    def __str__(self):
        return (f"{self.title} - "
                f"{self.quantity} {self.unit} - "
                f"{self.get_price()} - "
                f"{self.get_unit_price()}")

    def get_price(self):
        return f"€{self.price / 100:.2f}"

    def get_unit_type(self):
        if self.unit in WEIGHT_UNITS:
            return "weight"
        elif self.unit in VOLUME_UNITS:
            return "volume"
        else:
            return "unit"

    def get_unit(self):
        if self.unit in WEIGHT_UNITS:
            return "g"
        elif self.unit in VOLUME_UNITS:
            return "ml"
        else:
            return "unit"

    def get_quantity(self):
        multiplier = WEIGHT_UNITS.get(self.unit, VOLUME_UNITS.get(self.unit, 1))
        return self.quantity * multiplier

    def get_unit_price(self):
        return f"€{self.price / 100 / self.quantity:.2f} / {self.unit}"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
    )
    ingredient = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_in',
    )
    quantity = models.IntegerField()
    unit = models.CharField(max_length=6, choices=UNITS, default=UNITS.g)
