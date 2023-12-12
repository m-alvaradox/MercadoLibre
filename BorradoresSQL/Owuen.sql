use mercado_libre;

insert into USUARIO values(1001,'12345','Owen','Yagual',04-10-2002,true,true);
insert into USUARIO values(1002,'54321','Mario','Alvarado',14-11-2003,true,true);
insert into USUARIO values(1003,'aaaaa','Xavier,Camacho',4-01-2002,true,true);
insert into USUARIO values(1004,'11111','Javier','Rodriguez',02-05-2004,true,true);
insert into USUARIO values(1005,'12222222','Nayeli','Borbor',15-02-2003,true,false);
insert into USUARIO values(1006,'12229871','Luis','Ontaneda',01-01-2002,true,false);
insert into USUARIO values(1007,'122253','Nick','Figueroa',13-09-2002,true,false);
insert into USUARIO values(1008,'1256ga22','Carlos','Rodriguez',13-03-2002,true,false);
insert into USUARIO values(1009,'1asdsa2222','Joel','Villon',23-06-2004,true,false);
insert into USUARIO values(1010,'122xv2092','Angie','Velastegui',02-10-2001,true,false);
insert into USUARIO values(1011,'oiadsa','Angel','Ontaneda',11-07-2003,false,true);
insert into USUARIO values(1012,'5ioqw','Fernando','Chacon',20-03-1999,false,true);
insert into USUARIO values(1013,'aasdaaaa','Jorge','Quijije',24-10-1983,false,true);
insert into USUARIO values(1014,'11ads','Ariana','Perez',17-02-1997,false,true);
insert into USUARIO values(1015,'1x23zx45','Fiorella','Torres',05-05-1990,false,true);
insert into USUARIO values(1016,'5s43bcds21','Daniela','Roca',06-09-2001,false,true);


insert into CLIENTE values(1001);
insert into CLIENTE values(1002);
insert into CLIENTE values(1003);
insert into CLIENTE values(1004);
insert into CLIENTE values(1005);
insert into CLIENTE values(1006);
insert into CLIENTE values(1007);
insert into CLIENTE values(1008);
insert into CLIENTE values(1009);
insert into CLIENTE values(1010);

insert into VENDEDOR values(1001);
insert into VENDEDOR values(1002);
insert into VENDEDOR values(1003);
insert into VENDEDOR values(1004);
insert into VENDEDOR values(1011);
insert into VENDEDOR values(1012);
insert into VENDEDOR values(1013);
insert into VENDEDOR values(1014);
insert into VENDEDOR values(1015);
insert into VENDEDOR values(1016);

insert into PAIS values(901,'Ecuador');
insert into PAIS values(902,'Venezuela');
insert into PAIS values(903,'Colombia');
insert into PAIS values(904,'Brasil');
insert into PAIS values(905,'Uruguay');
insert into PAIS values(906,'Chile');
insert into PAIS values(907,'Argentina');
insert into PAIS values(908,'Bolivia');
insert into PAIS values(909,'Paraguay');
insert into PAIS values(910,'México');

insert into PROVINCIA values(801,901,'Guayas');
insert into PROVINCIA values(802,902,'Zulia');
insert into PROVINCIA values(803,903,'Bogotá');
insert into PROVINCIA values(804,904,'Sao Paulo');
insert into PROVINCIA values(805,905,'Montevideo');
insert into PROVINCIA values(806,906,'Santiago');
insert into PROVINCIA values(807,907,'Buenos Aires');
insert into PROVINCIA values(808,908,'La Paz');
insert into PROVINCIA values(809,909,'Central');
insert into PROVINCIA values(810,910,'Ciudad de México');
insert into PROVINCIA values(811,901,'Pichincha');
insert into PROVINCIA values(812,901,'Manabí');
insert into PROVINCIA values(813,901,'Santa Elena');
insert into PROVINCIA values(814,901,'Esmeraldas');


insert into CIUDAD values('Guayaquil',801,'GYE');
insert into CIUDAD values('Maracaibo',802,'MAR');
insert into CIUDAD values('Bogotá',803,'BOG');
insert into CIUDAD values('Sao Paulo',804,'SP');
insert into CIUDAD values('Montevideo',805,'MVO');
insert into CIUDAD values('Santiago',806,'SGO');
insert into CIUDAD values('Buenos Aires',807,'CABA');
insert into CIUDAD values('La Paz',808,'LPZ');
insert into CIUDAD values('Asunción',809,'ASUN');
insert into CIUDAD values('Ciudad de México',810,'CDMX');
insert into CIUDAD values('Quito',811,'PQT');
insert into CIUDAD values('Manta',812,'MNT');
insert into CIUDAD values('Portoviejo',812,'PTV');
insert into CIUDAD values('Salinas',813,'SLN');
insert into CIUDAD values('Libertad',813,'LBT');

