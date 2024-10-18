-- This script creates a table named 'users' if it does not already exist.
-- The 'users' table has the following columns:
-- - id: An auto-incrementing integer that serves as the primary key.
-- - email: A unique, non-nullable VARCHAR field to store the user's email address.
-- - name: A VARCHAR field to store the user's name.
-- - country: An ENUM field with possible values 'US', 'CO', 'TN', defaulting to 'US' and not nullable.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
        PRIMARY KEY(id)
    );
