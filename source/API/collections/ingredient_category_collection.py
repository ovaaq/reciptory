# -*- coding: utf-8 -*-

from source.API.collections.collection_interface import CollectionInterface


class IngredientCategoryCollection(CollectionInterface):



    def delete(self, object_id: str) -> bool:
        """Delete one object from the collection."""
        pass

    def delete_all(self) -> bool:
        """Delete all of the objects from the collection."""
        pass

