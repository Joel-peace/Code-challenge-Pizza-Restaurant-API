


# Pizza Restaurant API

A simple RESTful API built with Flask for managing restaurants, pizzas, and their menus.

## Requirements

- Python 3.8 or later
- pip

## Setup Instructions

### 1. Clone the Project

```bash
cd ~/Development/code/phase-4
git clone <your-repo-url> pizza-api-challenge
cd pizza-api-challenge
````

### 2. Create and Activate the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

Your terminal should now show:

```bash
(pizza-api-challenge)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Database Setup

### 1. Set Flask App

```bash
export FLASK_APP=server/app.py
```

### 2. Initialize and Migrate the Database

```bash
flask db init
flask db migrate -m "Initial setup"
flask db upgrade
```

### 3. Seed the Database

```bash
python server/seed.py
```

## Start the Server

```bash
flask run --port 5555
```

Visit:
[http://localhost:5555](http://localhost:5555)

## API Endpoints

### Restaurants

* `GET /restaurants`
* `GET /restaurants/<id>`
* `DELETE /restaurants/<id>`

### Pizzas

* `GET /pizzas`

### Add Pizza to a Restaurant

* `POST /restaurant_pizzas`

Example request:

```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

## Rules

* Pizza price must be between 1 and 30
* Restaurant names must be unique
* All fields are required in POST requests

## Example Errors

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

```json
{
  "error": "Restaurant not found"
}
```

## Test Commands (curl)

```bash
curl http://localhost:5555/restaurants

curl -X POST http://localhost:5555/restaurant_pizzas \
  -H "Content-Type: application/json" \
  -d '{"price": 10, "pizza_id": 2, "restaurant_id": 1}'

curl -X DELETE http://localhost:5555/restaurants/1
```

## Folder Structure

```
server/
├── app.py
├── config.py
├── seed.py
├── models/
│   ├── pizza.py
│   ├── restaurant.py
│   └── restaurant_pizza.py
└── controllers/
    ├── pizza_controller.py
    ├── restaurant_controller.py
    └── restaurant_pizza_controller.py
```

## Troubleshooting

Change the port if needed:

```bash
flask run --port 5556
```

Regenerate migrations if needed:

```bash
flask db migrate
flask db upgrade
```

Reactivate virtual environment if errors occur:

```bash
source venv/bin/activate
# Code-challenge-Pizza-Restaurant-API
