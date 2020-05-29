# -*- coding: utf-8 -*-

from json import loads
from bson.json_util import dumps
from flask_restful import Resource, abort
from source.API.connection import Connection
from source.API import verify
from source.API.collection import Collection

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
        request = {plural_term: collection.get_all()}
        if request.get(plural_term) is None:
            abort(404, status="fail", message="there is no objects in the database")

    else:
        request = {singe_term: collection.get(object_id)}
        if request.get(singe_term) is None:
            abort(404, status="fail", message=(singe_term + " with id '" + object_id + "' could not be found"))

    return loads(dumps({"status": "success", "data": request}))


def general_put():
    pass


def general_delete(collection, singe_term, object_id=None):
    """Deletes a object from the database.
     Returns JSON containing information of process.

    Keyword arguments:
    collection -- Collection instance.
    singe_term -- name of the object
    object_id -- To get specific object from the db
    """
    if object_id is None:
        abort(400, status="fail", message=singe_term + " id is required to delete object")

    else:
        request = {singe_term: collection.delete(object_id)}
        if request is False:
            abort(500, status="fail", message="Internal Server Error")

    return loads(dumps({"status": "success", "data": None}))


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
            """Deletes a ingredient from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_delete(ingredient_col, "ingredient", object_id)

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
            """Deletes a ingredient category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_delete(ingredient_category_col, "ingredient category", object_id)

    class Recipe(Resource):

        def get(self, object_id=None):
            """Generates get response for recipe requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(recipe_col, "recipe", object_id)

        def put(self, object_id=None):
            # edit a specific recipe
            pass

        def delete(self, object_id=None):
            """Deletes a recipe from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_delete(recipe_col, "recipe", object_id)

    class RecipeCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for recipe category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(recipe_category_col, "recipe category", object_id)

        def put(self, object_id=None):
            # edit a specific recipe
            pass

        def delete(self, object_id=None):
            """Deletes a recipe category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_get(recipe_category_col, "recipe category", object_id)

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
            """Deletes a method from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_get(method_col, "method", object_id)

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
            """Deletes a method category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_get(method_category_col, "method category", object_id)
