PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('3ad18f6d21c2');
CREATE TABLE IF NOT EXISTS "Clients" (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	phone VARCHAR NOT NULL, 
	birth_date DATE, 
	cc VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (cc)
);
INSERT INTO Clients VALUES(1,'Alex','1234567890',NULL,NULL);
CREATE TABLE facturas (
	id INTEGER NOT NULL, 
	phone VARCHAR NOT NULL, 
	name VARCHAR NOT NULL, 
	discount FLOAT, 
	payment_status BOOLEAN, 
	PRIMARY KEY (id)
);
INSERT INTO facturas VALUES(1,'1234567890','Alex',0.0,0);
CREATE TABLE products (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	image VARCHAR, 
	price FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO products VALUES(1,'Product_1','Url',20.0);
INSERT INTO products VALUES(2,'Product_2','Url',20.0);
INSERT INTO products VALUES(3,'Product_3','Url',20.0);
CREATE TABLE IF NOT EXISTS "facturaProducts" (
	id INTEGER NOT NULL, 
	factura_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	quantity INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(factura_id) REFERENCES facturas (id), 
	FOREIGN KEY(product_id) REFERENCES products (id)
);
INSERT INTO facturaProducts VALUES(1,1,1,3);
INSERT INTO facturaProducts VALUES(2,1,2,2);
COMMIT;
