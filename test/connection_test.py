from source.Connection import Connection

# testing the instance of Connection class
from source.Collection import Ingredient

c = Connection()
i = Ingredient(c)

ingredient_document = {
    "name": "asdasdasd",
    "belongs_categories": [1, 2, 3],
    "energy": 0,
    "protein": 0,
    "sugar": 0,
    "fibre": 0,
    "other_carbohydrates": 0,
    "saturated_fat": 0,
    "polyunsaturated_fat": 1,
    "monounsaturated_fat": 1,
    "sodium": 0
}
i.edit('5eb7b3e6e333c1bef7e2bb2d', ingredient_document)
print(i.get('5eb7b3e6e333c1bef7e2bb2d'))
