# -*- coding: utf-8 -*-

from source.API.settings import Settings

settings = Settings()

settings.ingredient_col.delete_all()
settings.ingredient_category_col.delete_all()
settings.method_col.delete_all()
settings.method_category_col.delete_all()
settings.recipe_col.delete_all()
settings.recipe_category_col.delete_all()

