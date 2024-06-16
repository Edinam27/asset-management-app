import sqlite3
import os

# Define the absolute path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'asset_management.db')

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create tables and view
cursor.executescript('''
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS assets (
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER,
    department_id INTEGER,
    location_id INTEGER,
    purchase_date TEXT,
    purchase_price REAL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE VIEW IF NOT EXISTS overview AS
SELECT 
    assets.asset_id,
    assets.name AS asset_name,
    categories.name AS category_name,
    departments.name AS department_name,
    locations.name AS location_name,
    assets.purchase_date,
    assets.purchase_price
FROM assets
JOIN categories ON assets.category_id = categories.category_id
JOIN departments ON assets.department_id = departments.department_id
JOIN locations ON assets.location_id = locations.location_id;
''')

# Insert default data
cursor.executescript('''
INSERT INTO categories (name) VALUES ('Electronics'), ('Furniture'), ('Vehicles')
ON CONFLICT(name) DO NOTHING;

INSERT INTO departments (name) VALUES ('IT'), ('HR'), ('Finance')
ON CONFLICT(name) DO NOTHING;

INSERT INTO locations (name) VALUES ('Head Office'), ('Warehouse'), ('Remote')
ON CONFLICT(name) DO NOTHING;
''')

conn.commit()
conn.close()
