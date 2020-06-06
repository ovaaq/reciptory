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
            try:
                parent_id = document["parent_category"]
                parent = self.get(parent_id.__str__())
                id_list = parent.get("child_categories")
                id_list.append(ObjectId(object_id))
                parent["child_categories"] = id_list
                del parent["_id"]
                self.edit(parent_id.__str__(), parent)
            except:
                pass
            print('Object with id "' + object_id.__str__()
                  + '" was added successfully to the collection "' + self.name + '"')
        except Exception as e:
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
            soon_deleted = self.collection.find_one({"_id": ObjectId(object_id)})
            try:
                #parent_id = soon_deleted.get("parent_category")
                #edit_parent = self.get(parent_id)
                #parents_children = edit_parent.get("child_categories")
                #edit_parent.set(parents_children.remove(object_id))
                #self.edit(parent_id, edit_parent)
                child_object = soon_deleted["child_categories"]
                for child in child_object:
                    print(child)
                    self.delete(child.__str__())
            except:
                pass
            return_value = self.collection.delete_one({"_id": ObjectId(object_id)})
            print(return_value)
            print('Object with id ' + object_id
                  + ' was deleted successfully from the collection "' + self.name + '"')
        except:
            print('Failed to delete object with id "' + object_id + '" from the collection "' + self.name + '"')
            return False

        return True

    def delete_all(self):
        """Tries to delete an ingredient from the database and
        returns boolean about outcome.

        Keyword arguments:
        ingredient_id -- database id for the ingredient object
        """
        try:
            self.collection.delete_many({})
            print('All objects were deleted successfully from the collection "' + self.name + '"')
        except Exception as e:
            print(e)
            print('Failed to delete all objects from the collection "' + self.name + '"')
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
            print('Failed to edit object with id ' + object_id + '  in the collection "' + self.name + '"')
            return False

        return True
