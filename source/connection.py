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

    def add_ingredient(self, ingredient_document):

        try:
            self.ingredients.insert_one(ingredient_document)
            print('Incredient ' + ingredient_document.get("name") + ' added successfully to database')
        except:
            print('Failed to add  ' + ingredient_document.get("name") + ' to database')
            return False

        return True

    def delete_ingredient(self, ingredient_id):

        try:
            self.ingredients.delete_one({"_id": ingredient_id})
            print('Incredient with id ' + ingredient_id + ' is now deleted')
        except:
            print('Failed to delete item with id ' + ingredient_id)
            return False
        return True

    def edit_ingredient(self):
        pass

    def search_ingredient(self, ingredient_id):
        pass

    def get_all_ingredients(self):
        pass

    def get_ingredient(self, ingredient_id):
        return self.ingredients.find_one({"_id": ingredient_id})
