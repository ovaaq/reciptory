# -*- coding: utf-8 -*-

ingredient_category_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The ingredient category schema",
    "description": "The ingredient category schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "name": "chicken",
            "parent_category": {
                "$oid": "5ebaa6ace1e9db12bc5fe71f"
            },
            "child_categories": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                },
                {
                    "$oid": "5ebaa74c00f2cddc8aa198de"
                }
            ]
        }
    ],
    "required": [
        "name",
        "parent_category",
        "child_categories"
    ],
    "additionalProperties": False,
    "properties": {
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "default": "",
            "examples": [
                "chicken"
            ]
        },
        "parent_category": {
            "$id": "#/properties/parent_category",
            "type": "object",
            "default": {},
            "examples": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                }
            ],
            "required": [
                "$oid"
            ],
            "additionalProperties": False,
            "properties": {
                "$oid": {
                    "$id": "#/properties/parent_category/properties/$oid",
                    "type": "string",
                    "default": "",
                    "examples": [
                        "5ebaa6ace1e9db12bc5fe71f"
                    ]
                }
            }
        },
        "child_categories": {
            "$id": "#/properties/child_categories",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "$oid": "5ebaa6ace1e9db12bc5fe71f"
                    },
                    {
                        "$oid": "5ebaa74c00f2cddc8aa198de"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/child_categories/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "$oid": "5ebaa6ace1e9db12bc5fe71f"
                            }
                        ],
                        "required": [
                            "$oid"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "$oid": {
                                "$id": "#/properties/child_categories/items/anyOf/0/properties/$oid",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "5ebaa6ace1e9db12bc5fe71f"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/child_categories/items"
            }
        }
    }
}