    -- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Insert default categories
INSERT INTO categories (name) VALUES 
('Electronics'), 
('Furniture'), 
('Vehicles');

-- Create departments table
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Insert default departments
DROP TABLE IF EXISTS departments;
INSERT INTO departments (name) 
VALUES 
('IT'), 
('HR'), 
('Finance'), 
('Faculty'),
('Transport'),
('Administration'),
('Management'),
('FACU')
;

-- Create locations table
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Insert default locations
INSERT INTO locations (name) 
VALUES 
('Central Admin'), 
('LBC Block'), 
('Graduate School'),
('Student Centre'),
('Library Complex'),
('Twin Towers'),
('Hostel A'),
('Hostel B'),
('Hostel C'),
('Clinic'),
('Auditorium'),
('Football Park')
;

-- Create assets table
DROP TABLE IF EXISTS assets;
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

-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER,
    transaction_date TEXT,
    department_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Insert a sample asset
INSERT INTO assets (name, category_id, department_id, location_id, purchase_date, purchase_price) 
VALUES 
('Macbook', 1, 1, 1, '2023-05-27', 10500.00),
('Chair', 2, 2, 2, '2023-05-27', 2500.00)
;

-- Create info table
CREATE TABLE IF NOT EXISTS info(
    overview_id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset_id INTEGER,
    category_id INTEGER,
    department_id INTEGER,
    location_id INTEGER,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Create overview view
CREATE VIEW IF NOT EXISTS overview AS
SELECT 
    assets.name AS asset_name,
    categories.name AS category_name,
    departments.name AS department_name,
    locations.name AS location_name
FROM assets
JOIN categories ON assets.category_id = categories.category_id
JOIN departments ON assets.department_id = departments.department_id
JOIN locations ON assets.location_id = locations.location_id;

SELECT * FROM assets;

SELECT * FROM overview;