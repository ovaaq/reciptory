# -*- coding: utf-8 -*-

from json import loads
from bson.json_util import dumps
from flask_restful import Resource, abort
from source.API.Connection import Connection
from source.API import Verify
from source.API.Collection import Collection

con = Connection()

ingredient_col = Collection(con, "ingredient")
ingredient_category_col = Collection(con, "ingredient_category")
recipe_col = Collection(con, "recipe")
recipe_category_col = Collection(con, "recipe_category")
method_col = Collection(con, "method")
method_category_col = Collection(con, "method_category")


def general_get(collection, singe_term, plural_term, object_id=None):
    """Generates get response for all general
    get requests. Returns JSON containing object.

    Keyword arguments:
    singe_term -- name of the object
    plural_term -- plural of the object
    object_id -- optional. To get specific object from the db
    """
    if object_id is None:
        data = {plural_term: collection.get_all()}
        if data is None:
            abort(404, message=(plural_term + " could not be found"))

    else:
        data = {singe_term: collection.get(object_id)}
        if data is None:
            abort(404, message=(plural_term + " could not be found"))

    return loads(dumps({"status": "success", "data": data}))


class Resources:
    class Ingredient(Resource):

        def get(self, object_id=None):
            """Generates get response for ingredient requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(ingredient_col, "ingredient", "ingredients", object_id)

        def put(self, object_id=None):
            # put a new ingredient
            pass

        def delete(self, object_id=None):
            # delete a specific ingredient
            pass

    class IngredientCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for ingredient category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(ingredient_category_col, "ingredient category", "ingredient categories", object_id)

        def put(self, object_id=None):
            # edit a specific ingredient category
            pass

        def delete(self, object_id=None):
            # delete a specific ingredient category
            pass

    class Recipe(Resource):

        def get(self, object_id=None):
            """Generates get response for recipe requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(recipe_col, "recipe", "recipes", object_id)

        def put(self, object_id=None):
            # edit a specific recipe
            pass

        def delete(self, object_id=None):
            # delete a specific recipe
            pass

    class RecipeCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for recipe category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(recipe_category_col, "recipe category", "recipe categories", object_id)

        def put(self, object_id=None):
            # edit a specific recipe
            pass

        def delete(self, object_id=None):
            # delete a specific recipe category
            pass

    class Method(Resource):

        def get(self, object_id=None):
            """Generates get response for method requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(method_col, "method", "methods", object_id)

        def put(self, object_id=None):
            # edit a specific method
            pass

        def delete(self, object_id=None):
            # delete a specific method
            pass

    class MethodCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for method category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(method_category_col, "method category", "method categories", object_id)

        def put(self, object_id=None):
            # edit a specific method category
            pass

        def delete(self, object_id=None):
            # delete a specific method category
            pass
