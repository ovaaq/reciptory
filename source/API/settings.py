import os

from dotenv import load_dotenv

from source.API.collections.ingredient import IngredientCollection
from source.API.collections.ingredient_category import IngredientCategoryCollection
from source.API.collections.method import MethodCollection
from source.API.collections.method_category import MethodCategoryCollection
from source.API.collections.recipe import RecipeCollection
from source.API.collections.recipe_category import RecipeCategoryCollection
from source.API.connection import Connection


class Settings:

    def __init__(self):
        load_dotenv()
        self.mongo_url = os.getenv("MONGO")
        self.connection = Connection(self.mongo_url)

        self.ingredient_col = IngredientCollection(self.connection, "ingredient")
        self.ingredient_category_col = IngredientCategoryCollection(self.connection, "ingredient_category")
        self.recipe_col = RecipeCollection(self.connection, "recipe")
        self.recipe_category_col = RecipeCategoryCollection(self.connection, "recipe_category")
        self.method_col = MethodCollection(self.connection, "method")
        self.method_category_col = MethodCategoryCollection(self.connection, "method_category")