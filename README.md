# Guidelines for installing a flower online shop on your computer


## Requirements 

Installed python version 3

This service provides opportunity to add categories, flowers, events and reviews and manage users(Admin, Managers, Customers)

## Installation 
* Install virtual environment `pip install virtualenv`
* create virtual environment `virtalenv <enviroment name>`
* activate virtual environment
* Install all packages to your virtual environment `pip install -r requirements.txt`

Installation complete
#### Open project in your IDE
Go to file flowershop/flowershop/settings.py and look for Database settings. In this project I used **postgres**.
Install database with configurations in settings.

In terminal with activated environment type
`python manage.py makemigrations`

```python manage.py migrate```

```python manage.py runserver```

## Test in Postman

Install postman and use my postman collection to test all functionality
link to postman collection: `https://www.postman.com/collections/7a04e2add862bd0ad786` or use file **flowerShop.postman_collection.json**


##View logs
* In terminal you can logs or in file test_main.log