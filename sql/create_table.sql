CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    domain TEXT NOT NULL,
    signup_date DATE NOT NULL
);
