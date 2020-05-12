from bson import ObjectId


class Collection:

    def __init__(self, connection, collection_name):
        """Constructor

        Keyword arguments:
        connection -- connection to the database
        collection_name -- collection name in the database
        """
        self.collection = connection.db.get_collection(collection_name)
        self.name = collection_name

    def verify(self, document):
        """Verifies that document is appropriately
        formed. Returns boolean about the verification.

        Keyword arguments:
        document -- document object to verify
        """
        control_object = self.get()
        for attribute in control_object:
            if attribute == "_id":
                continue

            control_type = control_object.get(attribute)
            document_type = document.get(attribute)

            if document_type is None:
                print('Document is missing attribute ' + attribute)
                return False

            if isinstance(control_type, str):
                if not isinstance(document_type, str):
                    print('Document\'s attribute "' + attribute + '" should have type "str" currently is "'
                          + document_type.__str__() + '"')
                    return False

            if isinstance(control_object.get(attribute), list):
                if not isinstance(document_type, list):
                    print('Document\'s attribute "' + attribute + '" should have type "list" currently is "'
                          + document_type.__str__() + '"')
                    return False

            if isinstance(control_type, int) or isinstance(control_type, float):
                if not (isinstance(document_type, int) or isinstance(document_type, float)):
                    print('Document\'s attribute "' + attribute + '" should be type "int" or "float" currently is "'
                          + document_type.__str__() + '"')
                    return False

        return True

    def get(self, object_id='random'):
        """Returns matching ingredient from the database.
        If fetching fails returns None.

        Keyword arguments:
        ingredient_id -- database id for the object
        """
        try:
            if object_id != 'random':
                tmp = self.collection.find_one({'_id': ObjectId(object_id)})
            else:
                tmp = self.collection.find_one({})

            if tmp is None:
                print('There was no object with id "' + object_id + '" in the collection "' + self.name + '"')
                return tmp
            print('Object with id "' + object_id + '" from the collection "' + self.name + '" was fetched successfully')
        except:
            print('Failed to fetch from the collection "' + self.name + '"')
            return None

        return tmp

    def get_all(self):
        """Returns all ingredients from the database.
        If fetching fails returns None.
        """
        try:
            tmp = self.collection.find({})
            if tmp is None:
                print('There was no objects in the collection "' + self.name + '"')
                return tmp
            print('Objects from the collection "' + self.name + '" were fetched successfully')
        except:
            print('Failed to fetch from the collection "' + self.name + '"')
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
            print('Object was added successfully to the collection "' + self.name + '"')
        except:
            print('Failed to add object to the collection "' + self.name + '"')
            return False

        return True

    def delete(self, object_id):
        """Tries to delete an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.collection.delete_one({"_id": ObjectId(object_id)})
            print('Object with id ' + object_id + ' was deleted successfully from the collection "' + self.name + '"')
        except:
            print('Failed to delete object to the collection "' + self.name + '"')
            return False

        return True

    def edit(self, object_id, document):
        """Tries to edit an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.collection.find_and_modify({"_id": ObjectId(object_id)}, {"$set": document}, upsert=True)
            print('Object with id ' + object_id + ' was edited successfully in the collection "' + self.name + '"')
        except:
            print('Failed to edit object in the collection "' + self.name + '"')
            return False

        return True
