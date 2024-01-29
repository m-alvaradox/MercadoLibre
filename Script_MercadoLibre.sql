create database IF NOT EXISTS MercadoLibre;
use MercadoLibre;

-- Creacion de Tablas

CREATE TABLE IF NOT EXISTS USUARIO (
  USERID VARCHAR(50) PRIMARY KEY,
  PASS VARCHAR(16) NOT NULL,
  NOMBRE VARCHAR(10) NOT NULL,
  APELLIDO VARCHAR(10) NOT NULL,
  FECHANACIMIENTO DATE NOT NULL,
  ESCLIENTE BOOLEAN NOT NULL DEFAULT TRUE,
  ESVENDEDOR BOOLEAN NOT NULL DEFAULT FALSE,
  EMAIL VARCHAR(50) NOT NULL,
  TELEFONO VARCHAR(10) NOT NULL,
  GENERO ENUM('Masculino','Femenino','LGBTI') NOT NULL
);

CREATE TABLE IF NOT EXISTS CLIENTE (
  USERID VARCHAR(50) PRIMARY KEY,
  CONSTRAINT fk_userid_cliente FOREIGN KEY (USERID) REFERENCES USUARIO (USERID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS VENDEDOR (
  USERID VARCHAR(50) PRIMARY KEY,
   REPUTACION FLOAT DEFAULT NULL,
  CONSTRAINT fk_userid_vendedor FOREIGN KEY (USERID) REFERENCES USUARIO (USERID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PAIS (
  COUNTRYID INT PRIMARY KEY,
  NOMBREPAIS VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS PROVINCIA (
  PROVID INT PRIMARY KEY,
  COUNTRYID INT NOT NULL,
  NOMBREPROVINCIA VARCHAR(20) NOT NULL,
  CONSTRAINT fk_countryid_provincia FOREIGN KEY (COUNTRYID) REFERENCES PAIS (COUNTRYID)
);

CREATE TABLE IF NOT EXISTS CIUDAD (
  CITYID INT PRIMARY KEY,
  NOMBRECIUDAD VARCHAR(50) NOT NULL,
  PROVID INT NOT NULL,
   SIGLAS VARCHAR(5) NOT NULL,
  CONSTRAINT fk_provid_ciudad FOREIGN KEY (PROVID) REFERENCES PROVINCIA (PROVID)
);

CREATE TABLE IF NOT EXISTS DIRECCION (
  ID INT auto_increment PRIMARY KEY,
  IDCIUDAD INT NOT NULL,
  USERID VARCHAR(50) NOT NULL,
  PARROQUIA VARCHAR(50) NOT NULL,
  REFERENCIAS VARCHAR(200) NOT NULL,
  CONSTRAINT fk_userid_direccion FOREIGN KEY (USERID) REFERENCES USUARIO (USERID) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_idciudad_direccion FOREIGN KEY (IDCIUDAD) REFERENCES CIUDAD (CITYID)
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
  PRODUCTID INT NOT NULL,
  IDVENDEDOR VARCHAR(50) NOT NULL,
  PRECIOVENTA FLOAT NOT NULL,
  ESTADO ENUM('Activa','Agotado') NOT NULL DEFAULT 'Activa',
  FECHAPUBLICACION DATE NOT NULL DEFAULT(CURRENT_DATE),
  NOMBREPUBLICACION VARCHAR(50) NOT NULL,
  STOCK INT NOT NULL,
  PRIMARY KEY(NOPUBLICACION),
  CONSTRAINT fk_productid_publicacion FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTO (PRODUCTID),
  CONSTRAINT fk_idvendedor_publicacion FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS VISUALIZACION_PUBLICACIONES (
  REGID INT AUTO_INCREMENT PRIMARY KEY,
  USERID VARCHAR(50),
  NOPUBLICACION  int,
  FECHA DATE NOT NULL DEFAULT(CURRENT_DATE),
  CONSTRAINT fk_userid_vispub FOREIGN KEY (USERID) REFERENCES USUARIO (USERID) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_nopublicacion_vispub FOREIGN KEY (NOPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS PAGO (
  TRANSID INT AUTO_INCREMENT PRIMARY KEY,
  METODO ENUM('Depósito','Crédito') NOT NULL,
  MONTO FLOAT NOT NULL,
  CUOTA INT NOT NULL,
  CARDNUMBER VARCHAR(20),
  IDCLIENTE VARCHAR(50),
  FECHAPAGO DATE NOT NULL DEFAULT (CURRENT_DATE),
  CONSTRAINT fk_idcliente_pago FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS PREGUNTA (
  IDPREGUNTA int  AUTO_INCREMENT,
  CONTENIDO VARCHAR(50) NOT NULL,
  TIEMPOENVIADO DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  FECHAHORARESPUESTA DATETIME DEFAULT NULL,
  MENSAJERESPUESTA VARCHAR(100) DEFAULT NULL,
  IDCLIENTE VARCHAR(50),
  IDVENDEDOR VARCHAR(50),
  NOPUBLICACION  int,
  
  PRIMARY KEY(IDPREGUNTA),
  CONSTRAINT fk_idcliente_pregunta FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_idvendedor_pregunta FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_nopublicacion_pregunta FOREIGN KEY (NOPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS CUPON (
  ID INT PRIMARY KEY,
  NOMBRE VARCHAR(10) NOT NULL,
  DESCUENTO FLOAT NOT NULL,
  FECHAVENCIMIENTO DATE NOT NULL,
  CLIENTEID VARCHAR(50),
  VECES INT NOT NULL,
  CONSTRAINT fk_clienteid_cupon FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ORDEN (
  ORDERID INT AUTO_INCREMENT PRIMARY KEY,
  FECHACREACION DATE NOT NULL DEFAULT (CURRENT_DATE),
  ESTADO ENUM('Pendiente','En curso','Completada') NOT NULL DEFAULT 'Pendiente',
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
  IDCLIENTE VARCHAR(50),
  IDVENDEDOR VARCHAR(50),
  IDDIRECCION INT,
  IDPUBLICACION INT,
  CONSTRAINT fk_idcliente_orden FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE (USERID) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT fk_idcupon_orden FOREIGN KEY (IDCUPON) REFERENCES CUPON (ID) ON DELETE SET NULL,
  CONSTRAINT fk_productid_orden FOREIGN KEY (PRODUCTID) REFERENCES PRODUCTO (PRODUCTID),
  CONSTRAINT fk_idpago_orden FOREIGN KEY (IDPAGO) REFERENCES PAGO (TRANSID),
  CONSTRAINT fk_idvendedor_orden FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR (USERID) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT fk_iddreccion_orden FOREIGN KEY (IDDIRECCION) REFERENCES DIRECCION (ID) ON DELETE SET NULL,
  CONSTRAINT fk_idpublicacion_orden FOREIGN KEY (IDPUBLICACION) REFERENCES PUBLICACION (NOPUBLICACION) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS RECLAMO (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  TIPO VARCHAR(20) NOT NULL,
  ESTADO ENUM('Abierto','Cerrado') NOT NULL DEFAULT 'Abierto',
  CLIENTEID VARCHAR(50) NOT NULL,
  VENDEDORID VARCHAR(50),
  ORDERID INT,
  FECHAINGRESO DATE NOT NULL DEFAULT (CURRENT_DATE),
  CONSTRAINT fk_clienteid_reclamo FOREIGN KEY (CLIENTEID) REFERENCES CLIENTE (USERID) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_vendedorid_reclamo FOREIGN KEY (VENDEDORID) REFERENCES VENDEDOR (USERID) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT fk_orderid_reclamo FOREIGN KEY (ORDERID) REFERENCES ORDEN (ORDERID)
);

CREATE TABLE IF NOT EXISTS FACTURA (
FACTID INT AUTO_INCREMENT PRIMARY KEY,
FECHA DATE NOT NULL DEFAULT (CURRENT_DATE),
DESCRIPCION VARCHAR(100),
IDVENDEDOR VARCHAR(50),
IDCLIENTE VARCHAR(50),
IDORDEN INT NOT NULL,
CONSTRAINT fk_idvendedor_factura FOREIGN KEY (IDVENDEDOR) REFERENCES VENDEDOR(USERID) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT fk_idcliente_factura FOREIGN KEY (IDCLIENTE) REFERENCES CLIENTE(USERID) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT fk_idorden_factura FOREIGN KEY (IDORDEN) REFERENCES ORDEN(ORDERID) 
);

CREATE TABLE IF NOT EXISTS TARJETA (
ID INT AUTO_INCREMENT PRIMARY KEY,
NUMERO VARCHAR(20) NOT NULL,
MARCA ENUM ('AMERICAN EXPRESS', 'VISA', 'MASTERCARD') NOT NULL,
CVV VARCHAR(3) NOT NULL,
FECHAVENCIMIENTO DATE NOT NULL,
USERID VARCHAR(50)  NOT NULL,
CONSTRAINT fk_userid_tarjeta FOREIGN KEY (USERID) REFERENCES USUARIO(USERID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- TRIGGERS

DELIMITER $$
CREATE TRIGGER IF NOT EXISTS NUEVOCLIENTE
AFTER INSERT ON USUARIO
FOR EACH ROW BEGIN
INSERT INTO CLIENTE VALUES (NEW.USERID);
END $$
DELIMITER $$

DELIMITER $$
CREATE TRIGGER IF NOT EXISTS NUEVOVENDEDOR
BEFORE INSERT ON PUBLICACION
FOR EACH ROW BEGIN
    
    UPDATE USUARIO
    SET ESVENDEDOR = TRUE
    WHERE USERID = NEW.IDVENDEDOR;

    INSERT IGNORE INTO VENDEDOR(USERID) VALUES (NEW.IDVENDEDOR);

END $$
DELIMITER $$

DELIMITER $$
CREATE TRIGGER IF NOT EXISTS ACTUALIZAR_ESTADO_PUBLICACION
BEFORE UPDATE ON PUBLICACION
FOR EACH ROW BEGIN

	IF NEW.STOCK >0 THEN
		SET NEW.estado = 'Activa';
	else
		SET new.estado = 'Agotado';
    END IF;

END $$
DELIMITER $$

DELIMITER $$
CREATE TRIGGER IF NOT EXISTS GENERARORDEN
AFTER INSERT ON ORDEN
FOR EACH ROW BEGIN
UPDATE PUBLICACION
SET STOCK = STOCK - NEW.CANTIDADPRODUCTO
WHERE NOPUBLICACION = NEW.IDPUBLICACION;

UPDATE CUPON
SET VECES = VECES - 1
WHERE ID = NEW.IDCUPON;

UPDATE VENDEDOR
SET REPUTACION = ROUND((SELECT AVG(ESTRELLASVENDEDOR) AS PROMEDIO FROM ORDEN WHERE IDVENDEDOR = new.IDVENDEDOR),2)
WHERE USERID = new.IDVENDEDOR;

END $$
DELIMITER $$

DELIMITER $$
CREATE TRIGGER IF NOT EXISTS ACTUALIZARREPUTACION
AFTER UPDATE ON ORDEN
FOR EACH ROW BEGIN
UPDATE VENDEDOR
SET REPUTACION = ROUND((SELECT AVG(ESTRELLASVENDEDOR) AS PROMEDIO FROM ORDEN WHERE IDVENDEDOR = new.IDVENDEDOR),2)
WHERE USERID = new.IDVENDEDOR;
END $$
DELIMITER $$

-- PROCEDURES
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS CREARCUENTA (IN USUARIO VARCHAR(50), IN PASS VARCHAR(50), 
IN NOMBRE VARCHAR(10), IN APELLIDO VARCHAR(10), IN FECHANACIMIENTO DATE, IN EMAIL VARCHAR(50), IN TELEFONO VARCHAR(10), IN GENERO ENUM ('Masculino', 'Femenino', 'LGBT'))
BEGIN

    DECLARE v_id_usuario INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;

    -- Inserto los datos

    INSERT INTO USUARIO (USERID,PASS,NOMBRE,APELLIDO,FECHANACIMIENTO, EMAIL,TELEFONO,GENERO) VALUES
    (USUARIO, PASS, NOMBRE, APELLIDO, FECHANACIMIENTO, EMAIL, TELEFONO, GENERO);

    SET v_id_usuario = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. ID de usuario: ', v_id_usuario) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS REALIZARCOMPRA (IN IDCUPON INT, IN PRODUCTID INT, IN IDPAGO INT,
IN CANTIDADPRODUCTO INT, IN IDPUBLICACION INT, IN IDCLIENTE VARCHAR(50), IN IDVENDEDOR VARCHAR(50),
IN IMPORTE FLOAT, IN IDDIRECCION INT, IN COSTOENVIO FLOAT, IN FECHAENTREGA DATE)
BEGIN

    DECLARE v_id_orden INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;

    -- Inserto los datos

    INSERT INTO ORDEN (IDCUPON, PRODUCTID, IDPAGO, CANTIDADPRODUCTO, IDPUBLICACION, IDCLIENTE, IDVENDEDOR,
    IMPORTE, IDDIRECCION, COSTOENVIO, FECHAENTREGA) VALUES
    (IDCUPON, PRODUCTID, IDPAGO, CANTIDADPRODUCTO, IDPUBLICACION, IDCLIENTE, IDVENDEDOR,
    IMPORTE, IDDIRECCION, COSTOENVIO, FECHAENTREGA);

    SET v_id_orden = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. ID de Orden: ', v_id_orden) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS CALIFICARCOMPRA (IN NEW_ESTRELLASPRODUCTO INT, IN NEW_ESTRELLASVENDEDOR INT, IN NEW_COMENTARIO VARCHAR(100), IN IDORDEN INT)
BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;

    UPDATE ORDEN
    SET ESTRELLASPRODUCTO = NEW_ESTRELLASPRODUCTO,
    ESTRELLASVENDEDOR = NEW_ESTRELLASVENDEDOR,
    COMENTARIO = NEW_COMENTARIO
    WHERE ORDERID = IDORDEN;
    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS NUEVADIRECCION (IN PARROQUIA VARCHAR(50), IN REFERENCIAS VARCHAR(200),
IN IDCIUDAD INT, IN USERID VARCHAR(50))
BEGIN

    DECLARE v_id_direccion INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;

    -- Inserto los datos

    INSERT INTO DIRECCION (PARROQUIA, REFERENCIAS, IDCIUDAD, USERID) VALUES
    (PARROQUIA, REFERENCIAS, IDCIUDAD, USERID);

    SET v_id_direccion = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Direccion: ', v_id_direccion) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS ELIMINARDIRECCION (IN DIRECCION_ID INT)
BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;

    DELETE FROM DIRECCION
    WHERE ID = DIRECCION_ID;

    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS NUEVORECLAMO (IN TIPO VARCHAR(20),
IN CLIENTEID VARCHAR(50), IN VENDEDORID VARCHAR(50), IN ORDERID INT)
BEGIN

    DECLARE v_id_reclamo INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;

    -- Inserto los datos

    INSERT INTO RECLAMO (TIPO, CLIENTEID, VENDEDORID, ORDERID) VALUES
    (TIPO, CLIENTEID, VENDEDORID, ORDERID);

    SET v_id_reclamo = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Reclamo: ', v_id_reclamo) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS EMITIRFACTURA (IN DESCRIPCION VARCHAR(100), IN IDVENDEDOR VARCHAR(50), 
IN IDCLIENTE VARCHAR(50), IN IDORDEN INT)
BEGIN

    DECLARE v_id_factura INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;

    -- Inserto los datos

    INSERT INTO FACTURA (DESCRIPCION, IDVENDEDOR, IDCLIENTE, IDORDEN) VALUES
    (DESCRIPCION, IDVENDEDOR, IDCLIENTE, IDORDEN);

    SET v_id_factura = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Factura: ', v_id_factura) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS registrarProducto(IN NOMBRE VARCHAR(50), IN MARCA VARCHAR(15), IN CATEGORIA VARCHAR(20), IN SUBCATEGORIA VARCHAR(20))
BEGIN

    DECLARE v_id_producto INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;
    -- Insertar datos
    INSERT INTO PRODUCTO (NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA)
    VALUES(NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA);

    SET v_id_producto = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Producto: ', v_id_producto) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS crearPublicacion(IN DESCRIPCION VARCHAR(500), IN TIPOEXPOSICION varchar(50), 
IN PRODUCTID int, IN IDVENDEDOR varchar(50), IN PRECIOVENTA float,
IN NOMBREPUBLICACION VARCHAR(50), IN STOCK int)
BEGIN

    DECLARE v_id_publicacion INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;
    -- Insertar datos
    INSERT INTO PUBLICACION (DESCRIPCION,TIPOEXPOSICION, PRODUCTID,IDVENDEDOR,PRECIOVENTA,
        NOMBREPUBLICACION,STOCK)
    VALUES(DESCRIPCION, TIPOEXPOSICION,PRODUCTID,IDVENDEDOR,PRECIOVENTA,
        NOMBREPUBLICACION,STOCK);

    SET v_id_publicacion = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Publicacion: ', v_id_publicacion) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS registrarVisualizacion(IN USERID varchar(50), IN NOPUBLICACION int)
BEGIN
    DECLARE v_regid INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;
    -- Insertar datos
    INSERT INTO visualizacion_publicaciones (USERID,NOPUBLICACION) 
    VALUES(USERID, NOPUBLICACION);

    SET v_regid = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Publicacion: ', v_regid) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;

END $$
DELIMITER;

DELIMITER //
CREATE PROCEDURE AskQuestion(IN idCliente VARCHAR(50), IN vendedor VARCHAR(50), IN publicacion INT, IN mensaje VARCHAR(50))
BEGIN
    DECLARE v_question_id INT;
    DECLARE v_numero_filas INT;

    START TRANSACTION;
    -- Insertar datos

    INSERT INTO PREGUNTA (CONTENIDO, IDCLIENTE, IDVENDEDOR, NOPUBLICACION) 
    VALUES (mensaje, idCliente, vendedor, publicacion);


    SET v_question_id = LAST_INSERT_ID();
    
    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;
    
    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Pregunta: ', v_question_id) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
    
END //
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS ACTUALIZAR_CUENTA(IN IDUSUARIO VARCHAR(50), IN DATO_ACTUALIZAR VARCHAR(50), IN NUEVO_DATO VARCHAR(50))
BEGIN
	DECLARE valor_nuevo VARCHAR(50);
    START TRANSACTION;
	CASE DATO_ACTUALIZAR
		WHEN 'USERID' THEN
			UPDATE USUARIO SET USERID = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT USERID FROM USUARIO WHERE USERID = NUEVO_DATO INTO valor_nuevo; #Debe compararse con el nuevo usuario
		WHEN 'EMAIL' THEN
			UPDATE USUARIO SET EMAIL = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT EMAIL FROM USUARIO WHERE USERID = IDUSUARIO INTO valor_nuevo;
		WHEN 'PASS' THEN
			UPDATE USUARIO SET PASS = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT PASS FROM USUARIO WHERE USERID = IDUSUARIO INTO valor_nuevo;
		WHEN 'NOMBRE' THEN
			UPDATE USUARIO SET NOMBRE = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT NOMBRE FROM USUARIO WHERE USERID = IDUSUARIO INTO valor_nuevo;
		WHEN 'APELLIDO' THEN
			UPDATE USUARIO SET APELLIDO = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT APELLIDO FROM USUARIO WHERE USERID = IDUSUARIO INTO valor_nuevo;
		WHEN 'TELEFONO' THEN
			UPDATE USUARIO SET TELEFONO = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT TELEFONO FROM USUARIO WHERE USERID = IDUSUARIO INTO valor_nuevo;
		WHEN 'GENERO' THEN
			UPDATE USUARIO SET GENERO = NUEVO_DATO WHERE USERID = IDUSUARIO;
            SELECT GENERO FROM USUARIO WHERE USERID = IDUSUARIO INTO valor_nuevo;
		ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Campo no válido';
	END CASE;
    IF valor_nuevo = NUEVO_DATO THEN
        COMMIT;
        SELECT CONCAT('¡Su ', DATO_ACTUALIZAR, ' se ha actualizado correctamente!') AS mensaje;
    ELSE
        ROLLBACK;
        SELECT '¡Error al actualizar los datos!. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS CANCELAR_CUENTA (IN IDUSUARIO VARCHAR(50))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;
    DELETE FROM USUARIO
    WHERE USERID = IDUSUARIO;

    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS RESPONDER_PREGUNTA (IN PREGUNTAID INT, IN RESPUESTA VARCHAR(100))
BEGIN
	DECLARE valor_nuevo VARCHAR(50);
    START TRANSACTION;

    UPDATE PREGUNTA SET MENSAJERESPUESTA = RESPUESTA WHERE IDPREGUNTA = PREGUNTAID;
	UPDATE PREGUNTA SET FECHAHORARESPUESTA = NOW() WHERE IDPREGUNTA = PREGUNTAID;
    
    SELECT MENSAJERESPUESTA FROM PREGUNTA WHERE IDPREGUNTA = PREGUNTAID INTO valor_nuevo;
	
    IF valor_nuevo = RESPUESTA THEN
        COMMIT;
        SELECT CONCAT('¡Su respuesta se ha publicado correctamente!') AS mensaje;
    ELSE
        ROLLBACK;
        SELECT '¡Error al actualizar los datos!. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS EDITAR_PUBLICACION (IN IDPUBLICACION INT,IN CAMPO VARCHAR(60), IN NUEVO_VALOR VARCHAR(500))
BEGIN
	DECLARE valor_nuevo VARCHAR(500);
    START TRANSACTION;

	CASE CAMPO
		WHEN 'nombrepublicacion' THEN
			UPDATE PUBLICACION SET NOMBREPUBLICACION =  NUEVO_VALOR WHERE NOPUBLICACION = IDPUBLICACION; #NOMBREPUBLICACION
			SELECT NOMBREPUBLICACION FROM PUBLICACION WHERE NOPUBLICACION = IDPUBLICACION INTO valor_nuevo; #NOMBREPUBLICACION
		WHEN 'descripcion' THEN
			UPDATE PUBLICACION SET DESCRIPCION =  NUEVO_VALOR WHERE NOPUBLICACION = IDPUBLICACION;
            SELECT DESCRIPCION FROM PUBLICACION WHERE NOPUBLICACION = IDPUBLICACION INTO valor_nuevo;
		WHEN 'precioventa' THEN
			UPDATE PUBLICACION SET PRECIOVENTA =  NUEVO_VALOR WHERE NOPUBLICACION = IDPUBLICACION;
            SELECT PRECIOVENTA FROM PUBLICACION WHERE NOPUBLICACION = IDPUBLICACION INTO valor_nuevo;
		WHEN 'estado' THEN
			UPDATE PUBLICACION SET ESTADO =  NUEVO_VALOR WHERE NOPUBLICACION = IDPUBLICACION;
            SELECT ESTADO FROM PUBLICACION WHERE NOPUBLICACION = IDPUBLICACION INTO valor_nuevo;
		WHEN 'stock' THEN
			UPDATE PUBLICACION SET STOCK =  NUEVO_VALOR WHERE NOPUBLICACION = IDPUBLICACION;
            SELECT STOCK FROM PUBLICACION WHERE NOPUBLICACION = IDPUBLICACION INTO valor_nuevo;
		ELSE
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Campo no válido';
	END CASE;
    	
    IF valor_nuevo = NUEVO_VALOR THEN
        COMMIT;
        SELECT CONCAT('¡Su publicacion se ha actualizado correctamente!') AS mensaje;
    ELSE
        ROLLBACK;
        SELECT '¡Error al actualizar la publicación!. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS ELIMINAR_PUBLICACION (IN IDPUBLICACION INT)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;
    DELETE FROM PUBLICACION
    WHERE NOPUBLICACION = IDPUBLICACION;

    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

-- PROCEDURES PRUEBA
DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS CAMBIAR_ESTADO_RECLAMO (IN RECLAMO_ID INT, IN NUEVO_ESTADO ENUM ('Abierto','Cerrado'))
BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;

    UPDATE RECLAMO
    SET ESTADO = NUEVO_ESTADO
    WHERE RECLAMO.ID = RECLAMO_ID;
    
    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS CAMBIAR_TIPO_PUBLICACION (IN PUBLICACION_ID INT, IN NUEVO_TIPO ENUM ('Gratuita','Clásica','Premium'))
BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;

    UPDATE PUBLICACION
    SET TIPOEXPOSICION = NUEVO_TIPO
    WHERE NOPUBLICACION = PUBLICACION_ID;
    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS CAMBIAR_ESTADO_ORDEN (IN ORDEN_ID INT, IN NUEVO_ESTADO ENUM ('Pendiente','En Curso','Completada'))
BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT 'ERROR';
        ROLLBACK;
	END;

    START TRANSACTION;

    UPDATE ORDEN
    SET ESTADO = NUEVO_ESTADO
    WHERE ORDERID = ORDEN_ID;
    SELECT 'OK';
    COMMIT; 

END $$
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE IF NOT EXISTS AGREGAR_CUPON(IN IDCUPON INT, IN NOMBRE VARCHAR(10), IN DESCUENTO FLOAT, 
IN FECHAVENCIMIENTO DATE, IN CLIENTEID VARCHAR(50), IN VECES INT)
BEGIN

    DECLARE v_numero_filas int;

    START TRANSACTION;

    INSERT INTO CUPON (ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO, CLIENTEID, VECES)
    VALUES (IDCUPON, NOMBRE, DESCUENTO, FECHAVENCIMIENTO, CLIENTEID, VECES);

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa') AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

DELIMITER $$

CREATE PROCEDURE IF NOT EXISTS AGREGAR_DEPOSITO(IN IDCLIENTE VARCHAR(50),IN MONTO FLOAT)
BEGIN

    DECLARE v_id_pago INT;
    DECLARE v_numero_filas int;

    START TRANSACTION;

    INSERT INTO PAGO (METODO, MONTO, CUOTA, IDCLIENTE)
    VALUES ('Depósito', MONTO, 1, IDCLIENTE);

    SET v_id_pago = LAST_INSERT_ID();

    -- Obtener el número de filas afectadas
    SELECT ROW_COUNT() INTO v_numero_filas;

    -- Comprobar si se insertó al menos una fila
    IF v_numero_filas = 1 THEN
        -- Éxito: confirmar la transacción
        COMMIT;
        SELECT CONCAT('Inserción exitosa. Pago: ', v_id_pago) AS mensaje;
    ELSE
        -- Error: deshacer la transacción
        ROLLBACK;
        SELECT 'Error al insertar datos. Transacción deshecha.' AS mensaje;
    END IF;
END $$
DELIMITER ;

-- Para llamar los SP
-- CALL CAMBIAR_ESTADO_RECLAMO();
-- CALL  CAMBIAR_TIPO_PUBLICACION();
-- CALL CAMBIAR_ESTADO_ORDEN();
-- CALL AGREGAR_CUPON();
-- CALL AGREGAR_DEPOSITO();

-- VISTAS
CREATE OR REPLACE VIEW genero_usuarios AS
SELECT genero,
    CONCAT(ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM usuario)), 0), '%') as porcentaje
FROM usuario
GROUP BY genero;

CREATE OR REPLACE VIEW interes_usuarios AS
SELECT Producto.categoria, 
    CONCAT(ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM visualizacion_publicaciones)), 0), '%') as porcentaje
FROM visualizacion_publicaciones LEFT JOIN  publicacion USING(NOPUBLICACION) JOIN Producto USING(PRODUCTID)
GROUP BY Producto.categoria;

CREATE OR REPLACE VIEW edades_usuarios AS
SELECT
    nombre,
    apellido,
    email,
    fechanacimiento,
    YEAR(CURDATE()) - YEAR(fechanacimiento) - (DATE_FORMAT(CURDATE(), '%m%d') < DATE_FORMAT(fechanacimiento, '%m%d')) AS edad_actual
FROM
    usuario;

CREATE OR REPLACE VIEW usuarios_por_pais AS
SELECT
    nombrepais,
    CONCAT(ROUND(((COUNT(*) / (SELECT COUNT(*) FROM usuario)) * 100),0),'%') AS porcentaje
FROM
    usuario join direccion using (userid) join ciudad on idciudad = cityid join provincia using (provid) join pais using (countryid)
GROUP BY
    nombrepais;


CREATE OR REPLACE VIEW calidad_mercadolibre AS
SELECT
    ROUND((AVG(estrellasproducto)),2) AS promedio_estrellas_producto,
    ROUND((AVG(estrellasvendedor)),2) AS promedio_estrellas_vendedor,
    CASE
        WHEN AVG(estrellasproducto) >= 0 AND AVG(estrellasproducto) < 2 THEN 'Muy mala'
        WHEN AVG(estrellasproducto) >= 2 AND AVG(estrellasproducto) < 3 THEN 'Mala'
        WHEN AVG(estrellasproducto) >= 3 AND AVG(estrellasproducto) < 4 THEN 'Regular'
        WHEN AVG(estrellasproducto) >= 4 AND AVG(estrellasproducto) < 5 THEN 'Buena'
        WHEN AVG(estrellasproducto) = 5 THEN 'Muy buena'
    END AS calidad_producto,
    CASE
        WHEN AVG(estrellasvendedor) >= 0 AND AVG(estrellasvendedor) < 2 THEN 'Muy mala'
        WHEN AVG(estrellasvendedor) >= 2 AND AVG(estrellasvendedor) < 3 THEN 'Mala'
        WHEN AVG(estrellasvendedor) >= 3 AND AVG(estrellasvendedor) < 4 THEN 'Regular'
        WHEN AVG(estrellasvendedor) >= 4 AND AVG(estrellasvendedor) < 5 THEN 'Buena'
        WHEN AVG(estrellasvendedor) = 5 THEN 'Muy buena'
    END AS calidad_vendedor
FROM
    orden;


-- INDICES
ALTER TABLE PRODUCTO
ADD INDEX idx_marca (marca);

ALTER TABLE USUARIO
ADD INDEX idx_nombre_usuario (nombre);

ALTER TABLE USUARIO
ADD INDEX idx_apellido_usuario (apellido);

ALTER TABLE CIUDAD
ADD INDEX idx_nombre_ciudad (NOMBRECIUDAD);

ALTER TABLE PAIS
ADD INDEX idx_nombre_pais(NOMBREPAIS);

-- INSERCIONES
INSERT INTO USUARIO (USERID, PASS, NOMBRE, APELLIDO, FECHANACIMIENTO, EMAIL, TELEFONO, GENERO) 
VALUES ('ownyag','12345','Owen','Yagual','2002-01-10','ownyag@live.com','0987654321','Masculino'),
('malvaradox','54321','Mario','Alvarado','2003-11-14','malvaradox@live.com','0912345678', 'Masculino'),
('xavicam','aaaaa','Xavier','Camacho','2002-04-01','xavicam@live.com','0913246587', 'Masculino'),
('javirod','11111','Javier','Rodriguez','2005-03-01','javirod@live.com','0915364875','Masculino'),
('naybor','12222222','Nayeli','Borbor','2001-02-01','naybor@live.com','0958455652', 'Femenino'),
('luchoont','12229871','Luis','Ontaneda','1990-05-01','luchont@yahoo.com','0985128912','LGBTI'),
('nickfigu','122253','Nick','Figueroa','2002-07-09','nickfigur@hotmail.com','0921289128','Masculino'),
('charlesrod','1256ga22','Carlos','Rodriguez','2010-05-12','charlesrod@gmail.com','0989125982','Masculino'),
('joelvill','1asdsa2222','Joel','Villon','2004-04-01','joelvilla@gmail.com','0985181891','Masculino'),
('angivel','122xv2092','Angie','Velastegui','2007-04-01','angivel@live.com','0985181895','Femenino'),
('angon','oiadsa','Angel','Ontaneda','2011-05-01','angon@live.com','0923748372','LGBTI'),
('ferchon','5ioqw','Fernando','Chacon','2015-03-01','ferchon@live.com','1234365465','Masculino'),
('jorgquij','aasdaaaa','Jorge','Quijije','2002-09-01','jorguijij@icloud.com','0998724354','Masculino'),
('arperez','11ads','Ariana','Perez','2002-12-01','arperez@live.com','3432345676', 'Femenino'),
('fiotorres','1x23zx45','Fiorella','Torres','1980-05-07','fiotorres@live.com','0983546753','LGBTI'),
('daniroca','5s43bcds21','Daniela','Roca','1980-10-05','daniroca@outlook.es','0956473847','Femenino');

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
    'Gratuita', 1,'ownyag',612.50,'Activa','2023-12-12','SAMSUNG GALAXY A70 SELLADO',4),
('INSPIRON 3910: rendimiento y portabilidad. Procesador Intel Core i5 de 11.ª generación, pantalla de 15,6 pulgadas.',
    'Gratuita',2,'malvaradox',800,'Activa','2022-10-23','DELL INSPIRON 3910 NUEVO',3),
('La Nitro 5: rendimiento potente y diseño elegante. Procesador Intel Core i7 de 12.ª generación, tarjeta gráfica NVIDIA RTX 3060',
    'Gratuita',3,'xavicam',250,'Activa','2019-11-11','XXXKIU DE OPORTUNIDAD',4),
('Las Air Force 1: un clásico de la moda urbana. Diseño sencillo, comodidad inigualable.',
    'Gratuita',4,'javirod',62.50,'Activa','2023-12-01','NKE AIR FORCE ONE',1),
('Las Forum Low: versátiles y combinables. Diseño retro, estilo minimalista.', 'Gratuita',5,'angon',210,
    'Activa','2022-11-11','ADIDAS FORUM LOW',5),
('El Millennium Falcon: el set de Lego más grande de la historia. 7541 piezas, nave espacial a escala 1:144.',
    'Gratuita',6,'ferchon',34.50,'Activa','2023-11-14','MILLENNIUM FALCOM APROVECHA',3),
('La mesa Pycca: sencilla y elegante. Diseño moderno, construcción resistente.',
    'Gratuita',7,'jorgquij',15.60,'Activa','2023-10-10','MESA PYCCA PARA LA FAMILIA',10),
('El iPhone 15 Pro Max: lo último en tecnología Apple. Pantalla OLED de 6,7 pulgadas, procesador A16 Bionic, cámara triple de 48MP.',
    'Gratuita',8,'arperez',1299.99,'Activa','2023-11-26','IPHONE 15 PRO MAX TRAIDA DESDE USA',5),
('Los faros LED Philips: más visibilidad y seguridad. Iluminación potente y uniforme, diseño elegante.',
    'Gratuita',9,'fiotorres',11.23,'Activa','2022-11-13','FAROS LED PHILLIPS',3),
('La cámara de reversa Anker: más seguridad al estacionar. Imágenes nítidas y claras, pantalla de 5 pulgadas.',
    'Gratuita',10,'daniroca',300,'Activa','2023-09-09','CAMARA REVERSA',8);
    
INSERT INTO VISUALIZACION_PUBLICACIONES (NOPUBLICACION,USERID,FECHA) VALUES
(1,'ownyag','2023-07-07'),(2,'malvaradox','2023-07-09'),(3,'xavicam','2023-07-12'),(4,'javirod','2023-07-15'),(5,'naybor','2023-08-16'),
(2,'luchoont','2023-07-28'),(7,'nickfigu','2023-08-01'),(7,'charlesrod','2023-08-07'),(3,'joelvill','2023-08-12'),(8,'angivel','2023-08-15');
    
INSERT INTO PAGO(IDCLIENTE,MONTO,METODO,CARDNUMBER,CUOTA, FECHAPAGO) VALUES
('ownyag',210,'Depósito',null,1,'2023-12-26'),
('malvaradox',612.50,'Depósito',null,1, '2023-12-11'),
('xavicam',34.50,'Depósito',null,1,'2023-12-21'),
('javirod',22.46,'Depósito',null,1,'2023-12-15'),
('naybor',980,'Depósito',null,1,'2023-12-13');

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
(4001,1,2,'malvaradox','ownyag',2,'2023-12-11','Completada',1,612.50,0,'2023-12-12',4,4,'Recibi en buenas condiciones pero muy tardado el envio',1),
(NULL,5,1,'ownyag','angon',NULL,'2023-12-26','Completada',1,210,0,NULL,5,5,'Buena experiencia, gracias',5),
(NULL,6,3,'xavicam','ferchon',NULL,'2023-12-21','Completada',1,34.50,0,NULL,4,4,NULL,6),
(NULL,9,4,'javirod','fiotorres',NULL,'2023-12-15','Completada',2,22.46,0,NULL,5,5,'Me gusto, gracias',9),
(4003,1,5,'naybor','ownyag',5,'2023-12-13','Completada',2,980,0,'2023-12-19',3,2,'Solo me llego una exijo una devolucion',1);

INSERT INTO RECLAMO (CLIENTEID,VENDEDORID,ORDERID,TIPO,FECHAINGRESO,ESTADO)VALUES
('malvaradox','ownyag',1,'RETRASO','2023-12-12','Cerrado'),
('naybor','ownyag',5,'FALLO ENTREGA','2023-12-19', 'Abierto');

INSERT INTO FACTURA (FECHA, DESCRIPCION, IDVENDEDOR, IDCLIENTE, IDORDEN) VALUES
('2023-12-14','COMPRA DE PRODUCTOS','ownyag','malvaradox',1);

INSERT INTO TARJETA (NUMERO, MARCA, CVV, FECHAVENCIMIENTO, USERID) VALUES
('5144 2637 4859 47586','MASTERCARD','067','2025-01-01','malvaradox');

-- DCL PERMISOS
 
-- Usuario 1: Sociologo
CREATE USER 'rafaelrosado'@'localhost' IDENTIFIED BY 'contrasena1';
GRANT SELECT ON mercadolibre.edades_usuarios TO 'rafaelrosado'@'localhost';
GRANT SELECT ON mercadolibre.genero_usuarios TO 'rafaelrosado'@'localhost';
FLUSH PRIVILEGES;

-- Usuario 2: Analista / Estratega de Marketing
CREATE USER 'micarod'@'localhost' IDENTIFIED BY 'contrasena2';
GRANT SELECT ON mercadolibre.calidad_mercadolibre TO 'micarod'@'localhost';
GRANT SELECT ON mercadolibre.interes_usuarios TO 'micarod'@'localhost';
GRANT SELECT ON mercadolibre.edades_usuarios TO 'micarod'@'localhost';
FLUSH PRIVILEGES;

-- Usuario 3: Banquero del barrio
CREATE USER 'lupita'@'localhost' IDENTIFIED BY 'contrasena3';
GRANT EXECUTE ON PROCEDURE mercadolibre.agregar_deposito TO 'lupita'@'localhost';
GRANT SELECT ON mercadolibre.edades_usuarios TO 'lupita'@'localhost';
FLUSH PRIVILEGES;

-- Usuario 4: Talento Humano
CREATE USER 'astridlopez'@'localhost' IDENTIFIED BY 'contrasena4';
GRANT SELECT ON mercadolibre.interes_usuarios TO 'astridlopez'@'localhost';
GRANT SELECT ON mercadolibre.edades_usuarios TO 'astridlopez'@'localhost';
FLUSH PRIVILEGES;

-- Usuario 5: Secretario
CREATE USER 'michaelpena'@'localhost' IDENTIFIED BY 'contrasena5';
GRANT EXECUTE ON PROCEDURE mercadolibre.agregar_cupon TO 'michaelpena'@'localhost';
GRANT SELECT ON mercadolibre.edades_usuarios TO 'michaelpena'@'localhost';
FLUSH PRIVILEGES;

/* Eliminar usuarios
DROP USER 'rafaelrosado'@'localhost';
DROP USER 'micarod'@'localhost';
DROP USER 'lupita'@'localhost';
DROP USER 'astridlopez'@'localhost';
DROP USER 'michaelpena'@'localhost';
*/