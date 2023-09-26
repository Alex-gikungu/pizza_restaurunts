# Pizza Restaurant Flask API
This project implements a Flask API for managing pizza restaurants and their menus.

## Table of Contents
.Introduction
.Features
.Project Structure
.Setup and Installation
.Usage
.Endpoints
.License

## Introduction
This project is a Flask-based RESTful API that allows users to manage pizza restaurants and their menus. It includes functionality to create, read, update, and delete restaurants, as well as managing the associated pizzas.

## Features
- Create, read, update, and delete restaurants
- Get a list of all restaurants
- Get a specific restaurant by ID
- Get a list of all pizzas
- Create a new association between a pizza and a restaurant
- Perform validations on restaurant names and pizza prices


## Project Structure
The project structure is organized as follows:
- app.py: Main Flask application file.
- config.py: Configuration settings for the Flask app.
- models.py: Defines the database models and relationships.
- routes.py: Contains the API routes and their corresponding functionality.
- migrations/: Directory for database migrations.


## Setup and Installation

1.Clone the repository:
    ```bash 
    git clone https://github.com/your-username/pizza-restaurant-flask-api.git
     cd pizza-restaurant-flask-api

2.Initialize the database and apply migrations:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## Usage
flask run 

## Endpoints
- GET /restaurants: Get a list of all restaurants.
- GET /restaurants/:id: Get a specific restaurant by ID.
- DELETE /restaurants/:id: Delete a restaurant by ID.
- GET /pizzas: Get a list of all pizzas.
- POST /restaurant_pizzas: Create a new association between a pizza and a restaurant.


## License
