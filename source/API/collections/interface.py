# -*- coding: utf-8 -*-

import pymongo
from bson import ObjectId
from bson.json_util import dumps
from pymongo.cursor import Cursor

from source.API import console, verify
from source.API.connection import Connection


class CollectionInterface:

    def __init__(self, connection: Connection, collection_name: str) -> None:
        """
        Constructor
        :param connection: connection to the database
        :param collection_name: collection name in the database
        """
        self.collection = connection.db.get_collection(collection_name)
        self.name = collection_name

    def add(self, data: dict) -> bool:
        """Add one object to the collection."""
        pass

    def delete(self, object_id: str) -> bool:
        """Delete one object from the collection."""
        pass

    def delete_all(self) -> bool:
        """Delete all of the objects from the collection."""
        pass

    def edit(self, object_id: str, data: dict) -> bool:
        """Edit one object from the collection."""
        pass

    def dump(self, data: dict) -> bool:
        """

        :param json:
        :return:
        """
        json = dumps(data)
        try:
            self.collection.insert_many(json)
        except:
            return False

        return True

    def get_one(self, object_id: str = None) -> (Cursor, None):
        """
        Returns matching ingredient from the database.
        If fetching fails returns None.

        :param object_id: id for the object
        :return: Cursor / None
        """
        if verify.id_check(object_id, self.collection):
            console.log('Object id is not valid in this collection')
            return None

        if object_id is None:
            console.log('There was no object id as a parameter')
            return None

        try:
            cursor = self.collection.find_one({'_id': ObjectId(object_id)})
            if cursor is None:
                console.log('There was no object with id "' + object_id + '" from the collection "'
                            + self.name + '"')
                return None
        except pymongo.errors.OperationFailure as e:
            console.log('Failed to get an object with id "' + object_id + '" from the collection "'
                        + self.name + '"')
            console.log(e.__str__())
            return None

        console.log('Object with id "' + object_id + '" was fetched successfully from the collection "'
                    + self.name + '"')
        return cursor

    def get_all(self) -> (Cursor, None):
        """
        Returns all the ingredient from the database.
        If fetching fails returns None.

        :return: Cursor / None
        """
        try:
            cursor: Cursor = self.collection.find({})
            if cursor.count() < 1:
                console.log('There was no objects in the collection "' + self.name + '"')
                return None
        except pymongo.errors.OperationFailure as e:
            console.log('Failed to get all the objects from the collection "' + self.name + '"')
            console.log(e.__str__())
            return None

        console.log('Objects were fetched successfully from the collection "' + self.name + '"')
        return cursor
