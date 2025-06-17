

# Pizza Restaurant API

A simple RESTful API built with Flask for managing restaurants, pizzas, and their menus.

---

## Setup Instructions

### 1. Clone the Project

```bash
cd ~/Development/code/phase-4
git clone https://github.com/user/repo.git pizza-api-challenge
cd pizza-api-challenge
```

### 2. Create and Activate the Virtual Environment

Create the virtual environment using `pipenv` and activate it:

```bash
pipenv install
pipenv shell
```

This will install the required dependencies and activate your virtual environment.

---

## Database Setup

### 1. Set the Flask App

```bash
export FLASK_APP=server/app.py
```

### 2. Install Specific Dependencies

Make sure the following dependencies are installed:

```bash
pipenv install Flask==2.3.3 Flask-Migrate==4.0.5 Flask-SQLAlchemy==3.1.1 SQLAlchemy==2.0.22
```

### 3. Seed the Database

```bash
python seed.py
```

---

## Start the Server

```bash
flask run --port 5555
```

Visit the API at:
[http://localhost:5555](http://localhost:5555)

---

## API Endpoints

### Restaurants

* `GET /restaurants`
* `GET /restaurants/<id>`
* `DELETE /restaurants/<id>`

### Pizzas

* `GET /pizzas`

### Add Pizza to a Restaurant

* `POST /restaurant_pizzas`

**Example Request Body:**

```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

---

## Example Error Responses

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

---

## Test Commands Using `curl`

### Get All Pizzas

```bash
curl http://127.0.0.1:5555/pizzas
```

### Get a Single Restaurant

```bash
curl http://127.0.0.1:5555/restaurants/1
```

### Add a Pizza to a Restaurant

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"price": 14, "pizza_id": 2, "restaurant_id": 2}' \
http://127.0.0.1:5555/restaurant_pizzas
```

### Delete a Restaurant

```bash
curl -X DELETE http://127.0.0.1:5555/restaurants/3
```

---

## Folder Structure

Include relevant directories such as:

```
.
├── server/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   └── ...
├── migrations/
├── instance/
├── seed.py
├── README.md
```

---

## Troubleshooting

* If port 5555 is in use, try running the server on a different port:

```bash
flask run --port 5556
```

* If database migrations are not working as expected, regenerate them:

```bash
flask db migrate
flask db upgrade
```


