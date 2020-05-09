import pymongo


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