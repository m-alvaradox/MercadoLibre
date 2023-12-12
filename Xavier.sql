CREATE DATABASE IF NOT EXISTS mercado_libre;
USE DATABASE mercado_libre;
CREATE TABLE IF NOT EXISTS USUARIO (
  USER_ID INT PRIMARY KEY,
  PASSWORD VARCHAR(16) NOT NULL,
  NOMBRE VARCHAR(10) NOT NULL,
  APELLIDO VARCHAR(10) NOT NULL,
  FECHA_NACIMIENTO DATE NOT NULL,
  ES_CLIENTE BOOLEAN NOT NULL,
  ES_VENDEDOR BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS CLIENTE (
  USER_ID INT PRIMARY KEY,
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID)
);

CREATE TABLE IF NOT EXISTS VENDEDOR (
  USER_ID INT PRIMARY KEY,
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID),
  REPUTACION FLOAT
);

CREATE TABLE IF NOT EXISTS PAIS (
  COUNTRY_ID INT PRIMARY KEY,
  NOMBRE VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS PROVINCIA (
  PROV_ID INT PRIMARY KEY,
  COUNTRY_ID INT,
  FOREIGN KEY (COUNTRY_ID) REFERENCES PAIS (COUNTRY_ID),
  NOMBRE VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS CIUDAD (
  NOMBRE VARCHAR(50) PRIMARY KEY,
  PROV_ID INT,
  FOREIGN KEY (PROV_ID) REFERENCES PROVINCIA (PROV_ID),
  SIGLAS VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS DIRECCION (
  ID INT PRIMARY KEY,
  CIUDAD VARCHAR(50),
  USER_ID INT,
  PARROQUIA VARCHAR(50),
  CALLE VARCHAR(50),
  CALLE_SECUNDARIA VARCHAR(50),
  NUMERO_CALLE INT,
  REFERENCIA VARCHAR(50),
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID),
  FOREIGN KEY (CIUDAD) REFERENCES CIUDAD (NOMBRE)
);

CREATE TABLE IF NOT EXISTS TELEFONO (
  USER_ID INT PRIMARY KEY,
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID),
  NUM_TELEFONO VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS CATEGORIA_PRODUCTO (
  CATEGORIA INT PRIMARY KEY,
  SUBCATEGORIA VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS PRODUCTO (
  PRODUCT_ID INT PRIMARY KEY,
  NOMBRE VARCHAR(10) NOT NULL,
  MARCA VARCHAR(10),
  PRECIO FLOAT NOT NULL,
  CATEGORIA VARCHAR(10),
  FOREIGN KEY (CATEGORIA) REFERENCES CATEGORIA_PRODUCTO (CATEGORIA)
);

CREATE TABLE IF NOT EXISTS IMAGEN_PRODUCTO (
  PRODUCTO_ID INT PRIMARY KEY,
  FOREIGN KEY (PRODUCTO_ID) REFERENCES PRODUCTO (PRODUCT_ID),
  IMAGE_URL VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS INVENTARIO (
  ID INT PRIMARY KEY,
  CANTIDAD_STOCK INT NOT NULL
);

CREATE TABLE IF NOT EXISTS ALMACENAMIENTO (
  ID INT,
  PRODUCT_ID INT,
  PRIMARY KEY (ID, PRODUCT_ID),
  FOREIGN KEY (ID) REFERENCES INVENTARIO (ID),
  FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTO (PRODUCT_ID)
);

CREATE TABLE IF NOT EXISTS PUBLICACION (
  PUBLICACION AUTOINCREMENT PRIMARY KEY,
  DESCRIPCION VARCHAR(100),
  TIPO_EXPOSICION ENUM('Gratuita','Clásica','Premium') NOT NULL,
  PRODUCT_ID INT,
  ID_VENDEDOR INT,
  FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTO (PRODUCT_ID),
  FOREIGN KEY (ID_VENDEDOR) REFERENCES VENDEDOR (USER_ID)
);

CREATE TABLE IF NOT EXISTS VISUALIZACION_PUBLICACIONES (
  USER_ID INT,
  PUBLICACION AUTOINCREMENT,
  PRIMARY KEY (USER_ID, PUBLICACION),
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID),
  FOREIGN KEY (PUBLICACION) REFERENCES PUBLICACION (PUBLICACION),
  FECHA DATE
);

CREATE TABLE IF NOT EXISTS DETALLE_CONTACTO (
  CLIENTE_ID INT,
  PUBLICACION AUTOINCREMENT,
  PRIMARY KEY (CLIENTE_ID, PUBLICACION),
  FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTE (USER_ID),
  FOREIGN KEY (PUBLICACION) REFERENCES PUBLICACION (PUBLICACION),
  MENSAJE VARHCAR(100),
  FECHA_HORA DATETIME
);

CREATE TABLE IF NOT EXISTS PAGO (
  TRANSA_ID INT PRIMARY KEY,
  CLIENTE_ID INT,
  MONTO FLOAT NOT NULL,
  METODO ENUM('Depósito','Crédito/Débito') NOT NULL,
  CARD_NUMBER INT,
  CUOTA INT,
  FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTE (USER_ID)
);

CREATE TABLE IF NOT EXISTS PREGUNTA (
  PREGUNTA_ID AUTOINCREMENT PRIMARY KEY,
  CLIENTE_ID INT,
  PUBLICACION AUTOINCREMENT,
  CONTENIDO VARCHAR(30) NOT NULL,
  TIEMPO_ENVIADO DATETIME NOT NULL,
  FECHA_HORA_RESPUESTA DATETIME,
  MENSAJE_RESPUESTA VARCHAR(100),
  FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTE (USER_ID),
  FOREIGN KEY (PUBLICACION) REFERENCES PUBLICACION (PUBLICACION)
);

CREATE TABLE IF NOT EXISTS CUPON (
  ID INT PRIMARY KEY,
  NOMBRE VARCHAR(10) NOT NULL,
  DESCUENTO FLOAT NOT NULL,
  FECHA_VENCIMIENTO DATE NOT NULL,
  CLIENTE_ID INT,
  FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTE (USER_ID)
);

CREATE TABLE IF NOT EXISTS ORDEN (
  ORDEN_ID INT PRIMARY KEY,
  CUPON_ID INT,
  PRODUCT_ID INT,
  PAGO_ID INT,
  CALIFICACION INT,
  CLIENTE_ID INT,
  VENDEDOR_ID INT,
  DIRECCION_ID INT,
  FECHA_CREACION DATE NOT NULL,
  ESTADO ENUM('Pendiente','En curso','Completada') NOT NULL,
  CANTIDAD_PRODUCTO INT NOT NULL,
  PAGO_TOTAL FLOAT NOT NULL,
  COSTO_ENVIO FLOAT,
  FECHA_ENTREGA DATE
  FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTE (USER_ID),
  FOREIGN KEY (CUPON_ID) REFERENCES CUPON (ID),
  FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTO (PRODUCT_ID),
  FOREIGN KEY (PAGO_ID) REFERENCES PAGO (TRANSA_ID),
  FOREIGN KEY (CALIFICACION) REFERENCES CALIFICACION_ORDEN (CALIFICACION_ID),
  FOREIGN KEY (VENDEDOR_ID) REFERENCES VENDEDOR (USER_ID),
  FOREIGN KEY (DIRECCION_ID) REFERENCES DIRECCION (ID)
);

CREATE TABLE IF NOT EXISTS CALIFICACION_ORDEN (
  CALIFICACION_ID INT,
  ORDEN_ID INT,
  CLIENTE_ID INT,
  PRIMARY KEY (CALIFICACION_ID, CLIENTE_ID),
  FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTE (USER_ID),
  FOREIGN KEY (ORDEN_ID) REFERENCES ORDEN (ORDEN_ID),
  ESTRELLAS_PRODUCTO INT,
  COMENTARIO_PRODUCTO VARCHAR(30),
  CALIFICACION_VENDEDOR ENUM('Positiva','Neutral','Negativa'),
  FOTO_EVIDENCIA VARCHAR(50),
);

CREATE TABLE IF NOT EXISTS
