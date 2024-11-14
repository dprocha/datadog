# Food Delivery API Documentation

## Overview

This API allows you to create, retrieve, update, and delete food orders stored in an SQLite database. Each order includes an item name, price, and timestamp of the order.

## Base URL

- **Host**: `http://localhost:8080`

## Endpoints

### 1. `POST /order`

**Description**: Creates a new order with `item_name` and `price`.

- **URL**: `/order`
- **Method**: `POST`
- **Request Body**:
  - `item_name` (string, required): Name of the food item.
  - `price` (float, required): Price of the food item.

- **Response**:
  - **Status 201**:
    ```json
    {
      "message": "Order created successfully",
      "order_id": <new_order_id>
    }
    ```
  - **Status 400** (If required fields are missing):
    ```json
    {
      "error": "Both 'item_name' and 'price' are required"
    }
    ```

#### Example `curl` Command

```bash
curl -X POST http://localhost:8080/order \
     -H "Content-Type: application/json" \
     -d '{"item_name": "Burger", "price": 9.99}'
```

### 2. `GET /orders`

**Description**: Retrieves a list of all orders.

- **URL**: `/orders`
- **Method**: `GET`
- **Response**:
  - **Status 200**:
    ```json
    [
      {
        "order_id": 1,
        "item_name": "Burger",
        "price": 9.99,
        "order_time": "2023-11-08T12:34:56"
      },
      ...
    ]
    ```

#### Example `curl` Command

```bash
curl -X GET http://localhost:8080/orders
```

### 3. `GET /order/<order_id>`

**Description**: Retrieves a specific order by `order_id`.

- **URL**: `/order/<order_id>`
- **Method**: `GET`
- **Path Parameter**:
  - `order_id` (int): The ID of the order to retrieve.

- **Response**:
  - **Status 200**:
    ```json
    {
      "order_id": 1,
      "item_name": "Burger",
      "price": 9.99,
      "order_time": "2023-11-08T12:34:56"
    }
    ```
  - **Status 404** (If order is not found):
    ```json
    {
      "error": "Order not found"
    }
    ```

#### Example `curl` Command

```bash
curl -X GET http://localhost:8080/order/1
````

### 4. `PUT /order/<order_id>`

**Description**: Updates the price of an existing order.

- **URL**: `/order/<order_id>`
- **Method**: `PUT`
- **Path Parameter**:
  - `order_id` (int): The ID of the order to update.
- **Request Body**:
  - `price` (float, required): The new price of the food item.

- **Response**:
  - **Status 200**:
    ```json
    {
      "message": "Order updated successfully"
    }
    ```
  - **Status 400** (If `price` is missing):
    ```json
    {
      "error": "'price' is required to update an order"
    }
    ```
  - **Status 404** (If order is not found):
    ```json
    {
      "error": "Order not found"
    }
    ```

#### Example `curl` Command

```bash
curl -X PUT http://localhost:8080/order/1 \
     -H "Content-Type: application/json" \
     -d '{"price": 11.99}'
```

### 5. `DELETE /order/<order_id>`

**Description**: Deletes an order by `order_id`.

- **URL**: `/order/<order_id>`
- **Method**: `DELETE`
- **Path Parameter**:
  - `order_id` (int): The ID of the order to delete.

- **Response**:
  - **Status 200**:
    ```json
    {
      "message": "Order deleted successfully"
    }
    ```
  - **Status 404** (If order is not found):
    ```json
    {
      "error": "Order not found"
    }
    ```

#### Example `curl` Command

```bash
curl -X DELETE http://localhost:8080/order/1
```

### 5. `Database Setup`

To use the API, ensure the SQLite database and the orders table are set up. You can create the database and table by running the following commands:

```bash
./setup_orders_db.sh
```
