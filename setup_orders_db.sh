#!/bin/bash

# Define the database name
DB_NAME="food_delivery.db"

# Create a new SQLite database and define the orders table schema (DDL)
sqlite3 $DB_NAME <<EOF
-- Drop the table if it already exists (to avoid duplicates if running the script multiple times)
DROP TABLE IF EXISTS orders;

-- Create the orders table with the specified schema
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    price REAL NOT NULL,
    order_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data into the orders table (DML)
INSERT INTO orders (item_name, price) VALUES ('Pizza', 12.99);
INSERT INTO orders (item_name, price) VALUES ('Burger', 8.49);
INSERT INTO orders (item_name, price) VALUES ('Pasta', 10.50);
INSERT INTO orders (item_name, price) VALUES ('Salad', 7.25);
INSERT INTO orders (item_name, price) VALUES ('Soda', 2.50);

-- Select all rows to verify the data was inserted
SELECT * FROM orders;
EOF

# Print a success message
echo "SQLite database '$DB_NAME' created with the 'orders' table and sample data."
