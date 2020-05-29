# -*- coding: utf-8 -*-

ingredient_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The ingredient schema",
    "description": "The ingredient schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "name": "raw chicken breast",
            "energy": 114.0,
            "protein": 21.2,
            "sugar": 0.0,
            "fibre": 0.0,
            "other_carbohydrates": 0.0,
            "saturated_fat": 0.6,
            "monounsaturated_fat": 0.8,
            "polyunsaturated_fat": 0.4,
            "sodium": 0.116,
            "belongs_categories": [
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
        "energy",
        "protein",
        "sugar",
        "fibre",
        "other_carbohydrates",
        "saturated_fat",
        "monounsaturated_fat",
        "polyunsaturated_fat",
        "sodium",
        "belongs_categories"
    ],
    "additionalProperties": False,
    "properties": {
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "default": "",
            "examples": [
                "raw chicken breast"
            ]
        },
        "energy": {
            "$id": "#/properties/energy",
            "type": "number",
            "default": 0.0,
            "examples": [
                114.0
            ]
        },
        "protein": {
            "$id": "#/properties/protein",
            "type": "number",
            "default": 0.0,
            "examples": [
                21.2
            ]
        },
        "sugar": {
            "$id": "#/properties/sugar",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.0
            ]
        },
        "fibre": {
            "$id": "#/properties/fibre",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.0
            ]
        },
        "other_carbohydrates": {
            "$id": "#/properties/other_carbohydrates",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.0
            ]
        },
        "saturated_fat": {
            "$id": "#/properties/saturated_fat",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.6
            ]
        },
        "monounsaturated_fat": {
            "$id": "#/properties/monounsaturated_fat",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.8
            ]
        },
        "polyunsaturated_fat": {
            "$id": "#/properties/polyunsaturated_fat",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.4
            ]
        },
        "sodium": {
            "$id": "#/properties/sodium",
            "type": "number",
            "default": 0.0,
            "examples": [
                0.116
            ]
        },
        "belongs_categories": {
            "$id": "#/properties/belongs_categories",
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
                        "$id": "#/properties/belongs_categories/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
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
                                "$id": "#/properties/belongs_categories/items/anyOf/0/properties/$oid",
                                "type": "string",
                                "title": "The $oid schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "5ebaa6ace1e9db12bc5fe71f"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/belongs_categories/items"
            },
            "minItems": 1
        }
    },
}