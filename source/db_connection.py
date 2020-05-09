import pymongo

class Connection:

    connection_address = 'mongodb://localhost:27017'
    user = "dummy"
    password = "placeholder"
    db = None

    def __init__(self, connection_address = None, user = None, password = None):
        if connection_address is not None:
            self.connection_address = connection_address

        if user is not None:
            self.user = user

        if password is not None:
            self.password = password

        client = pymongo.MongoClient(connection_address)

        self.db = client.get_database("local")

ingredient_categories = db.get_collection("incredient_categories")
ingredients = db.get_collection("ingredients")
cooking_method_categories = db.get_collection("cooking_method_categories")
cooking_methods = db.get_collection("cooking_methods")

