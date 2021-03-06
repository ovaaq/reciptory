# -*- coding: utf-8 -*-

from json import loads
from bson.json_util import dumps
from flask import request
from flask_restful import Resource, abort
from source.API import verify
from source.settings import Settings

settings = Settings()


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
        if data.get(plural_term) is None:
            abort(404, status="fail", message="there is no objects in the database")

    else:
        data = {singe_term: collection.get(object_id)}
        if data.get(singe_term) is None:
            abort(404, status="fail", message=(singe_term + " with id '" + object_id + "' could not be found"))

    return loads(dumps({"status": "success", "data": data}))


def general_put(collection, content, verifier, object_id=None):
    """Add or edit an object from the database.
     Returns JSON containing information of process.

    Keyword arguments:
    collection -- Collection instance
    content -- json document wish to be added or editer
    verifier -- Function that verifies sent data
    object_id -- optional. To edit specific object from the db
    """
    tmp = verifier(content)
    if len(tmp) < 1:
        if object_id is None:
            is_success = collection.add(content)
        else:
            is_success = collection.edit(object_id, content)
        if is_success:
            return loads(dumps({"status": "success", "data": content}))
        # palauta mieluummin tietokannasta haettu data eli varmista samuus
        else:
            abort(500, status="error", message="Internal Server Error")
    else:
        abort(400, status="fail", errors=tmp)


def general_delete(collection, singe_term, object_id=None):
    """Deletes an object from the database.
     Returns JSON containing information of process.

    Keyword arguments:
    collection -- Collection instance
    singe_term -- name of the object
    object_id -- To get specific object from the db
    """
    if object_id is None:
        abort(400, status="fail", message=singe_term + " id is required to delete object")

    else:
        transaction = {singe_term: collection.delete(object_id)}
        if transaction is False:
            abort(500, status="error", message="Internal Server Error")

    return loads(dumps({"status": "success", "data": None}))


class Resources:
    class Ingredient(Resource):

        def get(self, object_id=None):
            """Generates get response for ingredient requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(settings.ingredient_col, "ingredient", "ingredients", object_id)

        def put(self, object_id=None):
            """Add or edit an ingredient from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- optional. To edit specific object from the db
            """
            content = request.json
            return general_put(settings.ingredient_col, content, verify.ingredient, object_id)

        def delete(self, object_id=None):
            """Deletes a ingredient from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_delete(settings.ingredient_col, "ingredient", object_id)

    class IngredientCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for ingredient category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(settings.ingredient_category_col, "ingredient category", "ingredient categories", object_id)

        def put(self, object_id=None):
            """Add or edit an ingredient category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- optional. To edit specific object from the db
            """
            content = request.json
            return general_put(settings.ingredient_category_col, content, verify.ingredient_category, object_id)

        def delete(self, object_id=None):
            """Deletes a ingredient category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_delete(settings.ingredient_category_col, "ingredient category", object_id)

    class Recipe(Resource):

        def get(self, object_id=None):
            """Generates get response for recipe requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(settings.recipe_col, "recipe", object_id)

        def put(self, object_id=None):
            """Add or edit an recipe from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- optional. To edit specific object from the db
            """
            content = request.json
            return general_put(settings.recipe_col, content, verify.recipe, object_id)

        def delete(self, object_id=None):
            """Deletes a recipe from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_delete(settings.recipe_col, "recipe", object_id)

    class RecipeCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for recipe category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(settings.recipe_category_col, "recipe category", object_id)

        def put(self, object_id=None):
            """Add or edit an recipe category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- optional. To edit specific object from the db
            """
            content = request.json
            return general_put(settings.recipe_category_col, content, verify.recipe_category, object_id)

        def delete(self, object_id=None):
            """Deletes a recipe category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_get(settings.recipe_category_col, "recipe category", object_id)

    class Method(Resource):

        def get(self, object_id=None):
            """Generates get response for method requests.
            Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(settings.method_col, "method", "methods", object_id)

        def put(self, object_id=None):
            """Add or edit an method from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- optional. To edit specific object from the db
            """
            content = request.json
            return general_put(settings.method_col, content, verify.method, object_id)

        def delete(self, object_id=None):
            """Deletes a method from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_get(settings.method_col, "method", object_id)

    class MethodCategory(Resource):

        def get(self, object_id=None):
            """Generates get response for method category
             requests. Returns JSON containing object.

            Keyword arguments:
            object_id -- optional. To get specific object from the db
            """
            return general_get(settings.method_category_col, "method category", "method categories", object_id)

        def put(self, object_id=None):
            """Add or edit an method category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- optional. To edit specific object from the db
            """
            content = request.json
            return general_put(settings.method_category_col, content, verify.method_category, object_id)

        def delete(self, object_id=None):
            """Deletes a method category from the database.
             Returns JSON containing information of process.

            Keyword arguments:
            object_id -- To get specific object from the db
            """
            return general_get(settings.method_category_col, "method category", object_id)
