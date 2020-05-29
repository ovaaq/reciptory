# -*- coding: utf-8 -*-

# testing the instance of Connection class
from source.API import verify

ingredient_document = {
    "name": "kana",
    "energy": 0.1111,
    "protein": 2.332,
    "sugar": 0,
    "fibre": 0,
    "other_carbohydrates": 0,
    "saturated_fat": 0,
    "polyunsaturated_fat": 1,
    "monounsaturated_fat": 1,
    "sodium": 0,
    "belongs_categories": [{
        "$oid": "5ebaa6ace1e9db12bc5fe71f"
    }, {
        "$oid": "5ebaa74c00f2cddc8aa198de"
    }]
}


print(verify.ingredient(ingredient_document))
