CREATE DATABASE mercado_libre;
USE DATABASE mercado_libre;
CREATE TABLE USUARIO (
  USER_ID INT PRIMARY KEY,
  PASSWORD VARCHAR(16),
  NOMBRE VARCHAR(10),
  APELLIDO VARCHAR(10),
  FECHA_NACIMIENTO DATE,
  ES_CLIENTE BOOLEAN,
  ES_VENDEDOR BOOLEAN
);

CREATE TABLE CLIENTE (
  USER_ID INT PRIMARY KEY,
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID)
);

CREATE TABLE VENDEDOR (
  USER_ID INT PRIMARY KEY,
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID),
  REPUTACION FLOAT
);

CREATE TABLE TELEFONO (
  USER_ID INT PRIMARY KEY,
  FOREIGN KEY (USER_ID) REFERENCES USUARIO (USER_ID),
  NUM_TELEFONO VARCHAR(10)
);
