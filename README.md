# Reciptory
Repository for standardized recipes with database for ingredients and cooking methods.

![Python](https://img.shields.io/badge/Python-v3.8.3-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask-v1.1.2-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Mongo](https://img.shields.io/badge/Mongo-v4.2.6-blue.svg?longCache=true&logo=mongoDB&style=flat-square&logoColor=white&colorB=47A248&colorA=4c566a)
![Vue](https://img.shields.io/badge/Vue-v2.6.11-blue.svg?longCache=true&logo=vue.js&style=flat-square&logoColor=white&colorB=4FC08D&colorA=4c566a)
![Bulma](https://img.shields.io/badge/Bulma-v0.8.2-blue.svg?longCache=true&logo=bulma&style=flat-square&logoColor=white&colorB=00D1B2&colorA=4c566a)

## Vision
Would it be nice if recipes were precise, well defined and standardized? You could understand any recipe straight away and find all the definitions for different cooking methods and dish categories. Recipes would be formatted with standardized language and there would be also possibility to find nutritional information for ingredients and recipes.

## REST API
As a Back-End solution there Python Flask with MongoDB. It contains also JSON schema validator functions, which make sure that there is no malformed documents going in. You can check the valid examples in `doc/database_examples.txt` Here you can see what urls are used.

`api/ingredient/` to GET all the ingredients or PUT a new one

`api/ingredient/<id>` to GET, PUT or DELETE a spesific ingredient

`api/ingredient_cateogry/` to GET all the ingredient categories or PUT a new one

`api/ingredient_cateogry/<id>` to GET, PUT or DELETE a spesific ingredient category

`api/method/` to GET all the cooking methods or PUT a new one

`api/method/<id>` to GET, PUT or DELETE a spesific cooking method

`api/method_category/` to GET all the cooking method categories or PUT a new one

`api/method_category/<id>` to GET, PUT or DELETE a spesific cooking method category

`api/recipe/` to GET all the recipes or PUT a new one

`api/recipe/<id>` to GET, PUT or DELETE a spesific recipe

`api/recipe_cateogory/` to GET all the recipe categories or PUT a new one

`api/recipe_cateogory/<id>` to GET, PUT or DELETE a spesific recipe category




## Front-End
This side of the project will be produced with Vue.js and Bulma. Neomorphism will be used to extend to style the Front-End.

