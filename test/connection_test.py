from source.connection import Connection

# testing the instance of Connection class
c = Connection()

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
c.edit_ingredient('5eb7b3e6e333c1bef7e2bb2d', ingredient_document)
print(c.get_ingredient('5eb7b3e6e333c1bef7e2bb2d'))
