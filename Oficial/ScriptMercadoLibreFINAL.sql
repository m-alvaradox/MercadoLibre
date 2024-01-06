create database IF NOT EXISTS MercadoLibre;
use MercadoLibre;

-- Creacion de Tablas

CREATE TABLE IF NOT EXISTS USUARIO (
  USERID VARCHAR(50) PRIMARY KEY,
  PASS VARCHAR(16) NOT NULL,
  NOMBRE VARCHAR(10) NOT NULL,
  APELLIDO VARCHAR(10) NOT NULL,
  FECHANACIMIENTO DATE NOT NULL,
  ESCLIENTE BOOLEAN NOT NULL,
  ESVENDEDOR BOOLEAN NOT NULL,
  EMAIL VARCHAR(50) NOT NULL,
  TELEFONO VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS CLIENTE (
  USERID VARCHAR(50) PRIMARY KEY,
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID)
);

CREATE TABLE IF NOT EXISTS VENDEDOR (
  USERID VARCHAR(50) PRIMARY KEY,
   REPUTACION FLOAT DEFAULT NULL,
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID)
);

CREATE TABLE IF NOT EXISTS PAIS (
  COUNTRYID INT PRIMARY KEY,
  NOMBREPAIS VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS PROVINCIA (
  PROVID INT PRIMARY KEY,
  COUNTRYID INT NOT NULL,
  NOMBREPROVINCIA VARCHAR(20) NOT NULL,
  FOREIGN KEY (COUNTRYID) REFERENCES PAIS (COUNTRYID)
);

CREATE TABLE IF NOT EXISTS CIUDAD (
  CITYID INT PRIMARY KEY,
  NOMBRECIUDAD VARCHAR(50) NOT NULL,
  PROVID INT NOT NULL,
   SIGLAS VARCHAR(5) NOT NULL,
  FOREIGN KEY (PROVID) REFERENCES PROVINCIA (PROVID)
);

CREATE TABLE IF NOT EXISTS DIRECCION (
  ID INT auto_increment PRIMARY KEY,
  IDCIUDAD INT NOT NULL,
  USERID VARCHAR(50) NOT NULL,
  PARROQUIA VARCHAR(50) NOT NULL,
  REFERENCIAS VARCHAR(200) NOT NULL,
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID),
  FOREIGN KEY (IDCIUDAD) REFERENCES CIUDAD (CITYID)
);

CREATE TABLE IF NOT EXISTS PRODUCTO (
  PRODUCTID INT AUTO_INCREMENT PRIMARY KEY,
  NOMBRE VARCHAR(50) NOT NULL,
  MARCA VARCHAR(10),
  CATEGORIA VARCHAR(20),
  SUBCATEGORIA VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS PUBLICACION (
  NOPUBLICACION  int   AUTO_INCREMENT,
  DESCRIPCION VARCHAR(500),
  TIPOEXPOSICION ENUM('Gratuita','Clásica','Premium') NOT NULL,
  PRODUCTID INT,
  IDVENDEDOR VARCHAR(50),
  PRECIOVENTA FLOAT,
  ESTADO ENUM('Activa','Agotado','No Activa'),
  FECHAPUBLICACION DATE,
  NOMBREPUBLICACION VARCHAR(50),
  STOCK INT NOT NULL,
  PRIMARY KEY(NOPUBLICACION),
  FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTO (PRODUCTID),
  FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID)
);

CREATE TABLE IF NOT EXISTS VISUALIZACION_PUBLICACIONES (
  USERID VARCHAR(50),
  NOPUBLICACION  int,
  FECHA DATE,
  PRIMARY KEY (USERID, NOPUBLICACION),
  FOREIGN KEY (USERID) REFERENCES USUARIO (USERID),
  FOREIGN KEY (NOPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION)
);

CREATE TABLE IF NOT EXISTS PAGO (
  TRANSID INT PRIMARY KEY,
  METODO ENUM('Depósito','Crédito/Débito') NOT NULL,
  MONTO FLOAT NOT NULL,
  CUOTA INT NOT NULL,
  CARDNUMBER VARCHAR(20),
  IDCLIENTE VARCHAR(50) NOT NULL,
  FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID)
);

CREATE TABLE IF NOT EXISTS PREGUNTA (
  IDPREGUNTA int  AUTO_INCREMENT,
  CONTENIDO VARCHAR(50) NOT NULL,
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
  VECES INT NOT NULL,
  FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID)
);

