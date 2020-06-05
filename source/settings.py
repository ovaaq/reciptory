from dotenv import load_dotenv
import os

from source.API.collection import Collection
from source.API.connection import Connection


class Settings:

    def __init__(self):
        load_dotenv()
        self.mongo_url = os.getenv("MONGO")
        self.connection = Connection(self.mongo_url)

        self.ingredient_col = Collection(self.mongo_url, "ingredient")
        self.ingredient_category_col = Collection(self.mongo_url, "ingredient_category")
        self.recipe_col = Collection(self.mongo_url, "recipe")
        self.recipe_category_col = Collection(self.mongo_url, "recipe_category")
        self.method_col = Collection(self.mongo_url, "method")
        self.method_category_col = Collection(self.mongo_url, "method_category")