insert into DIRECCION values(2001,'Guayaquil',1001,'Rocafuerte','Avenida Rocafuerte','Calle Escobedo',100,'Parque de la Libertad');
insert into DIRECCION values(2002,'Guayaquil',1002,'Carbo','Calle 9 de Octubre','Calle 10 de Agosto',100,'Malecón Simón Bolívar');
insert into DIRECCION values(2003,'Guayaquil',1003,'Urdesa','Avenida Las Américas','Calle Francisco de Orellana',100,'Parque Samanes');
insert into DIRECCION values(2004,' Quito',1004,'Centro Historico','Calle García Moreno','Calle Sucre',100,'Palacio de Carondelet');
insert into DIRECCION values(2005,'Quito',1005,'La Mariscal','Avenida 18 de Semptiembre','Calle Reina Victoria',100,'Plaza Foch');
insert into DIRECCION values(2006,'Quito',1006,'El Ejido','Avenida de los Shyris','Calle Colón',100,'Parque El Ejido');
insert into DIRECCION values(2007,'Manta',1007,'Tarqui','Avenida 25 de Julio','Calle 10 de Agosto',100,'Parque de la madre');
insert into DIRECCION values(2008,'Portoviejo',1008,'Portoviejo','Avenida 3 de Mayo','Calle 28 de Agosto',100,'Parque de la Ciudad');
insert into DIRECCION values(2009,'Salinas',1009,'San Lorenzo','Avenida 9 de Octubre','Calle 10 de Agosto',100,'Yatch Club');
insert into DIRECCION values(2010,'Libertad',1010,'San Sebastian','Avenida Colombia','Calle Estados Unidos',100,'Refineria');

insert into TELEFONO values(1001,0987654321);
insert into TELEFONO values(1002,0912345678);
insert into TELEFONO values(1003,0913246587);
insert into TELEFONO values(1004,0915364875);
insert into TELEFONO values(1005,0958455652);
insert into TELEFONO values(1006,0985128912);
insert into TELEFONO values(1007,0921289128);
insert into TELEFONO values(1008,0989125982);
insert into TELEFONO values(1009,0985181891);
insert into TELEFONO values(1010,0985181895);

INSERT INTO CATEGORIA_PRODUCTO VALUES
  ('ELECTRONICA', 'CELULARES'),
  ('HOGAR', 'MUEBLES'),
  ('ROPA', 'VESTIDOS'),
  ('DEPORTES', 'ZAPATILLAS'),
  ('LIBROS', 'NOVELAS'),
  ('TECNOLOGIA', 'LAPTOPS'),
  ('BELLEZA', 'MAQUILLAJE'),
  ('MUSICA', 'CDs'),
  ('AUTOS', 'ACCESORIOS'),
  ('JUGUETES', 'LEGOS');

insert into PRODUCTO values
    (50001,'Smartphone','Samsung',2000,'ELECTRONICA'),
    (50002,'Laptop','Asus',1000,'TECNOLOGIA'),
    (50003,'Laptop','Acer',500,'TECNOLOGIA'),
    (50004,'Air force 1','Nike',120,'DEPORTES'),
    (50005,'Forum Low','Adidas',150,'DEPORTES'),
    (50006,'Lego Star Wars Millennium Falcon','Lego',200,'JUGUETES'),
    (50007,'Mesa','Pycca',40,'HOGAR'),
    (50008,'Iphone 15 Pro Max','Apple',1000,'ELECTRONICA'),
    (50009,'Kit de faros LED para auto','Philips',  200,'AUTOS'),
    (50010,'Cámara de reversa con pantalla','Anker',300,'AUTOS'),
    (50011,'Sistema de audio para auto','JBL',1000,'AUTOS'),
    (50012,'Lego Creator 3 en 1','Lego',50,'JUGUETES');

INSERT INTO IMAGEN_PRODUCTO values
    (50001,'imagen01.jpg'),
    (50002,'imagen02.jpg'),
    (50003,'imagen03.jpg'),
    (50004,'imagen04.jpg'),
    (50005,'imagen05.jpg'),
    (50006,'imagen06.jpg'),
    (50007,'imagen07.jpg'),
    (50008,'imagen08.jpg'),
    (50009,'imagen09.jpg'),
    (50010,'imagen10.jpg'),
    (50011,'imagen11.jpg'),
    (50012,'imagen12.jpg');

INSERT INTO INVENTARIO values
    (111001,10),
    (111002,13),
    (111003,5),
    (111004,20),
    (111005,40),
    (111006,12),
    (111007,4),
    (111008,10),
    (111009,100),
    (111010,32),
    (111011,8),
    (111012,3),
    (111013,30);

INSERT INTO ALMACENAMIENTO values
    (111001,50001),
    (111002,50002),
    (111003,50003),
    (111004,50004),
    (111005,50005),
    (111006,50006),
    (111007,50007),
    (111008,50008),
    (111009,50009),
    (111010,50010);

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

insert into VISUALIZACION_PUBLICACIONES values
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    ();

