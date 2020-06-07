# -*- coding: utf-8 -*-

from source.API.collections.collection_interface import CollectionInterface


class MethodCollection(CollectionInterface):

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