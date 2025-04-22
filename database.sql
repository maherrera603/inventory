DROP DATABASE IF EXISTS db_inventory;
CREATE DATABASE IF NOT EXISTS db_inventory;
USE db_inventory;

CREATE TABLE users(
    id INT( 255) auto_increment not null,
    name VARCHAR( 50) not null,
    lastname VARCHAR( 50 ) not null,
    idnumber VARCHAR( 10 ) NOT NULL,
    phone VARCHAR( 10 ) NOT NULL,
    email VARCHAR( 255 ) NOT NULL,
    password VARCHAR( 255 ) NOT NULL,
    role VARCHAR( 30 ) NOT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    CONSTRAINT pk_users PRIMARY KEY( id )
)ENGINE=InnoDb;

INSERT INTO `db_inventory`.`users` (`id`, `name`, `lastname`, `idnumber`, `phone`, `email`, `password`, `role`) VALUES ('1', 'nombre_user', 'apellidos_user', 'NoIdentificacion', 'telefono', 'email_admin', '$2b$12$7lcaKJDnt2TtRubIyT26C.q5inmMbX.E9QIQQaXjzDB6hJeZi8NEG', 'ADMIN_ROLE');

CREATE TABLE categories(
    id INT( 255 ) auto_increment not NULL,
    category VARCHAR( 255) NOT NULL,
    status VARCHAR( 100) NOT NULL,
    user INT( 255 ) NOT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    CONSTRAINT pk_category PRIMARY KEY( id ),
    CONSTRAINT fk_category_user FOREIGN KEY( user ) REFERENCES users( id )
)ENGINE=InnoDb;

CREATE TABLE products(
    id INT( 255 ) auto_increment not NULL,
    name VARCHAR( 255 ) NOT NULL,
    sku INT( 255 ) NOT NULL,
    category INT( 255 ) NOT NULL,
    quantity INT( 100 ) NOT NULL,
    price DECIMAL( 10, 2) NOT NULL,
    status VARCHAR( 100) NOT NULL,
    user INT( 255 ) NOT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    CONSTRAINT pk_product PRIMARY KEY( id ),
    CONSTRAINT fk_product_category FOREIGN KEY( category ) REFERENCES categories( id ),
    CONSTRAINT fk_product_user FOREIGN KEY( user ) REFERENCES users( id )
)ENGINE=InnoDb;

CREATE TABLE histories(
    id INT( 255 ) auto_increment not NULL,
    type VARCHAR( 100) NOT NULL,
    description TEXT NOT NULL,
    product INT( 255 ) NOT NULL,
    quantity INT( 100) NOT NULL,
    user INT( 255 ) NOT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    CONSTRAINT pk_history PRIMARY KEY( id ),
    CONSTRAINT fk_history_product FOREIGN KEY( product ) REFERENCES products( id ),
    CONSTRAINT fk_history_user FOREIGN KEY( user ) REFERENCES users( id)
)ENGINE=InnoDb;