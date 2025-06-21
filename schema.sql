-- Admins Table
CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    password VARCHAR(100)
);

-- Menu Items Table
CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Sample data
INSERT INTO menu_items (id, name, price) VALUES
(1, 'Chicken Wings', 300),
(2, 'Fries', 150),
(3, 'Soup', 200),
(4, 'Biryani', 250),
(5, 'Chicken Karahi', 800),
(6, 'Naan', 30),
(7, 'BBQ Platter', 1200),
(8, 'Kheer', 120),
(9, 'Gulab Jamun', 100),
(10, 'Ice Cream', 150),
(11, 'Soft Drink', 50),
(12, 'Lassi', 100),
(13, 'Tea', 40),
(14, 'Coffee', 70);

-- Orders Table
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    order_summary TEXT,
    total_price DECIMAL(10,2),
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
