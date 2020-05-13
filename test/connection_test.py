from source.Connection import Connection

# testing the instance of Connection class
from source.Collection import Collection

c = Connection()
i = Collection(c,'ingredients')

ingredient_document = {
    "name": "kana",
    "belongs_categories": [2,1],
    "energy": 0.1111,
    "protein": 2.332,
    "sugar": 0,
    "fibre": 0,
    "other_carbohydrates": 0,
    "saturated_fat": 0,
    "polyunsaturated_fat": 1,
    "monounsaturated_fat": 1,
    "sodium": 0
}

i.add(ingredient_document)

x = i.get_all()

for y in x:
    print(y)