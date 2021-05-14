# Guidelines for installing a flower online shop on your computer


## Requirements 

Installed python version 3

This is e-commerce backend for Flower shop based on **django, django rest-framework**. Service provides opportunity to add categories, flowers, events and reviews, manage them. Also you can manage users(Admins, Managers, Customers)

## Installation 
* Install virtual environment `pip install virtualenv`
* create virtual environment `virtalenv <enviroment name>`
* activate virtual environment
* Install all packages to your virtual environment `pip install -r requirements.txt`

Installation complete
#### Open project in your IDE
Go to file flowershop/flowershop/settings.py and look for Database settings. In this project I used **postgres**.
Setup database with configurations in settings.

In terminal with activated environment type

`python manage.py makemigrations`

```python manage.py migrate```

```python manage.py runserver```

## Test in Postman

Install postman and use my postman collection to test all functionality.

_link to postman collection:_ `https://www.postman.com/collections/7a04e2add862bd0ad786` or use file **flowerShop.postman_collection.json**


##View logs
* In terminal you can see logs or in file test_main.log