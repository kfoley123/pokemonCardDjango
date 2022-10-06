# _Pokemon Card Database Backend_

A Django REST API that connects to a SQlite Database.

---

## Authors

Kortney Foley

---

## Technologies Used

-   Python
-   Django
-   Django REST Framework
-   SQlite DB

---

## Description

This project is paired with a frontend that can be accessed [here](https://github.com/kfoley123/pokemoncard_frontend)

The purpose of designing this Pokemon Card Collection app was to develop my back end and database creation skills. Original version of the app had full CRUD functionality so that a card could be updated, added or deleted, but it didn't make sense to keep all these functions for general users, so most of these have been removed or limited to "admin" account user.

The App allows users to view all Pokemon cards that have been added to the database, sort them by different filters (i.e type and/or specifc card set) and create a user if signed out. When signed in, users can create their own collections of cards.

TODO:

-   Add endpoint for Pokedex Index filtering

---

## Getting Started

### Front-End

Front end can be accessed [here](https://github.com/kfoley123/pokemoncard_frontend)

### Back-End

-   create python VENV of your choice
-   start python VENV
-   if not using provided database, run: manage.py migrate
-   to run server: manage.py runserver

---

## License

Copyright (c) _2022_ _Kortney Foley_
