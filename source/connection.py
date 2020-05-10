import pymongo
from bson import ObjectId


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
            self.method_categories = self.db.get_collection("cooking_method_categories")
            self.methods = self.db.get_collection("cooking_methods")

        except ValueError:
            print("Connection failed")

    def get_ingredient(self, ingredient_id):
        """Use ingredient_id to return ingredient dictionary.
        If there is error return is None.

        Keyword arguments:
        ingredient_id -- database id for the object
        """
        try:
            tmp = self.ingredients.find_one({'_id': ObjectId(ingredient_id)})
            print('Ingredient ' + tmp.get('name') + ' was fetched successfully')
        except:
            print('Ingredient fetch failed')
            return None

        return tmp

    def get_all_ingredients(self):
        """Returns all ingredients found in the database.
        If fetching fails returns null.
        """
        try:
            tmp = self.ingredients.find({})
            print('Ingredients were fetched successfully')
        except:
            print('Ingredients fetch failed')
            return None

        return tmp

    def add_ingredient(self, ingredient_document):
        """Tries to add an ingredient to the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        """
        try:
            self.ingredients.insert_one(ingredient_document)
            print('Incredient ' + ingredient_document.get('name') + ' added successfully to database')
        except:
            print('Failed to add  ' + ingredient_document.get('name') + ' to database')
            return False

        return True

    def delete_ingredient(self, ingredient_id):
        """Tries to delete an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.ingredients.delete_one({"_id": ObjectId(ingredient_id)})
            print('Ingredient with id ' + ingredient_id + ' is now deleted')
        except:
            print('Failed to delete item with id ' + ingredient_id)
            return False

        return True

    def edit_ingredient(self, ingredient_id, ingredient_document):
        """Tries to edit an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.ingredients.find_and_modify({"_id": ObjectId(ingredient_id)}, {"$set": ingredient_document},
                                             upsert=True)
            print('Ingredient ' + ingredient_document.get("name") + ' was successfully edited in database')
        except:
            print('Failed to edit to database')
            return False

        return True
