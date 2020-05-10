from source.connection import Connection

# testing the instance of Connection class
c = Connection()

ingredient_document = {
    "name": "porkkana",
    "belongs_categories": [1, 2, 3],
    "energy": 0,
    "protein": 0,
    "sugar": 0,
    "fibre": 0,
    "other_carbohydrates": 0,
    "saturated_fat": 0,
    "polyunsaturated_fat": 0,
    "monounsaturated_fat": 0,
    "sodium": 0
}

c.add_ingredient(ingredient_document)
c.delete_ingredient('5eb71947d05729f03c9c10d2')
print(c.get_ingredient('5eb7b3a957742de724ce39b5'))
