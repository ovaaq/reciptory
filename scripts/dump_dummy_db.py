# -*- coding: utf-8 -*-

from source.API.settings import Settings

# RUN THIS SCRIPT TO CLEAR THE DATABASE AND GENERATE DUMMY VALUES FOR TESTING

settings = Settings()

settings.clear_database()

settings.ingredient_category_col.dump("ingredient_category.json")