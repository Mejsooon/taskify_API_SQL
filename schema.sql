CREATE DATABASE IF NOT EXISTS task_tracker
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE task_tracker;


CREATE TABLE users (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    username        VARCHAR(50) NOT NULL UNIQUE,
    password_hash   VARCHAR(255) NOT NULL
);


CREATE TABLE tasks (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    user_id             INT NOT NULL,
    difficulty          TINYINT NOT NULL CHECK (difficulty BETWEEN 1 AND 10),
    description         TEXT NOT NULL,
    additional_notes    TEXT,
    status              ENUM('active', 'completed') NOT NULL DEFAULT 'active',

    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);