# Gilded Rose API

## Requirements

- Python 2.7+
- pip
- Virtual Env

## Run Instructions

1. Create a virtual environment

    ````mkvirtualenv gilded-rose-matt-mccormick````
    
1. Install dependencies

    ````pip install -r requirements.txt````
    
1. Run API server

    ````python api.py````
        
1. Run tests

    ````python tests.py````
    
## Explanation
 
### Languages/Frameworks Chosen
 
I went with Python for the language simply because I've been programming with it the most lately and was most comfortable setting things up quickly.  
With Python, I've used both the Django and Flask frameworks.  For this simple task, I went with Flask-restful because it's a microframework and I didn't need to make use of more advanced functionality.
Flask-restful provides a simple way to create a RESTful API so that was a good choice for this project.
 
### API Data
 
The data is returned in JSON.  JSON is pretty standard for APIs so I thought it was a good choice.
 
#### GET /items
 
This route lists the inventory.
 
````curl http://127.0.0.1:5000/items````
    
##### Sample Response
   
````
[
  {
    "description": "Ergonomic chair",
    "id": 1,
    "name": "Chair",
    "price": 100
  },
  ...
]
````

#### POST /items/{id}/purchase

This route is where you can purchase an item.
Requires authorization.

In this task, the response will always be true.  Obviously, in a real application, I would want to check other things like the number of inventory in stock and whether we have the user's credit card on file or if they have enough credits to buy. 

````curl -X POST -H "Authorization: Token token1" http://127.0.0.1:5000/items/1/purchase````

##### Sample Response

````
{
  "success": true
}
````

### Authentication

Authentication uses the Authorization header along with a token.
I went with this for ease of use and used the Flask-HTTPAuth package which provides an easy way to do authentication.
Many API's will provide you with an API token so this would also be one authentication method when building an API.