use mercado_libre;

insert into USUARIO values
(1001,'12345','Owen','Yagual',04-10-2002,true,true),
(1002,'54321','Mario','Alvarado',14-11-2003,true,true),
(1003,'aaaaa','Xavier,Camacho',4-01-2002,true,true),
(1004,'11111','Javier','Rodriguez',02-05-2004,true,true),
(1005,'12222222','Nayeli','Borbor',15-02-2003,true,false),
(1006,'12229871','Luis','Ontaneda',01-01-2002,true,false),
(1007,'122253','Nick','Figueroa',13-09-2002,true,false),
(1008,'1256ga22','Carlos','Rodriguez',13-03-2002,true,false),
(1009,'1asdsa2222','Joel','Villon',23-06-2004,true,false),
(1010,'122xv2092','Angie','Velastegui',02-10-2001,true,false),
(1011,'oiadsa','Angel','Ontaneda',11-07-2003,false,true),
(1012,'5ioqw','Fernando','Chacon',20-03-1999,false,true),
(1013,'aasdaaaa','Jorge','Quijije',24-10-1983,false,true),
(1014,'11ads','Ariana','Perez',17-02-1997,false,true),
(1015,'1x23zx45','Fiorella','Torres',05-05-1990,false,true),
(1016,'5s43bcds21','Daniela','Roca',06-09-2001,false,true);


insert into CLIENTE values
(1001),(1002),(1003),(1004),(1005),(1006),(1007),(1008),(1009),(1010);

insert into VENDEDOR values
(1001),(1002),(1003),(1004),(1011),(1012),(1013),(1014),(1015),(1016);

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
(2001,'Guayaquil',1001,'Rocafuerte','Avenida Rocafuerte','Calle Escobedo',100,'Parque de la Libertad'),
(2002,'Guayaquil',1002,'Carbo','Calle 9 de Octubre','Calle 10 de Agosto',100,'Malecón Simón Bolívar'),
(2003,'Guayaquil',1003,'Urdesa','Avenida Las Américas','Calle Francisco de Orellana',100,'Parque Samanes'),
(2004,' Quito',1004,'Centro Historico','Calle García Moreno','Calle Sucre',100,'Palacio de Carondelet'),
(2005,'Quito',1005,'La Mariscal','Avenida 18 de Semptiembre','Calle Reina Victoria',100,'Plaza Foch'),
(2006,'Quito',1006,'El Ejido','Avenida de los Shyris','Calle Colón',100,'Parque El Ejido'),
(2007,'Manta',1007,'Tarqui','Avenida 25 de Julio','Calle 10 de Agosto',100,'Parque de la madre'),
(2008,'Portoviejo',1008,'Portoviejo','Avenida 3 de Mayo','Calle 28 de Agosto',100,'Parque de la Ciudad'),
(2009,'Salinas',1009,'San Lorenzo','Avenida 9 de Octubre','Calle 10 de Agosto',100,'Yatch Club'),
(2010,'Libertad',1010,'San Sebastian','Avenida Colombia','Calle Estados Unidos',100,'Refineria');

insert into TELEFONO values
(1001,0987654321),(1002,0912345678),(1003,0913246587),(1004,0915364875),(1005,0958455652),
(1006,0985128912),(1007,0921289128),(1008,0989125982),(1009,0985181891),(1010,0985181895);


insert into PRODUCTO values
    (50001,'Smartphone','Samsung''ELECTRONICA','Celulares'),
    (50002,'Laptop','Asus','TECNOLOGIA','Laptops'),
    (50003,'Laptop','Acer','TECNOLOGIA','Laptops'),
    (50004,'Air force 1','Nike','DEPORTES','Zapatillas'),
    (50005,'Forum Low','Adidas','DEPORTES','Zapatillas'),
    (50006,'Lego Star Wars Millennium Falcon','Lego','JUGUETES','LEGOS'),
    (50007,'Mesa','Pycca','HOGAR','MUEBLES'),
    (50008,'Iphone 15 Pro Max','Apple','ELECTRONICA','CELULARES'),
    (50009,'Kit de faros LED para auto','Philips','AUTOS','ACCESORIOS'),
    (50010,'Cámara de reversa con pantalla','Anker','AUTOS','ACCESORIOS'),
    (50011,'Sistema de audio para auto','JBL','AUTOS','ACCESORIOS'),
    (50012,'Lego Creator 3 en 1','Lego','JUGUETES','LEGOS');

INSERT INTO PUBLICACION(DESCRIPCION,TIPO_EXPOSICION,PRODUCT_ID,ID_VENDEDOR) values
    ('El Galaxy S23: lo último en tecnología móvil. Pantalla AMOLED de 6,1 pulgadas, procesador Snapdragon 8 Gen 2, cámara de 50MP.',
    'Gratuita', 50001,1001),
    ('La VivoBook 15: rendimiento y portabilidad. Procesador Intel Core i5 de 11.ª generación, pantalla de 15,6 pulgadas.',
    'Gratuita',50002,1002),
    ('La Nitro 5: rendimiento potente y diseño elegante. Procesador Intel Core i7 de 12.ª generación, tarjeta gráfica NVIDIA RTX 3060',
    'Gratuita',50003,1003),
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

