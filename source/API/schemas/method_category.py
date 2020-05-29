# -*- coding: utf-8 -*-

method_category_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The method category schema",
    "description": "The method category schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "name": "dry-heat",
            "definition": "Dry heat cooking refers to any cooking technique where the heat is transferred to the food "
                          "item without using extra moisture. This method typically involves high temperatures 300 C "
                          "or hotter. "
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
                "dry-heat"
            ]
        },
        "definition": {
            "$id": "#/properties/definition",
            "type": "string",
            "default": "",
            "examples": [
                "Dry heat cooking refers to any cooking technique where the heat is transferred to the food item "
                "without using extra moisture. This method typically involves high temperatures 300 C or hotter. "
            ]
        }
    }
}