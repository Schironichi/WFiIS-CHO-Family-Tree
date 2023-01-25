# WFiIS-CHO-Family-Tree
Family Tree Creator using Django and Neo4J Graph Database

## General description

It is a simple web application that represents a family tree. Each person has a basic information about them as well as closest family visible in both profile details and main page.
It is possible to add a new person and a relation between two people. Each person can be either married, parent or child of another person.

![graph](https://user-images.githubusercontent.com/57150634/214571293-e88ed6fa-21e7-4236-9000-bcf5f7168949.png)

Above picture shows a graph that was generated using data from this application's database.

The application was made using Django. To make the interface look pleasing, css styles and Bootstrap classes were added.
The graph database was hosted on the Neo4J AuraDB platform. The data was accessed using the neomodel library and the django-neomodel extension.
There are also files required to build the application on heroku.

## Screenshots

- Main Page:

![main_page](https://user-images.githubusercontent.com/57150634/214571407-854f0432-eb11-449d-adf5-600374a8a5cb.png)

- Profile:

![profile](https://user-images.githubusercontent.com/57150634/214571533-38d9a2db-7674-4294-bc4c-ed172a8fdbd3.png)

- New Relation Form:

![new_relation](https://user-images.githubusercontent.com/57150634/214571628-181f94ad-42a6-47ce-9ee3-ce176ce44a66.png)

- New Person Form:

![new_person](https://user-images.githubusercontent.com/57150634/214571694-740a5514-2fbc-4652-b757-2a94e3c96532.png)

- Remove Confirmation:

![remove](https://user-images.githubusercontent.com/57150634/214571759-efd7a434-1314-4287-9b7e-14c15b2d12a3.png)

## Genesis

The project was created for the subject Processing Data in Cloud Computing (Przetwarzanie danych w chmurach obliczeniowych) during the VII semester of studies.

## Bibliography

- [Corey Schafer's Python Django Tutorial series](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1)
