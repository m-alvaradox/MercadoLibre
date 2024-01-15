create database IF NOT EXISTS MercadoLibre;
use MercadoLibre;

CREATE TABLE IF NOT EXISTS USUARIO (
  USERID VARCHAR(50) PRIMARY KEY,
  PASS VARCHAR(16) NOT NULL,
  NOMBRE VARCHAR(10) NOT NULL,
  APELLIDO VARCHAR(10) NOT NULL,
  FECHANACIMIENTO DATE NOT NULL,
  ESCLIENTE BOOLEAN NOT NULL,
  ESVENDEDOR BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS CLIENTE (
  USERID VARCHAR(50) PRIMARY KEY,
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID)
);

CREATE TABLE IF NOT EXISTS VENDEDOR (
  USERID VARCHAR(50) PRIMARY KEY,
   REPUTACION FLOAT,
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID)
);

CREATE TABLE IF NOT EXISTS PAIS (
  COUNTRYID INT PRIMARY KEY,
  NOMBREPAIS VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS PROVINCIA (
  PROVID INT PRIMARY KEY,
  COUNTRYID INT,
  NOMBREPROVINCIA VARCHAR(10) NOT NULL,
  FOREIGN KEY (COUNTRYID) REFERENCES PAIS (COUNTRYID)
);

CREATE TABLE IF NOT EXISTS CIUDAD (
  NOMBRECIUDAD VARCHAR(50) PRIMARY KEY,
  PROVID INT,
   SIGLAS VARCHAR(5),
  FOREIGN KEY (PROVID) REFERENCES PROVINCIA (PROVID)
);

CREATE TABLE IF NOT EXISTS DIRECCION (
  ID INT PRIMARY KEY,
  CIUDAD VARCHAR(50),
  USERID VARCHAR(50),
  PARROQUIA VARCHAR(50),
  REFERENCIAS VARCHAR(50),
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID),
  FOREIGN KEY (CIUDAD) REFERENCES CIUDAD (NOMBRECIUDAD)
);

CREATE TABLE IF NOT EXISTS TELEFONO (
  USERID VARCHAR(50) PRIMARY KEY,
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID),
  NUM_TELEFONO VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS PRODUCTO (
  PRODUCTID INT PRIMARY KEY,
  NOMBRE VARCHAR(10) NOT NULL,
  MARCA VARCHAR(10),
  CATEGORIA VARCHAR(10),
  SUBCATEGORIA VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS PUBLICACION (
  NOPUBLICACION  int   AUTO_INCREMENT,
  DESCRIPCION VARCHAR(100),
  TIPOEXPOSICION ENUM('Gratuita','Clásica','Premium') NOT NULL,
  PRODUCTID INT,
  IDVENDEDOR VARCHAR(50),
  PRIMARY KEY(NOPUBLICACION),
  FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTO (PRODUCTID),
  FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID)
);

CREATE TABLE IF NOT EXISTS IMAGEN_PUBLICACION (
  PUBID INT PRIMARY KEY,
  IMAGEURL VARCHAR(100) NOT NULL,
  FOREIGN KEY (PUBID) REFERENCES PUBLICACION (NOPUBLICACION)
);

CREATE TABLE IF NOT EXISTS VISUALIZACION_PUBLICACIONES (
  USERID VARCHAR(50),
  NOPUBLICACION  int,
  FECHA DATE,
  PRIMARY KEY (USERID, NOPUBLICACION),
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID),
  FOREIGN KEY (NOPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION)
);

CREATE TABLE IF NOT EXISTS DETALLECONTACTO (
  IDCLIENTE VARCHAR(50),
  IDVENDEDOR VARCHAR(50),
  IDPUBLICACION  int,
  MENSAJE VARCHAR(100),
  FECHAHORA DATETIME,
  PRIMARY KEY (IDCLIENTE, IDVENDEDOR, IDPUBLICACION),
  FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID),
   FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (IDPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION)
);

CREATE TABLE IF NOT EXISTS PAGO (
  TRANSID INT PRIMARY KEY,
  METODO ENUM('Depósito','Crédito/Débito') NOT NULL,
  MONTO FLOAT NOT NULL,
  CUOTA INT,
  CARDNUMBER VARCHAR(20),
  IDCLIENTE VARCHAR(50),
  FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID)
);

CREATE TABLE IF NOT EXISTS PREGUNTA (
  IDPREGUNTA int  AUTO_INCREMENT,
  CONTENIDO VARCHAR(30) NOT NULL,
  TIEMPOENVIADO DATETIME NOT NULL,
  FECHAHORARESPUESTA DATETIME,
  MENSAJERESPUESTA VARCHAR(100),
  IDCLIENTE VARCHAR(50),
  IDVENDEDOR VARCHAR(50),
  NOPUBLICACION  int,
  
  PRIMARY KEY(IDPREGUNTA),
  FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID),
  FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (NOPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION)
);

CREATE TABLE IF NOT EXISTS CUPON (
  ID INT PRIMARY KEY,
  NOMBRE VARCHAR(10) NOT NULL,
  DESCUENTO FLOAT NOT NULL,
  FECHAVENCIMIENTO DATE NOT NULL,
  CLIENTEID VARCHAR(50),
  FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID)
);

CREATE TABLE IF NOT EXISTS ORDEN (
  ORDERID INT PRIMARY KEY,
  FECHACREACION DATE NOT NULL,
  ESTADO ENUM('Pendiente','En curso','Completada') NOT NULL,
  CANTIDADPRODUCTO INT NOT NULL,
  IMPORTE FLOAT NOT NULL,
  COSTOENVIO FLOAT,
  FECHAENTREGA DATE,
  ESTRELLASPRODUCTO INT,
  ESTRELLASVENDEDOR INT,
  COMENTARIO VARCHAR(100),
  IDCUPON INT,
  PRODUCTID INT,
  IDPAGO INT,
  IDCLIENTE VARCHAR(50),
  IDVENDEDOR VARCHAR(50),
  IDDIRECCION INT,
  FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID),
  FOREIGN KEY (IDCUPON) REFERENCES CUPON (ID),
  FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTO (PRODUCTID),
  FOREIGN KEY (IDPAGO) REFERENCES PAGO (TRANSID),
  FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (IDDIRECCION) REFERENCES DIRECCION (ID)
);

CREATE TABLE IF NOT EXISTS RECLAMO (
  ID INT PRIMARY KEY,
  TIPO VARCHAR(10),
  ESTADO ENUM('Abierto','Cerrado'),
  CLIENTEID VARCHAR(50),
  VENDEDORID VARCHAR(50),
  ORDERID INT,
  FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID),
  FOREIGN KEY (VENDEDORID) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (ORDERID) REFERENCES ORDEN (ORDERID)
);