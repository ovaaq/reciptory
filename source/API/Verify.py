import jsonschema
from jsonschema import validate
from source.API.Schemas import Schemas


def verify(document, schema):
    """Verifies that document is appropriately
    formed. Returns True if document is formed
    as schema instructs.

    Keyword arguments:
    document -- document object to verify
    schema -- schema which is used to validate
    """
    try:
        validate(instance=document, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        print(e)
        return False

    return True


def recipe(document):
    """Verifies that recipe is appropriately
    formatted. Returns boolean.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, Schemas.recipe)


def recipe_category(document):
    """Verifies that recipe category is appropriately
    formatted. Returns boolean.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, Schemas.recipe_category)


def ingredient(document):
    """Verifies that ingredient is appropriately
    formatted. Returns boolean.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, Schemas.ingredient)


def ingredient_category(document):
    """Verifies that ingredient category
     is appropriately formatted. Returns boolean.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, Schemas.ingredient_category)


def method(document):
    """Verifies that method is appropriately
    formatted. Returns boolean.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, Schemas.method)


def method_category(document):
    """Verifies that method category is appropriately
    formatted. Returns boolean.

    Keyword arguments:
    document -- document object to verify
    """
    return verify(document, Schemas.method_category)


