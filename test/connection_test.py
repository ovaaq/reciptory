# -*- coding: utf-8 -*-

# testing the instance of Connection class
from source.API import verify
from source.settings import Settings

settings = Settings()


test = {
    "name": "chicken",
    "parent_category": {
        "$oid": "5edaa2f5c9fabc0494de4333"
    },
    "child_categories": [{
            "$oid": "5eda9e7ea38fe3259ef3dc9b"
        },
        {
            "$oid": "5eda9e809724a58399b10f83"
        }
    ]
}

test2 = {
    "name": "chicken",
    "parent_category": {
        "$oid": "5edaa2f5c9fabc0494de4333"
    },
    "child_categories": [
    ]
}
settings.ingredient_category_col.add(test2)
#settings.ingredient_category_col.delete("5eda9e829063a7b05d288778")