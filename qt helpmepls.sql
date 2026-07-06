CREATE DATABASE IF NOT EXISTS horizon;
USE horizon;
CREATE TABLE guys (id INT AUTO_INCREMENT PRIMARY KEY, login VARCHAR(50) UNIQUE, parol VARCHAR(255));
CREATE TABLE my_data (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), value VARCHAR(255), user_login VARCHAR(50));
INSERT INTO guys (login, parol) VALUES ('admin', '123');
INSERT INTO guys (login, parol) VALUES ('test', 'test');