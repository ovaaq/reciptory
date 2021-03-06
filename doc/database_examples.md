## Ingredient

```json
{
    "_id": {
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
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
```

## Ingredient Category

```json

{
    "_id": {
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
    "name": "chicken",
    "parent_category": {
        "$oid": "5ebaa6ace1e9db12bc5fe71f"
    },
    "child_categories": [{
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
        {
            "$oid": "5ebaa74c00f2cddc8aa198de"
        }
    ]
}
```

## Method

```json
{    
    "_id": {
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
    "name": "roasting",
    "definition": "Roasting is a cooking method that uses dry heat 
    where hot air covers the food, cooking it evenly on all sides 
    with temperatures of at least 150 °C (300 °F) from an 
    open flame, oven, or other heat source.",
    "phrases": [
        "Roast $ingredient in the $p0 at $p1 $p2 for $p3 until $p4.",
        "Roast $ingredient in the $p0 at $p1 $p2 for $p3 
        until internal temperature reaches $p5 $p6."
    ],
    "parameters": [{
            "par_type": "option",
            "options": [
                "oven", "open flame", "baking oven", "pizza oven"
            ]
        },
        {
            "par_type": "number"
        },
        {
            "par_type": "option",
            "options": ["°C", "°F", "°K"]
        },
        {
            "par_type": "time"
        },
        {
            "par_type": "option",
            "options": ["well done", "medium", "browned"]
        },
        {
            "par_type": "number"
        },
        {
            "par_type": "option",
            "options": ["°C", "°F", "°K"]
        }
    ],
    "belongs_categories": [{
        "$oid": "5ebaa6ace1e9db12bc5fe71f"
    }]
}
```

## Method Category

```json
{
    "_id": {
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
    "name": "dry-heat",
    "definition": "Dry heat cooking refers to any cooking 
    technique where the heat is transferred to the food item without using 
    extra moisture. This method typically involves high temperatures 300 C or hotter."
}
```

## Recipe

```json
{
    "_id": {
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
    "name": "Pizza Dough",
    "authors": [{
        "$oid": "5ebaa6ace1e9db12bc5fe71f"
    }],
    "belongs_categories": [{
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
        {
            "$oid": "5ebaa74c00f2cddc8aa198de"
        }
    ],
    "ingredients": [{
            "$oid": "5ebaa6ace1e9db12bc5fe71f",
            "amount": 200.0,
            "measurement": "grams"
        },
        {
            "$oid": "5ebaa6ace1e9db12bc5fe71f",
            "amount": 200.0,
            "measurement": "grams"
        }
    ],
    "methods": [{
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
        {
            "$oid": "5ebaa74c00f2cddc8aa198de"
        }
    ],
    "steps": [{
            "method": {
                "$oid": "5ebaa6ace1e9db12bc5fe71f"
            },
            "method_params": ["00:23:23", "200", 3],
            "raw_ingredients": [1, 4],
            "end_products": [],
            "end_product": "dry ingredients",
            "additional_info": "Be careful with hot tools."
        },
        {
            "method": {
                "$oid": "5ebaa6ace1e9db12bc5fe71f"
            },
            "method_params": ["00:72:11", "smooth", 2, "kneeded"],
            "raw_ingredients": [2, 3],
            "end_products": [1],
            "end_product": "dough",
            "additional_info": "Work the dough"
        }
    ]
}
```

## Recipe Category

```json

{
    "_id": {
            "$oid": "5ebaa6ace1e9db12bc5fe71f"
        },
    "name": "dessert",
    "definition": "A usually sweet course or dish, as of 
    fruit, ice cream, or pastry, served at the end of a meal."
}
```
