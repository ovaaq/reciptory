# -*- coding: utf-8 -*-

from bson import ObjectId
from bson.json_util import loads, dumps


class Collection:

    def __init__(self, connection, collection_name):
        """Constructor

        Keyword arguments:
        connection -- connection to the database
        collection_name -- collection name in the database
        """
        self.collection = connection.db.get_collection(collection_name)
        self.name = collection_name

    def get(self, object_id=None):
        """Returns matching ingredient from the database.
        If fetching fails returns None.

        Keyword arguments:
        ingredient_id -- database id for the object
        """
        try:
            if object_id is not None:
                tmp = self.collection.find_one({'_id': ObjectId(object_id)})
            if tmp is None:
                print('There was no object with id "' + object_id + '" in the collection "' + self.name + '"')
                return None

            print('Object with id "' + object_id + '" from the collection "'
                  + self.name + '" was fetched successfully')
        except:
            print('There was no object with id "' + object_id + '" in the collection "' + self.name + '"')
            return None

        return tmp

    def get_all(self):
        """Returns all ingredients from the database.
        If fetching fails returns None.
        """
        try:
            tmp = self.collection.find({})
            if tmp.count() < 1:
                print('There was no objects in the collection "' + self.name + '"')
                return None
            print('Objects from the collection "' + self.name + '" were fetched successfully')
        except:
            print('Failed to fetch from the collection "' + self.name + '"')
            return None

        return tmp

    def add(self, data):
        """Tries to add an ingredient to the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        """
        try:
            document = loads(dumps(data))
            object_id = self.collection.insert_one(document).inserted_id
            print('Object with id "' + object_id.__str__()
                  + '" was added successfully to the collection "' + self.name + '"')
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
            print('Object with id ' + object_id
                  + ' was deleted successfully from the collection "' + self.name + '"')
        except:
            print('Failed to delete object to the collection "' + self.name + '"')
            return False

        return True

    def edit(self, object_id, data):
        """Tries to edit an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_document -- dictionary for the ingredient object
        ingredient_id -- database id for the ingredient object
        """
        try:
            document = loads(dumps(data))
            self.collection.update({"_id": ObjectId(object_id)}, document)
            print('Object with id ' + object_id + ' was edited successfully in the collection "' + self.name + '"')
        except:
            print('Failed to edit object in the collection "' + self.name + '"')
            return False

        return True
