import os

from dotenv import load_dotenv
from pymongo.collection import Collection

from source.API.collections.ingredient_collection import IngredientCollection
from source.API.collections.ingredient_category_collection import IngredientCategoryCollection
from source.API.collections.method_collection import MethodCollection
from source.API.collections.method_category_collection import MethodCategoryCollection
from source.API.collections.recipe_collection import RecipeCollection
from source.API.collections.recipe_category_collection import RecipeCategoryCollection
from source.API.connection import Connection


class Settings:

    def __init__(self):
        """
        Constructor
        """
        load_dotenv()
        self.mongo_url = os.getenv("MONGO")
        self.connection = Connection(self.mongo_url)

        self.ingredient_col: IngredientCollection = IngredientCollection(self.connection, "ingredient")
        self.ingredient_category_col: IngredientCategoryCollection = IngredientCategoryCollection(self.connection, "ingredient_category")
        self.recipe_col: RecipeCollection = RecipeCollection(self.connection, "recipe")
        self.recipe_category_col: RecipeCategoryCollection = RecipeCategoryCollection(self.connection, "recipe_category")
        self.method_col: MethodCollection = MethodCollection(self.connection, "method")
        self.method_category_col: MethodCategoryCollection = MethodCategoryCollection(self.connection, "method_category")

    def clear_database(self) -> None:
        """
        Drops all the collections from the database.

        :return: None
        """
        self.ingredient_col.delete_all()
        self.ingredient_category_col.delete_all()
        self.method_col.delete_all()
        self.method_category_col.delete_all()
        self.recipe_col.delete_all()
        self.recipe_category_col.delete_all()
