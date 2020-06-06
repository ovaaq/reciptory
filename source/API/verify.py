# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator

from source.API.schemas.ingredient import ingredient_schema
from source.API.schemas.ingredient_category import ingredient_category_schema
from source.API.schemas.method import method_schema
from source.API.schemas.method_category import method_category_schema
from source.API.schemas.recipe import recipe_schema
from source.API.schemas.recipe_category import recipe_category_schema


def verify(document, schema) -> list:
    """
    Verifies that document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param schema: schema for correct format
    :param document: document to verify
    :return: list
    """
    errors: list = []
    validator: Draft4Validator = Draft4Validator(schema)
    for error in sorted(validator.iter_errors(document), key=str):
        errors.append(error.message)

    return errors


def recipe(document) -> list:
    """
    Verifies that recipe document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param document: recipe document to verify
    :return: list
    """
    return verify(document, recipe_schema)


def recipe_category(document) -> list:
    """
    Verifies that recipe category document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param document: recipe category document to verify
    :return: list
    """
    return verify(document, recipe_category_schema)


def ingredient(document) -> list:
    """
    Verifies that ingredient document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param document: ingredient document to verify
    :return: list
    """
    return verify(document, ingredient_schema)


def ingredient_category(document) -> list:
    """
    Verifies that ingredient category document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param document: ingredient category document to verify
    :return: list
    """
    return verify(document, ingredient_category_schema)


def method(document) -> list:
    """
    Verifies that method document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param document: method document to verify
    :return: list
    """
    return verify(document, method_schema)


def method_category(document) -> list:
    """
    Verifies that method category document is appropriately
    formatted. Returns a list of errors. Empty list
    implies correct document.

    :param document: method category document to verify
    :return: list
    """
    return verify(document, method_category_schema)


def id_check(object_id: str, collection) -> bool:
    """
    Checks if object id is valid as an
    reference in selected collection.

    :param object_id: Id that is checked
    :param collection: Collection where to check
    :return: bool
    """

    # TODO: feature/ID-CHECK
    #  *logic to check is id legit
    return False