INSERT INTO IMAGEN_PUBLICACION values
    (1,'imagen01.jpg'),(2,'imagen02.jpg'),(3,'imagen03.jpg'),(4,'imagen04.jpg'),(5,'imagen05.jpg'),
    (6,'imagen06.jpg'),(7,'imagen07.jpg'),(8,'imagen08.jpg'),(9,'imagen09.jpg'),(10,'imagen10.jpg');
    
INSERT INTO VISUALIZACION_PUBLICACIONES(USERID,FECHA) VALUES
	(1001,'2023-07-07'),(1002,'2023-07-09'),(1003,'2023-07-12'),(1004,'2023-07-15'),(1005,'2023-08-16'),
    (1006,'2023-07-28'),(1007,'2023-08-01'),(1008,'2023-08-07'),(1009,'2023-08-12'),(1010,'2023-08-15');

INSERT INTO DETALLE_CONTACTO (CLIENTE, MENSAJE, FECHA_HORA) VALUES
  ('1001', 'Buena experiencia de compra, el producto llegó a tiempo.', '2023-12-07 14:30:00'),
  ('1002', 'Producto defectuoso, el vendedor no respondió a tiempo.', '2023-12-07 15:45:00'),
  ('1003', 'Excelente servicio al cliente, resolvieron mi problema rápidamente.', '2023-12-07 16:20:00'),
  ('1004', 'Demora en la entrega, pero el vendedor se disculpó y ofreció descuento.', '2023-12-07 17:10:00'),
  ('1005', 'Producto recibido en perfecto estado, lo recomiendo.', '2023-12-07 18:00:00'),
  ('1006', 'Problemas de comunicación con el vendedor, no recomiendo.', '2023-12-07 18:45:00'),
  ('1007', 'Entrega rápida y vendedor amable, muy satisfecho.', '2023-12-07 19:30:00'),
  ('1008', 'Producto diferente al anunciado, espero una solución.', '2023-12-07 20:15:00'),
  ('1009', 'Reembolso procesado rápidamente, buen servicio.', '2023-12-07 21:00:00'),
  ('1010', 'Vendedor no respondió a mis mensajes, mala experiencia.', '2023-12-07 21:45:00');

INSERT INTO PAGO VALUES
(3001,'1001',200.50,'Depósito','51XX 8XX837 67XX9',1),
(3002,'1002',38.75,'Crédito/Débito','65XX 9XX123 27XX6',1),
(3003,'1003',20.00,'Depósito','23XX 5XX837 78XX3',1),
(3004,'1004',45.50,'Crédito/Débito','15XX 3XX837 21XX2',1),
(3005,'1005',150.00,'Depósito','36XX 8XX721 67XX9',1),
(3006,'1006',124.50,'Depósito','12XX 6XX879 75XX5',1),
(3007,'1007',78.25,'Crédito/Débito','52XX 8XX866 77XX3',1),
(3008,'1008',360.00,'Depósito','21XX 1XX127 63XX3',1),
(3009,'1009',44.50,'Depósito','96XX 9XX478 22XX1',1),
(3010,'1010',24.99,'Depósito','87XX 1XX329 74XX1',1);

INSERT INTO PREGUNTA (CLIENTE_ID, CONTENIDO, TIEMPO_ENVIADO, FECHA_HORA_RESPUESTA, MENSAJE_RESPUESTA) VALUES
  ('1001', '¿Cuándo expira la oferta?', '2023-12-07 21:00:00', 'La oferta expira en 3 días.'),
  ('1002', '¿Hacen envíos internacionales?', '2023-12-07 21:15:00', 'Sí, hacemos envíos a nivel internacional.'),
  ('1003', '¿El producto incluye garantía?', '2023-12-07 21:30:00', 'Sí, todos nuestros productos tienen garantía de 1 año.'),
  ('1004', '¿Puedo devolver el artículo si no estoy satisfecho?', '2023-12-07 21:45:00', 'Sí, aceptamos devoluciones dentro de los 30 días posteriores a la compra.'),
  ('1005', '¿Tienen descuentos para compras al por mayor?', '2023-12-07 22:00:00', 'Sí, ofrecemos descuentos para compras al por mayor'),
  ('1006', '¿Cuánto tiempo demora el envío?', '2023-12-07 22:15:00', 'El envío demora aproximadamente de 3 a 5 días hábiles.'),
  ('1007', '¿Hay opciones de pago a plazos?', '2023-12-07 22:30:00', 'Sí, ofrecemos opciones de pago a plazos.'),
  ('1008', '¿El producto viene con manual de instrucciones?', '2023-12-07 22:45:00', 'Sí, incluimos un manual de instrucciones con cada producto.'),
  ('1009', '¿Hay descuentos para estudiantes?', '2023-12-07 23:00:00', 'Actualmente no ofrecemos descuentos específicos para estudiantes'),
  ('1010', '¿Este modelo está disponible en otros colores?', '2023-12-07 23:15:00', 'Sí, este modelo está disponible en varios colores.');