CREATE TABLE IF NOT EXISTS ORDEN (
  ORDERID INT AUTO_INCREMENT PRIMARY KEY,
  FECHACREACION DATE NOT NULL,
  ESTADO ENUM('Pendiente','En curso','Completada') NOT NULL,
  CANTIDADPRODUCTO INT NOT NULL,
  IMPORTE FLOAT NOT NULL,
  COSTOENVIO FLOAT NOT NULL,
  FECHAENTREGA DATE,
  ESTRELLASPRODUCTO INT,
  ESTRELLASVENDEDOR INT,
  COMENTARIO VARCHAR(100),
  IDCUPON INT,
  PRODUCTID INT NOT NULL,
  IDPAGO INT NOT NULL UNIQUE,
  IDCLIENTE VARCHAR(50) NOT NULL,
  IDVENDEDOR VARCHAR(50) NOT NULL,
  IDDIRECCION INT,
  IDPUBLICACION INT NOT NULL,
  FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID),
  FOREIGN KEY (IDCUPON) REFERENCES CUPON (ID),
  FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTO (PRODUCTID),
  FOREIGN KEY (IDPAGO) REFERENCES PAGO (TRANSID),
  FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (IDDIRECCION) REFERENCES DIRECCION (ID),
  FOREIGN KEY (IDPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION)
);

CREATE TABLE IF NOT EXISTS RECLAMO (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  TIPO VARCHAR(20),
  ESTADO ENUM('Abierto','Cerrado'),
  CLIENTEID VARCHAR(50),
  VENDEDORID VARCHAR(50),
  ORDERID INT,
  FECHAINGRESO DATE NOT NULL,
  FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID),
  FOREIGN KEY (VENDEDORID) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (ORDERID) REFERENCES ORDEN (ORDERID)
);

CREATE TABLE IF NOT EXISTS FACTURA (
FACTID INT AUTO_INCREMENT PRIMARY KEY,
FECHA DATE,
DESCRIPCION VARCHAR(100),
IDVENDEDOR VARCHAR(50),
IDCLIENTE VARCHAR(50),
IDORDEN INT,
FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR(USERID),
FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE(USERID),
FOREIGN KEY (IDORDEN) REFERENCES ORDEN(ORDERID) 
);

-- Insercion Datos

insert into USUARIO values('ownyag','12345','Owen','Yagual','2002-01-10',true,true,'ownyag@live.com','0987654321'); 
insert into USUARIO values('malvaradox','54321','Mario','Alvarado','2003-11-14',true,true,'malvaradox@live.com','0912345678');
insert into USUARIO values('xavicam','aaaaa','Xavier','Camacho','2002-04-01',true,true,'xavicam@live.com','0913246587');
insert into USUARIO values('javirod','11111','Javier','Rodriguez','2005-03-01',true,true,'javirod@live.com','0915364875');
insert into USUARIO values('naybor','12222222','Nayeli','Borbor','2001-02-01',true,false,'naybor@live.com','0958455652');
insert into USUARIO values('luchoont','12229871','Luis','Ontaneda','1990-05-01',true,false,'luchont@yahoo.com','0985128912');
insert into USUARIO values('nickfigu','122253','Nick','Figueroa','2002-07-09',true,false,'nickfigur@hotmail.com','0921289128');
insert into USUARIO values('charlesrod','1256ga22','Carlos','Rodriguez','2010-05-12',true,false,'charlesrod@gmail.com','0989125982');
insert into USUARIO values('joelvill','1asdsa2222','Joel','Villon','2004-04-01',true,false,'joelvilla@gmail.com','0985181891');
insert into USUARIO values('angivel','122xv2092','Angie','Velastegui','2007-04-01',true,false,'angivel@live.com','0985181895');
insert into USUARIO values('angon','oiadsa','Angel','Ontaneda','2011-05-01',true,true,'angon@live.com','0923748372');
insert into USUARIO values('ferchon','5ioqw','Fernando','Chacon','2015-03-01',true,true,'ferchon@live.com','1234365465');
insert into USUARIO values('jorgquij','aasdaaaa','Jorge','Quijije','2002-09-01',true,true,'jorguijij@icloud.com','0998724354');
insert into USUARIO values('arperez','11ads','Ariana','Perez','2002-12-01',true,true,'arperez@live.com','3432345676');
insert into USUARIO values('fiotorres','1x23zx45','Fiorella','Torres','1980-05-07',true,true,'fiotorres@live.com','0983546753');
insert into USUARIO values('daniroca','5s43bcds21','Daniela','Roca','1980-10-05',true,true,'daniroca@outlook.es','0956473847');

