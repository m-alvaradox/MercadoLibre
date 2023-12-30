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
  NOMBREPAIS VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS PROVINCIA (
  PROVID INT PRIMARY KEY,
  COUNTRYID INT,
  NOMBREPROVINCIA VARCHAR(20) NOT NULL,
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
  REFERENCIAS VARCHAR(200),
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

CREATE TABLE IF NOT EXISTS DETALLECONTACTO (
IDMENSAJE INT AUTO_INCREMENT,
  IDCLIENTE VARCHAR(50),
  IDVENDEDOR VARCHAR(50),
  IDPUBLICACION  int,
  MENSAJE VARCHAR(100),
  FECHAHORA DATETIME,
  PRIMARY KEY (IDMENSAJE, IDCLIENTE, IDVENDEDOR, IDPUBLICACION),
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
  TIPO VARCHAR(20),
  ESTADO ENUM('Abierto','Cerrado'),
  CLIENTEID VARCHAR(50),
  VENDEDORID VARCHAR(50),
  ORDERID INT,
  FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID),
  FOREIGN KEY (VENDEDORID) REFERENCES VENDEDOR (USERID),
  FOREIGN KEY (ORDERID) REFERENCES ORDEN (ORDERID)
);

CREATE TABLE IF NOT EXISTS FACTURA (
FACTID INT PRIMARY KEY,
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

insert into USUARIO values('ownyag','12345','Owen','Yagual','2002-01-10',true,true); 
insert into USUARIO values('malvaradox','54321','Mario','Alvarado','2003-11-14',true,true);
insert into USUARIO values('xavicam','aaaaa','Xavier','Camacho','2002-04-01',true,true);
insert into USUARIO values('javirod','11111','Javier','Rodriguez','2005-03-01',true,true);
insert into USUARIO values('naybor','12222222','Nayeli','Borbor','2001-02-01',true,false);
insert into USUARIO values('luchoont','12229871','Luis','Ontaneda','1990-05-01',true,false);
insert into USUARIO values('nickfigu','122253','Nick','Figueroa','2002-07-09',true,false);
insert into USUARIO values('charlesrod','1256ga22','Carlos','Rodriguez','2010-05-12',true,false);
insert into USUARIO values('joelvill','1asdsa2222','Joel','Villon','2004-04-01',true,false);
insert into USUARIO values('angivel','122xv2092','Angie','Velastegui','2007-04-01',true,false);
insert into USUARIO values('angon','oiadsa','Angel','Ontaneda','2011-05-01',false,true);
insert into USUARIO values('ferchon','5ioqw','Fernando','Chacon','2015-03-01',false,true);
insert into USUARIO values('jorgquij','aasdaaaa','Jorge','Quijije','2002-09-01',false,true);
insert into USUARIO values('arperez','11ads','Ariana','Perez','2002-12-01',false,true);
insert into USUARIO values('fiotorres','1x23zx45','Fiorella','Torres','1980-05-07',false,true);
insert into USUARIO values('daniroca','5s43bcds21','Daniela','Roca','1980-10-05',false,true);

insert into CLIENTE values
('ownyag'),('malvaradox'),('xavicam'),('javirod'),('naybor'),('luchoont'),('nickfigu'),('charlesrod'),('joelvill'),('angivel');

insert into VENDEDOR values
('ownyag',5),('malvaradox',5),('xavicam',4),('javirod',4.5),('angon',4.6),('ferchon',3),('jorgquij',2),('arperez',5),('fiotorres',1),('daniroca',2.7);

insert into PAIS values
(901,'Ecuador'),(902,'Venezuela'),(903,'Colombia'),(904,'Brasil'),(905,'Uruguay'),
(906,'Chile'),(907,'Argentina'),(908,'Bolivia'),(909,'Paraguay'),(910,'México');

insert into PROVINCIA values
(801,901,'Guayas'),(802,902,'Zulia'),(803,903,'Bogotá'),(804,904,'Sao Paulo'),(805,905,'Montevideo'),(806,906,'Santiago'),
(807,907,'Buenos Aires'),(808,908,'La Paz'),(809,909,'Central'),(810,910,'Ciudad de México'),(811,901,'Pichincha'),
(812,901,'Manabí'),(813,901,'Santa Elena'),(814,901,'Esmeraldas');

insert into CIUDAD values
('Guayaquil',801,'GYE'),('Maracaibo',802,'MAR'),('Bogotá',803,'BOG'),('Sao Paulo',804,'SP'),
('Montevideo',805,'MVO'),('Santiago',806,'SGO'),('Buenos Aires',807,'CABA'),('La Paz',808,'LPZ'),('Asunción',809,'ASUN'),
('Ciudad de México',810,'CDMX'),('Quito',811,'PQT'),('Manta',812,'MNT'),('Portoviejo',812,'PTV'),('Salinas',813,'SLN'),('Libertad',813,'LBT');

insert into DIRECCION values 
(2001,'Guayaquil','ownyag','Rocafuerte','Avenida Rocafuerte Calle Escobedo 100 Parque de la Libertad'),
(2002,'Guayaquil','malvaradox','Carbo','Calle 9 de Octubre Calle 10 de Agosto 100 Malecón Simón Bolívar'),
(2003,'Guayaquil','xavicam','Urdesa','Avenida Las Américas Calle Francisco de Orellana 100 Parque Samanes'),
(2004,'Quito','javirod','Centro Historico','Calle García Moreno Calle Sucre 100 Palacio de Carondelet'),
(2005,'Quito','naybor','La Mariscal','Avenida 18 de Semptiembre Calle Reina Victoria 100 Plaza Foch'),
(2006,'Quito','luchoont','El Ejido','Avenida de los Shyris Calle Colón 100 Parque El Ejido'),
(2007,'Manta','nickfigu','Tarqui','Avenida 25 de Julio Calle 10 de Agosto 100 Parque de la madre'),
(2008,'Portoviejo','charlesrod','Portoviejo','Avenida 3 de Mayo Calle 28 de Agosto 100 Parque de la Ciudad'),
(2009,'Salinas','joelvill','San Lorenzo','Avenida 9 de Octubre Calle 10 de Agosto 100 Yatch Club'),
(2010,'Libertad','angivel','San Sebastian','Avenida Colombia Calle Estados Unidos 100 Refineria');

insert into TELEFONO values
('ownyag',0987654321),('malvaradox',0912345678),('xavicam',0913246587),('javirod',0915364875),('naybor',0958455652),
('luchoont',0985128912),('nickfigu',0921289128),('charlesrod',0989125982),('joelvill',0985181891),('angivel',0985181895);

insert into PRODUCTO values
    (50001,'GALAXY A70','SAMSUNG','TECNOLOGIA','SMARTPHONES'),
    (50002,'INSPIRON 3910','DELL','TECNOLOGIA','LAPTOPS'),
    (50003,'XXKIU','ACER','TECNOLOGIA','LAPTOPS'),
    (50004,'AIR FORCE 1','NIKE','DEPORTES','ZAPATILLAS'),
    (50005,'FORUM LOW','ADIDAS','DEPORTES','ZAPATILLAS'),
    (50006,'LEGO STAR WARS MILLENNIUM FALCON','LEGO','JUGUETES','ROMPECABEZAS'),
    (50007,'MESA','PYCCA','HOGAR','MUEBLES'),
    (50008,'IPHONE 15 PRO MAX','APPLE','TECNOLOGIA','SMARTPHONES'),
    (50009,'KIT DE FAROS LED PARA AUTO','PHILIPS','AUTOS','ACCESORIOS'),
    (50010,'CAMARA DE REVERSA CON PANTALLA','ANKER','AUTOS','ACCESORIOS'),
    (50011,'SISTEMA DE AUDIO PARA AUTO','JBL','AUTOS','ACCESORIOS'),
    (50012,'LEGO CREATOR 3 EN 1','LEGO','JUGUETES','ROMPECABEZAS');
    
    INSERT INTO PUBLICACION(DESCRIPCION,TIPOEXPOSICION,PRODUCTID,IDVENDEDOR,PRECIOVENTA,ESTADO,FECHAPUBLICACION,NOMBREPUBLICACION) values
    ('El Galaxy S23: lo último en tecnología móvil. Pantalla AMOLED de 6,1 pulgadas, procesador Snapdragon 8 Gen 2, cámara de 50MP.',
    'Gratuita', 50001,'ownyag',612.50,'Activa','2023-12-12','SAMSUNG GALAXY A70 SELLADO'),
    ('INSPIRON 3910: rendimiento y portabilidad. Procesador Intel Core i5 de 11.ª generación, pantalla de 15,6 pulgadas.',
    'Gratuita',50002,'malvaradox',800,'Activa','2022-10-23','DELL INSPIRON 3910 NUEVO'),
    ('La Nitro 5: rendimiento potente y diseño elegante. Procesador Intel Core i7 de 12.ª generación, tarjeta gráfica NVIDIA RTX 3060',
    'Gratuita',50003,'xavicam',250,'Agotado','2019-11-11','XXXKIU DE OPORTUNIDAD'),
    ('Las Air Force 1: un clásico de la moda urbana. Diseño sencillo, comodidad inigualable.',
    'Gratuita',50004,'javirod',62.50,'Activa','2023-12-01','NKE AIR FORCE ONE'),
    ('Las Forum Low: versátiles y combinables. Diseño retro, estilo minimalista.', 'Gratuita',50005,'angon',210,
    'Activa','2022-11-11','ADIDAS FORUM LOW'),
    ('El Millennium Falcon: el set de Lego más grande de la historia. 7541 piezas, nave espacial a escala 1:144.',
    'Gratuita',50006,'ferchon',34.50,'Activa','2023-11-14','MILLENNIUM FALCOM APROVECHA'),
    ('La mesa Pycca: sencilla y elegante. Diseño moderno, construcción resistente.',
    'Gratuita',50007,'jorgquij',15.60,'Activa','2023-10-10','MESA PYCCA PARA LA FAMILIA'),
    ('El iPhone 15 Pro Max: lo último en tecnología Apple. Pantalla OLED de 6,7 pulgadas, procesador A16 Bionic, cámara triple de 48MP.',
    'Gratuita',50008,'arperez',1299.99,'Activa','2023-11-26','IPHONE 15 PRO MAX TRAIDA DESDE USA'),
    ('Los faros LED Philips: más visibilidad y seguridad. Iluminación potente y uniforme, diseño elegante.',
    'Gratuita',50009,'fiotorres',11.23,'Agotado','2022-11-13','FAROS LED PHILLIPS'),
    ('La cámara de reversa Anker: más seguridad al estacionar. Imágenes nítidas y claras, pantalla de 5 pulgadas.',
    'Gratuita',50010,'daniroca',300,'Activa','2023-09-09','CAMARA REVERSA');
    
    INSERT INTO VISUALIZACION_PUBLICACIONES (NOPUBLICACION,USERID,FECHA) VALUES
	(1,'ownyag','2023-07-07'),(2,'malvaradox','2023-07-09'),(3,'xavicam','2023-07-12'),(4,'javirod','2023-07-15'),(5,'naybor','2023-08-16'),
    (2,'luchoont','2023-07-28'),(7,'nickfigu','2023-08-01'),(7,'charlesrod','2023-08-07'),(3,'joelvill','2023-08-12'),(8,'angivel','2023-08-15');
    
    INSERT INTO DETALLECONTACTO (IDCLIENTE, IDVENDEDOR, IDPUBLICACION, MENSAJE, FECHAHORA) VALUES
  ('malvaradox','ownyag', 1,'Amigo, algun descuento?', '2023-12-07 14:30:00'),
  ('malvaradox', 'ownyag', 1,'No, amigo es fijo', '2023-12-07 14:35:00'),
  ('naybor','xavicam',3,'Hola, estoy interesado en el producto','2023-12-25 14:35:00'),
  ('naybor','xavicam',3,'Claro, te doy mi whatsapp: 09982736546','2023-12-27 14:35:00'),
  ('charlesrod','arperez',8,'No tiene el mismo iphone con mayor capacidad?','2023-12-24 23:00:00');

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
(4001,'DESCNAV',32,'2023-12-31','malvaradox'),(4002,'DESCMAQ',35,'2023-12-31','xavicam'),
(4003,'DESCDOG',20,'2023-12-25','naybor'),(4004,'DESCCAT',30,'2023-12-31','nickfigu'),
(4005,'DESCNPH',40,'2023-12-15','charlesrod');

INSERT INTO ORDEN (ORDERID,IDCUPON,PRODUCTID,IDPAGO,IDCLIENTE,IDVENDEDOR,IDDIRECCION,FECHACREACION,ESTADO,CANTIDADPRODUCTO,IMPORTE,COSTOENVIO,FECHAENTREGA,ESTRELLASPRODUCTO,ESTRELLASVENDEDOR,COMENTARIO) VALUES
(1234,4001,50001,3002,'malvaradox','ownyag',2002,'2023-12-11','Completada',1,612.50,0,'2023-12-12',4,4,'Recibi en buenas condiciones pero muy tardado el envio'),
(2232,NULL,50005,3001,'ownyag','angon',NULL,'2023-12-26','Completada',1,210,NULL,NULL,5,5,'Buena experiencia, gracias'),
(2132,NULL,50006,3003,'xavicam','ferchon',NULL,'2023-12-21','Completada',1,34.50,NULL,NULL,4,4,NULL),
(1235,NULL,50009,3004,'javirod','fiotorres',NULL,'2023-12-15','Completada',2,22.46,NULL,NULL,5,5,'Me gusto, gracias'),
(4444,4003,50001,3005,'naybor','ownyag',2005,'2023-12-13','Completada',2,980,0,'2023-12-19',3,2,'Solo me llego una exijo una devolucion');

INSERT INTO RECLAMO (ID,CLIENTEID,VENDEDORID,ORDERID,TIPO,ESTADO)VALUES
(7001,'malvaradox','ownyag',1234,'RETRASO','Cerrado'),
(7002,'naybor','ownyag',4444,'FALLO ENTREGA', 'Abierto');

INSERT INTO FACTURA VALUES
(8989,'2023-12-14','COMPRA DE PRODUCTOS','ownyag','malvaradox',1234);