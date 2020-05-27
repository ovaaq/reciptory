# testing the instance of Connection class
from source.API import Verify

ingredient_document = {
    "_id": {"$oid": "placeholder"},
    "name": "kana",
    "belongs_categories": [{"$oid":"2"},{"$oid":"2"}],
    "energy": 0.1111,
    "protein": 2.332,
    "sugar": 0,
    "fibre": 0,
    "other_carbohydrates": 0,
    "saturated_fat": 0,
    "polyunsaturated_fat": 1,
    "monounsaturated_fat": 1,
    "sodium": 0,
}

ingredient_document["_id"]["$oid"] = "new_id"

print(Verify.ingredient(ingredient_document))