insert into CLIENTE values
('ownyag'),('malvaradox'),('xavicam'),('javirod'),('naybor'),('luchoont'),('nickfigu'),('charlesrod'),('joelvill'),('angivel'),('angon'),('ferchon'),('jorgquij'),('arperez'),('fiotorres'),('daniroca');

insert into VENDEDOR(USERID) values
('ownyag'),('malvaradox'),('xavicam'),('javirod'),('angon'),('ferchon'),('jorgquij'),('arperez'),('fiotorres'),('daniroca');

insert into PAIS values
(901,'Ecuador'),(902,'Venezuela'),(903,'Colombia'),(904,'Brasil'),(905,'Uruguay'),
(906,'Chile'),(907,'Argentina'),(908,'Bolivia'),(909,'Paraguay'),(910,'México');

insert into PROVINCIA values
(801,901,'Guayas'),(802,902,'Zulia'),(803,903,'Bogotá'),(804,904,'Sao Paulo'),(805,905,'Montevideo'),(806,906,'Santiago'),
(807,907,'Buenos Aires'),(808,908,'La Paz'),(809,909,'Central'),(810,910,'Ciudad de México'),(811,901,'Pichincha'),
(812,901,'Manabí'),(813,901,'Santa Elena'),(814,901,'Esmeraldas');

insert into CIUDAD values
(701,'Guayaquil',801,'GYE'),(702,'Maracaibo',802,'MAR'),(703,'Bogotá',803,'BOG'),(704,'Sao Paulo',804,'SP'),
(705,'Montevideo',805,'MVO'),(706,'Santiago',806,'SGO'),(707,'Buenos Aires',807,'CABA'),(708,'La Paz',808,'LPZ'),(709,'Asunción',809,'ASUN'),
(710,'Ciudad de México',810,'CDMX'),(711,'Quito',811,'PQT'),(712,'Manta',812,'MNT'),(713,'Portoviejo',812,'PTV'),(714,'Salinas',813,'SLN'),(715,'Libertad',813,'LBT');

insert into DIRECCION (IDCIUDAD, USERID, PARROQUIA, REFERENCIAS) values 
(701,'ownyag','Rocafuerte','Avenida Rocafuerte Calle Escobedo 100 Parque de la Libertad'),
(701,'malvaradox','Carbo','Calle 9 de Octubre Calle 10 de Agosto 100 Malecón Simón Bolívar'),
(701,'xavicam','Urdesa','Avenida Las Américas Calle Francisco de Orellana 100 Parque Samanes'),
(711,'javirod','Centro Historico','Calle García Moreno Calle Sucre 100 Palacio de Carondelet'),
(711,'naybor','La Mariscal','Avenida 18 de Semptiembre Calle Reina Victoria 100 Plaza Foch'),
(711,'luchoont','El Ejido','Avenida de los Shyris Calle Colón 100 Parque El Ejido'),
(712,'nickfigu','Tarqui','Avenida 25 de Julio Calle 10 de Agosto 100 Parque de la madre'),
(713,'charlesrod','Portoviejo','Avenida 3 de Mayo Calle 28 de Agosto 100 Parque de la Ciudad'),
(714,'joelvill','San Lorenzo','Avenida 9 de Octubre Calle 10 de Agosto 100 Yatch Club'),
(715,'angivel','San Sebastian','Avenida Colombia Calle Estados Unidos 100 Refineria'),
(701,'malvaradox','Tarqui','La Vista Towers Edif. 8D 7A');

