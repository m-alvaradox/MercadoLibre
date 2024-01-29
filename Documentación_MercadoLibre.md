# Documentación

Sistema: Mercado Libre

**Índice**

1. [Triggers](#id1)
2. [Views](#id2)
3. [Procedures](#id3)
4. [Índices](#id4)
5. [Usuarios y Privilegios](#id5)

### Data Definition Language (DDL)

#### Triggers (Disparadores) <a name="id1"></a>

| Nombre                        | Evento | Tabla       | Tiempo | Descripción                                                                                             |
| ----------------------------- | ------ | ----------- | ------ | -------------------------------------------------------------------------------------------------------- |
| GENERARORDEN                  | INSERT | ORDEN       | AFTER  | Se actualiza el stock disponible y la cantidad de veces que puede aplicar un cupón al generar una orden |
| ACTUALIZARREPUTACION          | UPDATE | ORDEN       | AFTER  | Recalcula la reputación del vendedor con la nueva calificación                                         |
| ACTUALIZAR_ESTADO_PUBLICACION | UPDATE | PUBLICACION | BEFORE | Cambia el estado de la publicación según el stock                                                      |
| NUEVOCLIENTE                  | INSERT | USUARIO     | AFTER  | Todo nuevo usuario es considerado cliente                                                                |
| NUEVOVENDEDOR                 | INSERT | PUBLICACION | BEFORE | El usuario se convierte en vendedor cuando realiza por primera vez una publicación                      |

#### Views (Reportes) <a name="id2"></a>

| Nombre               | Descripción                                                                                                                                                                                                                                                                             |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GENERO_USUARIOS      | Define un porcentaje de cada género en base a los usuarios registrados en la base de datos                                                                                                                                                                                              |
| EDADES_USUARIOS      | Muestre las edades actuales de los usuarios en base a la fecha de nacimiento                                                                                                                                                                                                             |
| USUARIOS_POR_PAÍS   | Define un porcentaje de los usuarios por país                                                                                                                                                                                                                                           |
| INTERES_USUARIOS     | Define un porcentaje en base a las visualizaciones de productos por categoría                                                                                                                                                                                                           |
| CALIDAD_MERCADOLIBRE | Estima la credibilidad del sistema de Mercado Libre a través de una vista que mostrará el promedio de todas las estrellas producto y vendedor de todas la órdenes. Además, a través de condiciones se mostrará la calidad del servicio (Muy mala, Mala, Regular, Buena, Muy Buena) |

#### Stored Procedures (Procedimientos) <a name="id3"></a>

| Nombre                 | Parámetros                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| CREARCUENTA            | usuario, password, nombre, apellido, fechanacimiento, email, telefono, genero                                                     |
| ACTUALIZAR_CUENTA      | IDUSUARIO, DATO_ACTUALIZAR, NUEVO_DATO                                                                                            |
| CANCELAR_CUENTA        | IDUSUARIO                                                                                                                         |
| registrarProducto      | nombre, marca, categoria, subcategoria                                                                                            |
| crearPublicacion       | descripcion, tipoexposicion, productid, idvendedor, precioventa, nombrepublicacion, stock                                         |
| MODIFICAR_PUBLICACION  | IDPUBLICACION, CAMPO, NUEVO_VALOR                                                                                                 |
| ELIMINAR_PUBLICACION   | IDPUBLICACION                                                                                                                     |
| ENVIAR_PREGUNTA        | idCliente, vendedor, publicacion, mensaje                                                                                         |
| RESPONDER_PREGUNTA     | PREGUNTAID, RESPUESTA                                                                                                             |
| registrarVisualizacion | userid, nopublicacion                                                                                                             |
| REALIZARCOMPRA         | cupon, idproducto, idpago, cantidadproducto, idpublicacion, idcliente, idvendedor, importe, iddireccion, costoenvio, fechaentrega |
| CALIFICARCOMPRA        | estrellasproducto, estrellasvendedor, comentario,  idOrden                                                                        |
| NUEVADIRECCION         | parroquia, referencias, idCiudad, userid                                                                                          |
| ELIMINARDIRECCION      | idDireccion                                                                                                                       |
| NUEVORECLAMO           | tipo, idCliente, idVendedor, idOrden                                                                                              |
| EMITIRFACTURA          | descripcion, idVendedor, idCliente, idOrden                                                                                       |
| AGREGAR_CUPON          | IDCUPON, NOMBRE, DESCUENTO, FECHAVENCIMIENTO, CLIENTEID, VECES                                                                    |
| AGREGAR_DEPOSITO       | IDCLIENTE, MONTO                                                                                                                  |

#### Índices <a name="id4"></a>

| Índice              | Tabla    | Columnas     | Justificación                                                                                                                                                                                                                                                                  |
| -------------------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| idx_marca            | Producto | marca        | Agregue este indice porque las personas queremos identificar un producto directamente por la marca, por lo que ahorrariamos buscar en todas las filas la marca cuando podemos establecer este indice que nos lleve directo haciendo mas eficaz el tiempo de ejecucion del query |
| idx_nombre_usuario   | Usuario  | nombre       | Agregado con el objetivo de agilizar el tiempo de consulta para el filtrado de usuario donde en la mayoria de los casos, buscaremos mostrar su nombre, accion que es utilizada frecuentemente en nuestro diseño de la aplicacion                                               |
| idx_apellido_usuario | Usuario  | apellido     | Agregado con el objetivo de agilizar el tiempo de consulta para el filtrado de usuario que al igual que el indice por nombre, casi siempre buscaremos mostrar el apellido del cliente                                                                                           |
| idx_nombre_ciudad    | Ciudad   | nombreciudad | La razón por la que se creó el índice previo es debido a que es importante optimizar la búsqueda a partir de las distintas ciudades. Especialmente cuando se trata de una ṕagina en la que se realiza una compra-venta desde y hasta una variedad de lugares.              |
| idx_nombre_pais      | Pais     | nombrepais   | En una aplicacion como mercado libre es muy importante el país, por lo que cada busqueda o uso en el sistema será optimizado al crear un indice de la tabla país                                                                                                             |

### Control y Seguridad (DCL) <a name="id5"></a>

| Usuario      | Contraseña | Descripción                                                                                    | Permisos                                                       |
| ------------ | ----------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| rafaelrosado | contrasena1 | Sociólogo                                                                                      | Views: genero_usuarios, edades_usuarios                        |
| micarod      | contrasena2 | Analista/Estratega de Marketing                                                                 | Views: calidad_mercadolibre, interes_usuarios, edades_usuarios |
| lupita       | contrasena3 | Banquero del Barrio: Es quien efectúa los pagos mediante depósito en el sistema               | Views: edades_usuarios Procedures: agregar_deposito            |
| astridlopez  | contrasena4 | Talento Humano: Encargado de enviar un correo de felicitación a quienes cumplen años este mes | Views: edades_usuarios, interes_usuarios                       |
| michaelpena  | contrasena5 | Secretario: Encargado de agregar cupones                                                        | Views: edades_usuarios, Procedures: agregar_cupones            |
