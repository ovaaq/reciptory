# -*- coding: utf-8 -*-

from typing import IO

import pymongo
from bson import ObjectId
from bson.json_util import loads, dumps
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
        try:
            document: dict = loads(dumps(data))
            object_id: ObjectId = self.collection.insert_one(document).inserted_id
            console.log('Object with id "' + object_id.__str__()
                        + '" was added successfully to the collection "' + self.name + '"')
        except Exception as e:
            console.log('Failed to add object to the collection "' + self.name + '"')
            console.exception(e)
            return False

        return True

    def delete(self, object_id: str) -> bool:
        """Delete one object from the collection."""
        try:
            count: int = self.collection.delete_one({"_id": ObjectId(object_id)}).deleted_count
            if count > 0:
                console.log('Object with id ' + object_id
                            + ' was deleted successfully from the collection "' + self.name + '"')
            else:
                raise Exception
        except Exception as e:
            console.log('Failed to delete object with id "' + object_id + '" from the collection "' + self.name + '"')
            console.exception(e)
            return False

        return True

    def delete_all(self) -> bool:
        """Delete all of the objects from the collection."""
        try:
            self.collection.drop()
            console.log('All objects were deleted successfully from the collection "' + self.name + '"')
        except Exception as e:
            console.log('Failed to delete all objects from the collection "' + self.name + '"')
            console.exception(e)
            return False

        return True

    def edit(self, object_id: str, data: dict) -> bool:
        """Edit one object from the collection."""
        try:
            document: dict = loads(dumps(data))
            self.collection.replace_one({"_id": ObjectId(object_id)}, document)
            console.log(
                'Object with id ' + object_id + ' was edited successfully in the collection "' + self.name + '"')
        except Exception as e:
            console.log('Failed to edit object with id "' + object_id + '"  in the collection "' + self.name + '"')
            console.exception(e)
            return False

        return True

    def dump(self, path: str) -> bool:
        """
        Dumps JSON-file containing objects
        to the collection. Returns boolean about success.

        :param path: str path to the JSON-file
        :return: bool
        """
        try:
            json_file: IO = open(path)
            json_str: str = json_file.read()
            document: dict = loads(json_str)
            self.collection.insert_many(document)
        except pymongo.errors.BulkWriteError as e:
            console.log('Failed to dump JSON-file into collection "' + self.name + '"')
            console.exception(e)
            return False

        console.log('JSON-file successfully dumped into collection "' + self.name + '"')
        return True

    def get_one(self, object_id: str = None) -> (Cursor, None):
        """
        Returns matching object from the collection.
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
            console.exception(e)
            return None

        console.log('Object with id "' + object_id + '" was fetched successfully from the collection "'
                    + self.name + '"')
        return cursor

    def get_all(self) -> (Cursor, None):
        """
        Returns all the objects from the collection.
        If fetching fails returns None.

        :return: Cursor / None
        """
        self.collection.count_documents()
        try:
            cursor: Cursor = self.collection.find({})
            if cursor.count() < 1:
                console.log('There was no objects in the collection "' + self.name + '"')
                return None
        except pymongo.errors.OperationFailure as e:
            console.log('Failed to get all the objects from the collection "' + self.name + '"')
            console.exception(e)
            return None

        console.log('Objects were fetched successfully from the collection "' + self.name + '"')
        return cursor