insert into PRODUCTO (NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA) values
    ('GALAXY A70','SAMSUNG','TECNOLOGIA','SMARTPHONES'),
    ('INSPIRON 3910','DELL','TECNOLOGIA','LAPTOPS'),
    ('XXKIU','ACER','TECNOLOGIA','LAPTOPS'),
    ('AIR FORCE 1','NIKE','DEPORTES','ZAPATILLAS'),
    ('FORUM LOW','ADIDAS','DEPORTES','ZAPATILLAS'),
    ('LEGO STAR WARS MILLENNIUM FALCON','LEGO','JUGUETES','ROMPECABEZAS'),
    ('MESA','PYCCA','HOGAR','MUEBLES'),
    ('IPHONE 15 PRO MAX','APPLE','TECNOLOGIA','SMARTPHONES'),
    ('KIT DE FAROS LED PARA AUTO','PHILIPS','AUTOS','ACCESORIOS'),
    ('CAMARA DE REVERSA CON PANTALLA','ANKER','AUTOS','ACCESORIOS'),
    ('SISTEMA DE AUDIO PARA AUTO','JBL','AUTOS','ACCESORIOS'),
    ('LEGO CREATOR 3 EN 1','LEGO','JUGUETES','ROMPECABEZAS');
    
    INSERT INTO PUBLICACION(DESCRIPCION,TIPOEXPOSICION,PRODUCTID,IDVENDEDOR,PRECIOVENTA,ESTADO,FECHAPUBLICACION,NOMBREPUBLICACION,STOCK) values
    ('El Galaxy S23: lo último en tecnología móvil. Pantalla AMOLED de 6,1 pulgadas, procesador Snapdragon 8 Gen 2, cámara de 50MP.',
    'Gratuita', 1,'ownyag',612.50,'Activa','2023-12-12','SAMSUNG GALAXY A70 SELLADO',2),
    ('INSPIRON 3910: rendimiento y portabilidad. Procesador Intel Core i5 de 11.ª generación, pantalla de 15,6 pulgadas.',
    'Gratuita',2,'malvaradox',800,'Activa','2022-10-23','DELL INSPIRON 3910 NUEVO',3),
    ('La Nitro 5: rendimiento potente y diseño elegante. Procesador Intel Core i7 de 12.ª generación, tarjeta gráfica NVIDIA RTX 3060',
    'Gratuita',3,'xavicam',250,'Activa','2019-11-11','XXXKIU DE OPORTUNIDAD',4),
    ('Las Air Force 1: un clásico de la moda urbana. Diseño sencillo, comodidad inigualable.',
    'Gratuita',4,'javirod',62.50,'Activa','2023-12-01','NKE AIR FORCE ONE',1),
    ('Las Forum Low: versátiles y combinables. Diseño retro, estilo minimalista.', 'Gratuita',5,'angon',210,
    'Activa','2022-11-11','ADIDAS FORUM LOW',5),
    ('El Millennium Falcon: el set de Lego más grande de la historia. 7541 piezas, nave espacial a escala 1:144.',
    'Gratuita',6,'ferchon',34.50,'Activa','2023-11-14','MILLENNIUM FALCOM APROVECHA',1),
    ('La mesa Pycca: sencilla y elegante. Diseño moderno, construcción resistente.',
    'Gratuita',7,'jorgquij',15.60,'Activa','2023-10-10','MESA PYCCA PARA LA FAMILIA',10),
    ('El iPhone 15 Pro Max: lo último en tecnología Apple. Pantalla OLED de 6,7 pulgadas, procesador A16 Bionic, cámara triple de 48MP.',
    'Gratuita',8,'arperez',1299.99,'Activa','2023-11-26','IPHONE 15 PRO MAX TRAIDA DESDE USA',5),
    ('Los faros LED Philips: más visibilidad y seguridad. Iluminación potente y uniforme, diseño elegante.',
    'Gratuita',9,'fiotorres',11.23,'Activa','2022-11-13','FAROS LED PHILLIPS',2),
    ('La cámara de reversa Anker: más seguridad al estacionar. Imágenes nítidas y claras, pantalla de 5 pulgadas.',
    'Gratuita',10,'daniroca',300,'Activa','2023-09-09','CAMARA REVERSA',8);
    
    INSERT INTO VISUALIZACION_PUBLICACIONES (NOPUBLICACION,USERID,FECHA) VALUES
	(1,'ownyag','2023-07-07'),(2,'malvaradox','2023-07-09'),(3,'xavicam','2023-07-12'),(4,'javirod','2023-07-15'),(5,'naybor','2023-08-16'),
    (2,'luchoont','2023-07-28'),(7,'nickfigu','2023-08-01'),(7,'charlesrod','2023-08-07'),(3,'joelvill','2023-08-12'),(8,'angivel','2023-08-15');
    
INSERT INTO PAGO(TRANSID,IDCLIENTE,MONTO,METODO,CARDNUMBER,CUOTA) VALUES
(3001,'ownyag',210,'Depósito','4XXX 2XXX 0X4X 8X56',1),
(3002,'malvaradox',612.50,'Crédito/Débito','5XX7 1X92 X075 3X12',1),
(3003,'xavicam',34.50,'Depósito','12X5 XXX0 7XX2 5XX0',1),
(3004,'javirod',22.46,'Crédito/Débito','9XXX 1528 43X6 2XX8',1),
(3005,'naybor',980,'Depósito','3156 X92X 7X08 74X5',1);

