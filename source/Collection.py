from bson import ObjectId


class Collection:

    def __init__(self, connection, collection_name, ):
        """Constructor

        Keyword arguments:
        connection -- connection to the database
        collection_name -- collection name in the database
        """
        self.collection = connection.db.get_collection(collection_name)

    def verify(self, document):
        """Verifies that document is appropriately
        formed. Returns boolean about the verification.

        Keyword arguments:
        document -- document object to verify
        """
        pass

    def get(self, id):
        """Returns matching ingredient from the database.
        If fetching fails returns None.

        Keyword arguments:
        ingredient_id -- database id for the object
        """
        try:
            tmp = self.collection.find_one({'_id': ObjectId(id)})
            print('Ingredient ' + tmp.get('name') + ' was fetched successfully')
        except:
            print('Ingredient fetch failed')
            return None

        return tmp

    def get_all(self):
        """Returns all ingredients from the database.
        If fetching fails returns None.
        """
        try:
            tmp = self.collection.find({})
            print('Ingredients were fetched successfully')
        except:
            print('Ingredients fetch failed')
            return None

        return tmp

    def add(self, document):
        """Tries to add an ingredient to the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        """
        try:
            self.collection.insert_one(document)
            print('Ingredient ' + document.get('name') + ' added successfully to database')
        except:
            print('Failed to add  ' + document.get('name') + ' to database')
            return False

        return True

    def delete(self, id):
        """Tries to delete an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.collection.delete_one({"_id": ObjectId(id)})
            print('Ingredient with id ' + id + ' is now deleted')
        except:
            print('Failed to delete item with id ' + id)
            return False

        return True

    def edit(self, id, document):
        """Tries to edit an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.collection.find_and_modify({"_id": ObjectId(id)}, {"$set": document}, upsert=True)
            print('Ingredient ' + document.get("name") + ' was successfully edited in database')
        except:
            print('Failed to edit to database')
            return False

        return True
