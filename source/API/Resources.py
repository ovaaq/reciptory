# -*- coding: utf-8 -*-

from flask_restful import Resource
from source.API.Connection import Connection
from source.API import Verify
from source.API.Collection import Collection

class Resources:
    
    class Ingredient(Resource):
        def get(self):
            # get all ingredients
            pass

        def put(self):
            # put a new ingredient
            pass

    class IngredientId(Resource):

        def get(self, id):
            # get a specific ingredient
            pass

        def put(self, id):
            # edit a specific ingredient
            pass

        def delete(self, id):
            # delete a specific ingredient
            pass

    class IngredientCategory(Resource):

        def get(self):
            # get all ingredient categories
            pass

        def put(self):
            # add a new ingredient category
            pass

    class IngredientCategoryId(Resource):

        def get(self, id):
            # get a specific ingredient category
            pass

        def put(self, id):
            # edit a specific ingredient category
            pass

        def delete(self, id):
            # delete a specific ingredient category
            pass

    class Recipe(Resource):

        def get(self):
            # get all recipes
            pass

        def put(self):
            # put a new recipe
            pass

    class RecipeId(Resource):

        def get(self, id):
            # get a specific recipe
            pass

        def put(self, id):
            # edit a specific recipe
            pass

        def delete(self, id):
            # delete a specific recipe
            pass

    class RecipeCategory(Resource):

        def get(self):
            # get all recipe categories
            pass

        def put(self):
            # put a new recipe category
            pass

    class RecipeCategoryId(Resource):

        def get(self, id):
            # get a specific recipe category
            pass

        def put(self, id):
            # edit a specific recipe
            pass

        def delete(self, id):
            # delete a specific recipe category
            pass

    class Method(Resource):

        def get(self):
            # get all methods
            pass

        def put(self):
            # put a new method
            pass

    class MethodId(Resource):

        def get(self, id):
            # get a specific method
            pass

        def put(self, id):
            # edit a specific method
            pass

        def delete(self, id):
            # delete a specific method
            pass

    class MethodCategory(Resource):

        def get(self):
            # get all method categories
            pass

        def put(self):
            # put a new method category
            pass

    class MethodCategoryId(Resource):

        def get(self, id):
            # get a specific method category
            pass

        def put(self, id):
            # edit a specific method category
            pass

        def delete(self, id):
            # delete a specific method category
            pass
