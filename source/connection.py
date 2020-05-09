import pymongo
from pymongo.errors import WriteError


class Connection:

    def __init__(self, host='localhost', port='27017', user='', password=''):

        if len(password) > 0 and len(user) > 0:
            uri = "mongodb://%s:%s@%s:%s" % (user, password, host, port)
        else:
            uri = "mongodb://%s:%s" % (host, port)

        try:
            client = pymongo.MongoClient(uri)
            print("Connected to " + uri)
            self.db = client.get_database("local")

            self.ingredient_categories = self.db.get_collection("incredient_categories")
            self.ingredients = self.db.get_collection("ingredients")
            self.cooking_method_categories = self.db.get_collection("cooking_method_categories")
            self.cooking_methods = self.db.get_collection("cooking_methods")

        except ValueError:
            print("Connection failed")

    def add_ingredient(self, name, belongs_categories, nutritional_info):

        try:
            ingredient_document = {
                "name": name,
                "belongs_categories": belongs_categories,
                "energy": nutritional_info[0],
                "protein": nutritional_info[1],
                "sugar": nutritional_info[2],
                "fibre": nutritional_info[3],
                "other_carbohydrates": nutritional_info[4],
                "saturated_fat": nutritional_info[5],
                "polyunsaturated_fat": nutritional_info[6],
                "monounsaturated_fat": nutritional_info[7],
                "sodium": nutritional_info[8]
            }

            self.ingredients.insert_one(ingredient_document)
            print('Incredient ' + name + ' added successfully to database')
        except (IndexError, TypeError, ValueError):
            print('Failed to add ' + name + ' to database')
            return False

        return True

    def delete_ingredient(self):
        pass

    def edit_ingredient(self):
        pass

    def search_ingredient(self, ingredient_id):
        pass

    def get_all_ingredients(self):
        pass
