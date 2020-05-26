class Schemas:

    ingredient = {
        "title": "Ingredient",
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
        "required": ["name", "energy", "protein", "sugar", "fibre", "other_carbohydrates", "saturated_fat",
                     "polyunsaturated_fat", "monounsaturated_fat", "sodium", "belongs_categories"]
    }

    ingredient_category = {
        "title": "Ingredient Category",
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
        "required": ["name", "parent_category", "child_categories"]
    }

    method = {
        "title": "Method",
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
        "required": ["name", "belongs_categories", "definition", "parameters"]
    }

    method_category = {
        "title": "Method Category",
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
        "required": ["name", "definition"]
    }

    recipe = {}

    recipe_category = {
        "title": "Recipe Category",
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
        "required": ["name", "definition"]
    }