class Schemas:

    ingredient = {
        "title": "Ingredient",
        "maxProperties": 12,
        "properties": {
            "_id": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "name": {"type": "string"},
            "energy": {"type": "number"},
            "protein": {"type": "number"},
            "sugar": {"type": "number"},
            "fibre": {"type": "number"},
            "other_carbohydrates": {"type": "number"},
            "saturated_fat": {"type": "number"},
            "polyunsaturated_fat": {"type": "number"},
            "monounsaturated_fat": {"type": "number"},
            "sodium": {"type": "number"},
            "belongs_categories": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    },
                    "required": ["$oid"]
                }
            }
        },
        "required": ["_id", "name", "energy", "protein", "sugar", "fibre", "other_carbohydrates", "saturated_fat",
                     "polyunsaturated_fat", "monounsaturated_fat", "sodium", "belongs_categories"]
    }

    ingredient_category = {
        "title": "Ingredient Category",
        "maxProperties": 4,
        "properties": {
            "_id": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "name": {"type": "string"},
            "parent_category": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "child_categories": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    },
                    "required": ["$oid"]
                }
            }
        },
        "required": ["_id", "name", "parent_category", "child_categories"]
    }

    method = {
        "title": "Method",
        "maxProperties": 5,
        "properties": {
            "_id": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "belongs_categories": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "$oid": {"type": "string"}
                    },
                    "required": ["$oid"]
                }
            },
            "name": {"type": "string"},
            "definition": {"type": "string"},
            "parameters": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "param_type": {"type": "string"},
                        "name": {"type": "string"},
                        "options": {"type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                        },
                        "variable": {"type": ["string", "number", "boolean"]}
                    }
                },
                "required": ["$oid"]
            }
        },
        "required": ["_id", "name", "belongs_categories", "definition", "parameters"]
    }

    method_category = {
        "title": "Method Category",
        "maxProperties": 3,
        "properties": {
            "_id": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "name": {"type": "string"},
            "definition": {"type": "string"},
        },
        "required": ["_id", "name", "definition"]
    }

    recipe = {
        "title": "Recipe",
        "maxProperties": 7,
        "properties": {
            "_id": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "name": {"type": "string"},
            "intro": {"type": "string"},
            "recipe_categories": {
                "type": "array",
                "items": {
                    "type": "object",
                    "maxProperties": 1,
                    "properties": {
                        "$oid": {"type": "string"}
                    },
                    "required": ["$oid"]
                }
            },
            "ingredients": {
                "type": "array",
                "items": {
                    "type": "object",
                    "maxProperties": 3,
                    "properties": {
                        "_id": {
                            "type": "object",
                            "properties": {
                                "$oid": {
                                    "type": "string"
                                }
                            }
                        },
                        "amount": {"type": "number"},
                        "unit" : {"type": "string"}
                    },
                    "required": ["$oid"]
                }
            },
            "methods": {
                "type": "array",
                "items": {
                    "type": "object",
                    "maxProperties": 1,
                    "properties": {
                        "_id": {
                            "type": "object",
                            "properties": {
                                "$oid": {
                                    "type": "string"
                                }
                            }
                        },
                    },
                    "required": ["$oid"]
                }
            },
            "steps": {
                "type": "array",
                "items": {
                    "type": "object",
                    "maxProperties": 3,
                    "properties": {
                        "method": {
                            "type": "object",
                            "properties": {
                                "$oid": {
                                    "type": "string"
                                }
                            }
                        },
                        "parameters": {"type": "array",
                                       "items": {"type": ["number", "string", "boolean", "object"]}},
                        "used_ingredients": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "$oid": {"type": "string"}
                                },
                                "required": ["$oid"]
                            }
                        },
                        "used_products": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "recipe_index": {"type": "number"},
                                    "product_index": {"type": "number"}
                                },
                                "required": ["recipe_index"]
                            }
                        },
                        "product_name": {"type": "string"},
                        "info": {"type": "string"}
                    },
                    "required": ["$oid"]
                }
            },

        },
        "required": ["_id", "name","intro", "recipe_categories", "ingredients", "methods", "steps"]
    }

    recipe_category = {
        "title": "Recipe Category",
        "maxProperties": 3,
        "properties": {
            "_id": {
                "type": "object",
                "properties": {
                    "$oid": {
                        "type": "string"
                    }
                }
            },
            "name": {"type": "string"},
            "definition": {"type": "string"},
        },
        "required": ["_id", "name", "definition"]
    }