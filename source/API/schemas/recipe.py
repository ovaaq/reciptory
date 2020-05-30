# -*- coding: utf-8 -*-

recipe_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The recipe schema",
    "description": "The recipe schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "name": "Pizza Dough",
            "authors": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                }
            ],
            "belongs_categories": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                },
                {
                    "$oid": "5ebaa74c00f2cddc8aa198de"
                }
            ],
            "ingredients": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f",
                    "amount": 200,
                    "measurement": "grams"
                },
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f",
                    "amount": 200,
                    "measurement": "grams"
                }
            ],
            "methods": [
                {
                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                },
                {
                    "$oid": "5ebaa74c00f2cddc8aa198de"
                }
            ],
            "steps": [
                {
                    "method": {
                        "$oid": "5ebaa6ace1e9db12bc5fe71f"
                    },
                    "method_params": [
                        "00:23:23",
                        "200",
                        3
                    ],
                    "raw_ingredients": [
                        1,
                        4
                    ],
                    "end_products": [],
                    "end_product": "dry ingredients",
                    "additional_info": "Be careful with hot tools."
                },
                {
                    "method": {
                        "$oid": "5ebaa6ace1e9db12bc5fe71f"
                    },
                    "method_params": [
                        "00:72:11",
                        "smooth",
                        2,
                        "kneeded"
                    ],
                    "raw_ingredients": [
                        2,
                        3
                    ],
                    "end_products": [
                        1
                    ],
                    "end_product": "dough",
                    "additional_info": "Work the dough"
                }
            ]
        }
    ],
    "required": [
        "name",
        "authors",
        "belongs_categories",
        "ingredients",
        "methods",
        "steps"
    ],
    "additionalProperties": False,
    "properties": {
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "Pizza Dough"
            ]
        },
        "authors": {
            "$id": "#/properties/authors",
            "type": "array",
            "title": "The authors schema",
            "description": "An explanation about the purpose of this instance.",
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
                        "$id": "#/properties/authors/items/anyOf/0",
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
                                "$id": "#/properties/authors/items/anyOf/0/properties/$oid",
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
                "$id": "#/properties/authors/items"
            }
        },
        "belongs_categories": {
            "$id": "#/properties/belongs_categories",
            "type": "array",
            "title": "The belongs_categories schema",
            "description": "An explanation about the purpose of this instance.",
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
            }
        },
        "ingredients": {
            "$id": "#/properties/ingredients",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "$oid": "5ebaa6ace1e9db12bc5fe71f",
                        "amount": 200,
                        "measurement": "grams"
                    },
                    {
                        "$oid": "5ebaa6ace1e9db12bc5fe71f",
                        "amount": 200,
                        "measurement": "grams"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/ingredients/items/anyOf/0",
                        "type": "object",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "$oid": "5ebaa6ace1e9db12bc5fe71f",
                                "amount": 200,
                                "measurement": "grams"
                            }
                        ],
                        "required": [
                            "$oid",
                            "amount",
                            "measurement"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "$oid": {
                                "$id": "#/properties/ingredients/items/anyOf/0/properties/$oid",
                                "type": "string",
                                "title": "The $oid schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "5ebaa6ace1e9db12bc5fe71f"
                                ]
                            },
                            "amount": {
                                "$id": "#/properties/ingredients/items/anyOf/0/properties/amount",
                                "type": "integer",
                                "title": "The amount schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    200
                                ]
                            },
                            "measurement": {
                                "$id": "#/properties/ingredients/items/anyOf/0/properties/measurement",
                                "type": "string",
                                "title": "The measurement schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "grams"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/ingredients/items"
            }
        },
        "methods": {
            "$id": "#/properties/methods",
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
                        "$id": "#/properties/methods/items/anyOf/0",
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
                                "$id": "#/properties/methods/items/anyOf/0/properties/$oid",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "5ebaa6ace1e9db12bc5fe71f"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/methods/items"
            }
        },
        "steps": {
            "$id": "#/properties/steps",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "method": {
                            "$oid": "5ebaa6ace1e9db12bc5fe71f"
                        },
                        "method_params": [
                            "00:23:23",
                            "200",
                            3
                        ],
                        "raw_ingredients": [
                            1,
                            4
                        ],
                        "end_products": [],
                        "end_product": "dry ingredients",
                        "additional_info": "Be careful with hot tools."
                    },
                    {
                        "method": {
                            "$oid": "5ebaa6ace1e9db12bc5fe71f"
                        },
                        "method_params": [
                            "00:72:11",
                            "smooth",
                            2,
                            "kneeded"
                        ],
                        "raw_ingredients": [
                            2,
                            3
                        ],
                        "end_products": [
                            1
                        ],
                        "end_product": "dough",
                        "additional_info": "Work the dough"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/steps/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "method": {
                                    "$oid": "5ebaa6ace1e9db12bc5fe71f"
                                },
                                "method_params": [
                                    "00:23:23",
                                    "200",
                                    3
                                ],
                                "raw_ingredients": [
                                    1,
                                    4
                                ],
                                "end_products": [],
                                "end_product": "dry ingredients",
                                "additional_info": "Be careful with hot tools."
                            }
                        ],
                        "required": [
                            "method",
                            "method_params",
                            "raw_ingredients",
                            "end_products",
                            "end_product",
                            "additional_info"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "method": {
                                "$id": "#/properties/steps/items/anyOf/0/properties/method",
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
                                        "$id": "#/properties/steps/items/anyOf/0/properties/method/properties/$oid",
                                        "type": "string",
                                        "default": "",
                                        "examples": [
                                            "5ebaa6ace1e9db12bc5fe71f"
                                        ]
                                    }
                                }
                            },
                            "method_params": {
                                "$id": "#/properties/steps/items/anyOf/0/properties/method_params",
                                "type": "array",
                                "default": [],
                                "examples": [
                                    [
                                        "00:23:23",
                                        "200"
                                    ]
                                ],
                                "additionalItems": True,
                                "items": {
                                    "anyOf": [
                                        {
                                            "$id": "#/properties/steps/items/anyOf/0/properties/method_params/items"
                                                   "/anyOf/0",
                                            "type": "string",
                                            "default": "",
                                            "examples": [
                                                "00:23:23",
                                                "200"
                                            ]
                                        },
                                        {
                                            "$id": "#/properties/steps/items/anyOf/0/properties/method_params/items"
                                                   "/anyOf/1",
                                            "type": "integer",
                                            "default": 0,
                                            "examples": [
                                                3
                                            ]
                                        }
                                    ],
                                    "$id": "#/properties/steps/items/anyOf/0/properties/method_params/items"
                                }
                            },
                            "raw_ingredients": {
                                "$id": "#/properties/steps/items/anyOf/0/properties/raw_ingredients",
                                "type": "array",
                                "default": [],
                                "examples": [
                                    [
                                        1,
                                        4
                                    ]
                                ],
                                "additionalItems": True,
                                "items": {
                                    "anyOf": [
                                        {
                                            "$id": "#/properties/steps/items/anyOf/0/properties/raw_ingredients/items"
                                                   "/anyOf/0",
                                            "type": "integer",
                                            "default": 0,
                                            "examples": [
                                                1,
                                                4
                                            ]
                                        }
                                    ],
                                    "$id": "#/properties/steps/items/anyOf/0/properties/raw_ingredients/items"
                                }
                            },
                            "end_products": {
                                "$id": "#/properties/steps/items/anyOf/0/properties/end_products",
                                "type": "array",
                                "default": [],
                                "examples": [
                                    []
                                ],
                                "additionalItems": True,
                                "items": {
                                    "anyOf": [],
                                    "$id": "#/properties/steps/items/anyOf/0/properties/end_products/items"
                                }
                            },
                            "end_product": {
                                "$id": "#/properties/steps/items/anyOf/0/properties/end_product",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "dry ingredients"
                                ]
                            },
                            "additional_info": {
                                "$id": "#/properties/steps/items/anyOf/0/properties/additional_info",
                                "type": "string",
                                "default": "",
                                "examples": [
                                    "Be careful with hot tools."
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/steps/items"
            }
        }
    }
}