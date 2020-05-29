# -*- coding: utf-8 -*-

recipe_category_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The recipe category schema",
    "description": "The recipe category schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "name": "dessert",
            "definition": "A usually sweet course or dish, as of fruit, ice cream, or pastry, served at the end of a "
                          "meal. "
        }
    ],
    "required": [
        "name",
        "definition"
    ],
    "additionalProperties": False,
    "properties": {
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "default": "",
            "examples": [
                "dessert"
            ]
        },
        "definition": {
            "$id": "#/properties/definition",
            "type": "string",
            "default": "",
            "examples": [
                "A usually sweet course or dish, as of fruit, ice cream, or pastry, served at the end of a meal."
            ]
        }
    }
}