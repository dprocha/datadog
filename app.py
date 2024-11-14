from datetime import datetime
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DATABASE = 'food_delivery.db'

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Endpoint to create a new order
@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    item_name = data.get('item_name')
    price = data.get('price')
    
    if not item_name or not price:
        return jsonify({"error": "Both 'item_name' and 'price' are required"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (item_name, price, order_time) VALUES (?, ?, ?)",
                   (item_name, price, datetime.now()))
    conn.commit()
    order_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"message": "Order created successfully", "order_id": order_id}), 201

# Endpoint to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    
    # Convert rows to a list of dictionaries
    orders_list = [dict(row) for row in orders]
    return jsonify(orders_list), 200

# Endpoint to get a single order by ID
@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
    order = cursor.fetchone()
    conn.close()
    
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    
    return jsonify(dict(order)), 200

# Endpoint to update an existing order by ID
@app.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    new_price = data.get('price')
    
    if new_price is None:
        return jsonify({"error": "'price' is required to update an order"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE orders SET price = ? WHERE order_id = ?", (new_price, order_id))
    conn.commit()
    conn.close()
    
    if cursor.rowcount == 0:
        return jsonify({"error": "Order not found"}), 404
    
    return jsonify({"message": "Order updated successfully"}), 200

# Endpoint to delete an order by ID
@app.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
    conn.commit()
    conn.close()
    
    if cursor.rowcount == 0:
        return jsonify({"error": "Order not found"}), 404
    
    return jsonify({"message": "Order deleted successfully"}), 200

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=8080, debug=True)