# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from source.API.Resources import Resources

app = Flask(__name__)
api = Api(app)

api.add_resource(Resources.Ingredient, '/api/ingredient/')
api.add_resource(Resources.IngredientId, '/api/ingredient/<id>')
api.add_resource(Resources.IngredientCategory, '/api/ingredient_category')
api.add_resource(Resources.IngredientCategoryId, '/api/ingredient_category/<id>')

api.add_resource(Resources.Recipe, '/api/recipe')
api.add_resource(Resources.RecipeId, '/api/recipe/<id>')
api.add_resource(Resources.RecipeCategory, '/api/recipe_category')
api.add_resource(Resources.RecipeCategoryId, '/api/recipe_category/<id>')

api.add_resource(Resources.Method, '/api/method')
api.add_resource(Resources.MethodId, '/api/method/<id>')
api.add_resource(Resources.MethodCategory, '/api/method_category')
api.add_resource(Resources.MethodCategoryId, '/api/method_category/<id>')

if __name__ == '__main__':
    app.run(debug=True)
