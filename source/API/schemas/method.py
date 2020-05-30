# -*- coding: utf-8 -*-

method_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "title": "The cooking method schema",
    "description": "The cooking method schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "name": "roasting",
            "definition": "Roasting is a cooking method that uses dry heat where hot air covers the food, cooking it "
                          "evenly on all sides with temperatures of at least 150 °C (300 °F) from an open flame, "
                          "oven, or other heat source.",
            "phrases": [
                "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until $p4.",
                "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until internal temperature reaches $p5 $p6."
            ],
            "parameters": [
                {
                    "par_type": "option",
                    "options": [
                        "oven",
                        "open flame",
                        "baking oven",
                        "pizza oven"
                    ]
                },
                {
                    "par_type": "number"
                },
                {
                    "par_type": "option",
                    "options": [
                        "°C",
                        "°F",
                        "°K"
                    ]
                },
                {
                    "par_type": "time"
                },
                {
                    "par_type": "option",
                    "options": [
                        "well done",
                        "medium",
                        "browned"
                    ]
                },
                {
                    "par_type": "number"
                },
                {
                    "par_type": "option",
                    "options": [
                        "°C",
                        "°F",
                        "°K"
                    ]
                }
            ],
            "belongs_categories": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                }
            ]
        }
    ],
    "required": [
        "name",
        "definition",
        "phrases",
        "parameters",
        "belongs_categories"
    ],
    "additionalProperties": False,
    "properties": {
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "default": "",
            "examples": [
                "roasting"
            ]
        },
        "definition": {
            "$id": "#/properties/definition",
            "type": "string",
            "default": "",
            "examples": [
                "Roasting is a cooking method that uses dry heat where hot air covers the food, cooking it evenly on "
                "all sides with temperatures of at least 150 °C (300 °F) from an open flame, oven, or other heat "
                "source. "
            ]
        },
        "phrases": {
            "$id": "#/properties/phrases",
            "type": "array",
            "default": [],
            "examples": [
                [
                    "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until $p4.",
                    "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until internal temperature reaches $p5 $p6."
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/phrases/items/anyOf/0",
                        "type": "string",
                        "default": "",
                        "examples": [
                            "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until $p4.",
                            "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until internal temperature reaches $p5 "
                            "$p6. "
                        ]
                    }
                ],
                "$id": "#/properties/phrases/items"
            }
        },
        "parameters": {
            "$id": "#/properties/parameters",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "par_type": "option",
                        "options": [
                            "oven",
                            "open flame",
                            "baking oven",
                            "pizza oven"
                        ]
                    },
                    {
                        "par_type": "number"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/parameters/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "par_type": "option",
                                "options": [
                                    "oven",
                                    "open flame",
                                    "baking oven",
                                    "pizza oven"
                                ]
                            }
                        ],
                        "required": [
                            "par_type",
                            "options"
                        ],
                        "additionalProperties": true,
                        "properties": {
                            "par_type": {
                                "$id": "#/properties/parameters/items/anyOf/0/properties/par_type",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "option"
                                ]
                            },
                            "options": {
                                "$id": "#/properties/parameters/items/anyOf/0/properties/options",
                                "type": "array",
                                "default": [],
                                "examples": [
                                    [
                                        "oven",
                                        "open flame"
                                    ]
                                ],
                                "additionalItems": True,
                                "items": {
                                    "anyOf": [
                                        {
                                            "$id": "#/properties/parameters/items/anyOf/0/properties/options/items"
                                                   "/anyOf/0",
                                            "type": "string",
                                            "default": "",
                                            "examples": [
                                                "oven",
                                                "open flame"
                                            ]
                                        }
                                    ],
                                    "$id": "#/properties/parameters/items/anyOf/0/properties/options/items"
                                }
                            }
                        }
                    },
                    {
                        "$id": "#/properties/parameters/items/anyOf/1",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "par_type": "number"
                            }
                        ],
                        "required": [
                            "par_type"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "par_type": {
                                "$id": "#/properties/parameters/items/anyOf/1/properties/par_type",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "number"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/parameters/items"
            }
        },
        "belongs_categories": {
            "$id": "#/properties/belongs_categories",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "$oid": "5ebaa6ace1e9db12bc5fe71f"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/belongs_categories/items/anyOf/0",
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
                                "$id": "#/properties/belongs_categories/items/anyOf/0/properties/$oid",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "5ebaa6ace1e9db12bc5fe71f"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/belongs_categories/items"
            }
        }
    }
}