INSERT INTO PREGUNTA (IDCLIENTE, IDVENDEDOR, NOPUBLICACION,  CONTENIDO, TIEMPOENVIADO, FECHAHORARESPUESTA, MENSAJERESPUESTA) VALUES
  ('xavicam','arperez',8, '¿El producto incluye garantía?', '2023-12-07 21:30:00', '2023-12-07 21:40:00','Sí, todos nuestros productos tienen garantía de 1 año.'),
  ('luchoont','malvaradox',2,'¿Acepta transferencias por PagoMovil?','2023-12-23 07:15:00','2023-12-23 09:40:00','No amigo, solo tarjetas de credito'),
  ('nickfigu','malvaradox',2,'Tiene para colocar SIM fisico?','2023-12-23 10:10:10','2023-12-23 17:00:00','No, solo soporta ESIM que puede conseguir en Movistar'),
  ('joelvill','javirod',4,'Son originales?','2024-01-02 12:35:21','2024-01-03 13:15:33','Si, por que no?'),
  ('angivel','jorgquij',7,'Estan ubicados en Manta?','2023-12-27 12:00:00',NULL,NULL);
  
INSERT INTO CUPON VALUES
(4001,'DESCNAV',32,'2023-12-31','malvaradox',2),(4002,'DESCMAQ',35,'2024-02-15','xavicam',2),
(4003,'DESCDOG',20,'2024-01-03','naybor',2),(4004,'DESCCAT',30,'2023-12-31','nickfigu',2),
(4005,'DESCNPH',40,'2023-12-15','charlesrod',2), (4006, 'START2024',50,'2024-01-30','malvaradox',1);

INSERT INTO ORDEN (IDCUPON,PRODUCTID,IDPAGO,IDCLIENTE,IDVENDEDOR,IDDIRECCION,FECHACREACION,ESTADO,CANTIDADPRODUCTO,IMPORTE,COSTOENVIO,FECHAENTREGA,ESTRELLASPRODUCTO,ESTRELLASVENDEDOR,COMENTARIO,IDPUBLICACION) VALUES
(4001,1,3002,'malvaradox','ownyag',2,'2023-12-11','Completada',1,612.50,0,'2023-12-12',4,4,'Recibi en buenas condiciones pero muy tardado el envio',1),
(NULL,5,3001,'ownyag','angon',NULL,'2023-12-26','Completada',1,210,0,NULL,5,5,'Buena experiencia, gracias',5),
(NULL,6,3003,'xavicam','ferchon',NULL,'2023-12-21','Completada',1,34.50,0,NULL,4,4,NULL,6),
(NULL,9,3004,'javirod','fiotorres',NULL,'2023-12-15','Completada',2,22.46,0,NULL,5,5,'Me gusto, gracias',9),
(4003,1,3005,'naybor','ownyag',5,'2023-12-13','Completada',2,980,0,'2023-12-19',3,2,'Solo me llego una exijo una devolucion',1);

INSERT INTO RECLAMO (CLIENTEID,VENDEDORID,ORDERID,TIPO,FECHAINGRESO,ESTADO)VALUES
('malvaradox','ownyag',1,'RETRASO','2023-12-12','Cerrado'),
('naybor','ownyag',5,'FALLO ENTREGA','2023-12-19', 'Abierto');

INSERT INTO FACTURA (FECHA, DESCRIPCION, IDVENDEDOR, IDCLIENTE, IDORDEN) VALUES
('2023-12-14','COMPRA DE PRODUCTOS','ownyag','malvaradox',1);

-- TRIGGERS
DELIMITER $$
CREATE TRIGGER GENERARORDEN
BEFORE INSERT ON ORDEN
FOR EACH ROW BEGIN
UPDATE PUBLICACION
SET STOCK = STOCK - NEW.CANTIDADPRODUCTO
WHERE NOPUBLICACION = NEW.IDPUBLICACION;

UPDATE CUPON
SET VECES = VECES - 1
WHERE ID = NEW.IDCUPON;

END $$
DELIMITER $$

DELIMITER $$
CREATE TRIGGER ELIMINARDIRECCION
BEFORE DELETE ON DIRECCION
FOR EACH ROW BEGIN
UPDATE ORDEN
SET IDDIRECCION = NULL
WHERE IDDIRECCION = OLD.ID;

END $$
DELIMITER $$