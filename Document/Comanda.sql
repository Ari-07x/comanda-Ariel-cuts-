-- Base de Datos Comanda Online Grupo 10 Rocket Team
-- Script de creación de la base de datos
-- Path: comanda.sql

-- Se crea la base de datos
CREATE DATABASE comanda; 
-- Se usa la base de datos
USE comanda;

-- Se crea la tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id_user INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80),
    email VARCHAR(80),
    password VARCHAR(80),
    role VARCHAR(20),
    phone VARCHAR(45),
    payment VARCHAR(45)
);

-- Se crea la tabla de negocios
CREATE TABLE IF NOT EXISTS business (
    id_business INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    address VARCHAR(255),
    phone VARCHAR(20),
    cuit VARCHAR(11),
    email VARCHAR(50),
    facebook VARCHAR(50),
    instagram VARCHAR(50),
    twitter VARCHAR(50)
);

-- Se crea la tabla de staff
CREATE TABLE IF NOT EXISTS staff (
id bigint unsigned not null primary key auto_increment,
shift VARCHAR(20),
id_user INT UNSIGNED NOT NULL,
id_business INT UNSIGNED NOT NULL,
FOREIGN KEY (id_user) REFERENCES `users` (`id_user`),
FOREIGN KEY (id_business) REFERENCES `business` (`id_business`)
);

-- Se crea la tabla de mesas
CREATE TABLE IF NOT EXISTS tables (
    id_table varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
    table_number INT NOT NULL UNIQUE,
    chairs INT,
    id_business INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id_table`),
    FOREIGN KEY (id_business) REFERENCES `business` (`id_business`)
);

-- Se crea la tabla de ordenes
CREATE TABLE IF NOT EXISTS orders (
    id_order INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    table_id VARCHAR(255),
    order_date datetime(6),
    FOREIGN KEY (table_id) REFERENCES `tables` (`id_table`)
);

-- Se crea la tabla de promociones
CREATE TABLE IF NOT EXISTS promo (
    id_promo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_date datetime(6),
    name VARCHAR(40),
    descriptions VARCHAR(255),
    sealing_price DECIMAL(2),
    status bit(1) DEFAULT NULL
);

-- Se crea la tabla unión de ordenes y promociones
CREATE TABLE IF NOT EXISTS promo_orders (
id bigint unsigned not null primary key auto_increment,
id_order INT UNSIGNED NOT NULL,
id_promo INT UNSIGNED NOT NULL,
FOREIGN KEY (id_order) REFERENCES `orders` (`id_order`),
FOREIGN KEY (id_promo) REFERENCES `promo` (`id_promo`)
);

-- Se crea la tabla de proveedores
CREATE TABLE IF NOT EXISTS supplier (
    id_supplier INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    address VARCHAR(255),
    phone VARCHAR(20),
    cuit VARCHAR(11),
    email VARCHAR(50),
    status bit(1) DEFAULT NULL
);

-- Se crea la tabla de productos
CREATE TABLE IF NOT EXISTS products (
    id_product INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    descriptions VARCHAR(255),
    sealing_price DECIMAL(2),
    cost_price DECIMAL(2),
	id_supplier INT  UNSIGNED NOT NULL,
	stock INT,
	status bit(1) DEFAULT NULL,
	FOREIGN KEY (id_supplier) REFERENCES `supplier` (`id_supplier`)
);

-- Se crea la tabla unión de ordenes y productos
CREATE TABLE IF NOT EXISTS products_orders (
id bigint unsigned not null primary key auto_increment,
id_product INT UNSIGNED NOT NULL,
id_order INT UNSIGNED NOT NULL,
FOREIGN KEY (id_order) REFERENCES `orders` (`id_order`),
FOREIGN KEY (id_product) REFERENCES `products` (`id_product`)
);

-- Se crea la tabla unión de promociones y productos
CREATE TABLE IF NOT EXISTS promo_products (
id bigint unsigned not null primary key auto_increment,
id_product INT UNSIGNED NOT NULL,
id_promo INT UNSIGNED NOT NULL,
FOREIGN KEY (id_promo) REFERENCES `promo` (`id_promo`),
FOREIGN KEY (id_product) REFERENCES `products` (`id_product`)
);

-- Se crea la tabla de reseñas
CREATE TABLE IF NOT EXISTS review (
    id_review INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    date_review datetime(6),
    email VARCHAR(50),
    review_text TEXT,
	rate INT,
	id_order INT UNSIGNED NOT NULL,
	FOREIGN KEY (id_order) REFERENCES `orders` (`id_order`)
);

-- Se crea la tabla de contactos
CREATE TABLE IF NOT EXISTS contact (
    id_contact INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    date_contact datetime(6),
    email VARCHAR(50),
    phone VARCHAR(20),
    contact_text TEXT,
	id_business INT UNSIGNED NOT NULL,
	FOREIGN KEY (id_business) REFERENCES `business` (`id_business`)
);

