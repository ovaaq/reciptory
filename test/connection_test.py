# -*- coding: utf-8 -*-

# testing the instance of Connection class
from source.API.settings import Settings

settings = Settings()


test = {
    "name": "shallot",
    "parent_category": {
        "$oid": "5edb9987d678535b93caffe8"
    },
    "child_categories": [
    ]
}

test2 = {
    "name": "root",
    "parent_category": None,
    "child_categories": [
    ]
}
#settings.ingredient_category_col.add(test)
#settings.ingredient_category_col.delete("5eda9e829063a7b05d288778")
#settings.ingredient_category_col.delete_all()

#all = settings.ingredient_category_col.get_all()

settings.ingredient_category_col.delete("5edb640fd6b3cf1a3978c8a0")