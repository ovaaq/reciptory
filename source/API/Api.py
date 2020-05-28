# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from source.API.Resources import Resources

app = Flask(__name__)
api = Api(app)

# /api/ingredient
api.add_resource(Resources.Ingredient, '/api/ingredient/', '/api/ingredient/<object_id>')

# /api/ingredient_category
api.add_resource(Resources.IngredientCategory, '/api/ingredient_category', '/api/ingredient_category/<object_id>')

# /api/recipe
api.add_resource(Resources.Recipe, '/api/recipe', '/api/recipe/<object_id>')

# /api/recipe_category
api.add_resource(Resources.RecipeCategory, '/api/recipe_category', '/api/recipe_category/<object_id>')

# /api/method
api.add_resource(Resources.Method, '/api/method', '/api/method/<object_id>')

# /api/method_category
api.add_resource(Resources.MethodCategory, '/api/method_category', '/api/method_category/<object_id>')

if __name__ == '__main__':
    app.run(debug=False)
