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

    recipe = {}

    ingredient_category = {}

    method = {}

    method_category = {}
