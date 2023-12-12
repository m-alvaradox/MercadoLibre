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
    (1,'imagen01.jpg'),
    (2,'imagen02.jpg'),
    (3,'imagen03.jpg'),
    (4,'imagen04.jpg'),
    (5,'imagen05.jpg'),
    (6,'imagen06.jpg'),
    (7,'imagen07.jpg'),
    (8,'imagen08.jpg'),
    (9,'imagen09.jpg'),
    (10,'imagen10.jpg'),



