# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator

from source.API.schemas.ingredient import ingredient_schema
from source.API.schemas.ingredient_category import ingredient_category_schema
from source.API.schemas.method import method_schema
from source.API.schemas.method_category import method_category_schema
from source.API.schemas.recipe import recipe_schema
from source.API.schemas.recipe_category import recipe_category_schema


def verify(document, schema):
    """Verifies that document is appropriately
    formed. Returns True if document is formed
    as schema instructs. Returns list of errors
    otherwise.

    Keyword arguments:
    document -- document object to verify
    schema -- schema which is used to validate
    """
    errors = []
    validator = Draft4Validator(schema)
    for error in sorted(validator.iter_errors(document), key=str):
        errors.append(error.message)

    if len(errors) > 0:
        return errors
    return True


def recipe(document):
    """Verifies that recipe is appropriately
    formatted. Returns True if valid and list
    of errors otherwise.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, recipe_schema)


def recipe_category(document):
    """Verifies that recipe category is appropriately
    formatted. Returns True if valid and list
    of errors otherwise.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, recipe_category_schema)


def ingredient(document):
    """Verifies that ingredient is appropriately
    formatted. Returns True if valid and list
    of errors otherwise.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, ingredient_schema)


def ingredient_category(document):
    """Verifies that ingredient category
     is appropriately formatted. Returns True
     if valid and list of errors otherwise.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, ingredient_category_schema)


def method(document):
    """Verifies that method is appropriately
    formatted. Returns True if valid and list
    of errors otherwise.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, method_schema)


def method_category(document):
    """Verifies that method category is appropriately
    formatted. Returns True if valid and list
    of errors otherwise.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, method_category_schema)