INSERT INTO CUPON VALUES
(4001,'DESCNAV',32,'2023-12-31','1001'),(3002,'DESCMAQ',35,'2023-12-31','1002'),
(4003,'DESCDOG',20,'2023-12-25','1003'),(3004,'DESCCAT',30,'2023-12-31','1004'),
(4005,'DESCNAV',40,'2023-12-15','1005'),(3006,'DESCLOV',30,'2023-12-25','1006'),
(4007,'DESCESC',25,'2023-12-25','1007'),(3008,'DESCBEB',15,'2023-12-31','1008'),
(4009,'DESCOMI',20,'2023-12-31','1009'),(3010,'DESCELE',10,'2023-12-31','1010');

INSERT INTO ORDEN VALUES
(5001, 4001, 50001, 3001, 6001, '1001', '1002', 2001, '2023-12-01', 'Completada', 1, 222.50, 5.00, '2023-12-8'),
(5002, 4001, 50001, 3001, 6002, '1002', '1003', 2002, '2023-12-02', 'Completada', 1, 56.00, 4.00, '2023-12-9'),
(5003, 4001, 50001, 3001, 6003, '1003', '1004', 2003, '2023-12-03', 'Completada', 1, 12.00, 2.00, '2023-12-10'),
(5004, 4001, 50001, 3001, 6004, '1004', '1001', 2004, '2023-12-04', 'Completada', 1, 40.50, 5.00, '2023-12-11'),
(5005, 4001, 50001, 3001, 6005, '1005', '1001', 2005, '2023-12-05', 'En curso', 1, 60.00, 3.00, '2023-12-15'),
(5006, 4001, 50001, 3001, 6006, '1006', '1002', 2006, '2023-12-06', 'En curso', 1, 70.00, 5.00, '2023-12-15'),
(5007, 4001, 50001, 3001, 6007, '1007', '1003', 2007, '2023-12-07', 'En curso', 1, 30.50, 5.00, '2023-12-16'),
(5008, 4001, 50001, 3001, 6008, '1008', '1004', 2008, '2023-12-08', 'En curso', 1, 10.00, 0.00, '2023-12-17'),
(5009, 4001, 50001, 3001, 6009, '1009', '1001', 2009, '2023-12-09', 'En curso', 1, 33.50, 5.00, '2023-12-18'),
(5010, 4001, 50001, 3001, 6010, '1010', '1001', 2010, '2023-12-10', 'En curso', 1, 112.00, 5.00, '2023-12-19');

INSERT INTO CALIFICACION_ORDEN VALUES
(6001,5001,'1001',5,'Buena atención','Positiva','http://example.com/img/1.jpg'),
(6002,5002,'1002',4,'Entrega rápida','Positiva','http://example.com/img/2.png'),
(6003,5003,'1003',5,'Buena calidad','Positiva','http://example.com/img/3.jpeg'),
(6004,5004,'1004',4,'Atención rápida','Positiva','http://example.com/img/4.gif'),
(6005,5005,'1005',3,'Demora en entrega','Neutral','http://example.com/img/5.jpg'),
(6006,5006,'1006',2,'Pésima atención','Negativa','http://example.com/img/6.png'),
(6007,5007,'1007',1,'Producto en malas condiciones','Negativa','http://example.com/img/7.jpeg'),
(6008,5008,'1008',4,'Cumple lo que promete','Positiva','http://example.com/img/8.gif'),
(6009,5009,'1009',4,'Atención rápida','Positiva','http://example.com/img/9.jpg'),
(6010,5010,'1010',5,'Buena atención','Positiva','http://example.com/img/10.png');

INSERT INTO RECLAMO VALUES
(7001,'1001',5001,'RETRASO','Cerrado'),
(7002,'1002',5002,'ATENCION','Abierto'),
(7003,'1003',5003,'PRODUCTO','Cerrado'),
(7004,'1004',5004,'PRODUCTO','Cerrado'),
(7005,'1005',5005,'PRODUCTO','Cerrado'),
(7006,'1006',5006,'ATENCION','Abierto'),
(7007,'1007',5007,'ATENCION','Abierto'),
(7008,'1008',5008,'RETRASO','Cerrado'),
(7009,'1009',5009,'PRODUCTO','Cerrado'),
(7010,'1010',5010,'PRODUCTO','Cerrado');

