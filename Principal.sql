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
  NOMBREPAIS VARCHAR(10) NOT NULL
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
  DESCRIPCION VARCHAR(100),
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
  CARDNUMBER INT,
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
    'Gratuita', 50001,1001,612.50,'Activa','2023-12-12','SAMSUNG GALAXY A70 SELLADO'),
    ('INSPIRON 3910: rendimiento y portabilidad. Procesador Intel Core i5 de 11.ª generación, pantalla de 15,6 pulgadas.',
    'Gratuita',50002,1002,800,'Activa','2022-10-23','DELL INSPIRON 3910 NUEVO'),
    ('La Nitro 5: rendimiento potente y diseño elegante. Procesador Intel Core i7 de 12.ª generación, tarjeta gráfica NVIDIA RTX 3060',
    'Gratuita',50003,1003,250,'Agotada','2019-11-11','XXXKIU DE OPORTUNIDAD'),
    ('Las Air Force 1: un clásico de la moda urbana. Diseño sencillo, comodidad inigualable.',
    'Gratuita',50004,1004),
    ('Las Forum Low: versátiles y combinables. Diseño retro, estilo minimalista.',
    'Gratuita',50005,1011),
    ('El Millennium Falcon: el set de Lego más grande de la historia. 7541 piezas, nave espacial a escala 1:144.',
    'Gratuita',50006,1012),
    ('La mesa Pycca: sencilla y elegante. Diseño moderno, construcción resistente.',
    'Gratuita',50007,1013),
    ('El iPhone 15 Pro Max: lo último en tecnología Apple. Pantalla OLED de 6,7 pulgadas, procesador A16 Bionic, cámara triple de 48MP.',
    'Gratuita',50008,1014),
    ('Los faros LED Philips: más visibilidad y seguridad. Iluminación potente y uniforme, diseño elegante.',
    'Gratuita',50009,1015),
    ('La cámara de reversa Anker: más seguridad al estacionar. Imágenes nítidas y claras, pantalla de 5 pulgadas.',
    'Gratuita',50010,1016);
    
    