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
|  Nombre | Evento  | Tabla   | Tiempo   | Descripción   |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| GENERARORDEN   | INSERT  | ORDEN  | AFTER  |  Se actualiza el stock disponible y la cantidad de veces que puede aplicar un cupón al generar una orden |
| ACTUALIZARREPUTACION   | UPDATE   | ORDEN  | AFTER  |  Recalcula la reputación del vendedor con la nueva calificación   |
| ACTUALIZAR_ESTADO_PUBLICACION   | UPDATE   | PUBLICACION  | BEFORE  |  Cambia el estado de la publicación según el stock |
| NUEVOCLIENTE    | INSERT   | USUARIO   | AFTER  | Todo nuevo usuario es considerado cliente  |
| NUEVOVENDEDOR  | INSERT   | PUBLICACION  | BEFORE  | El usuario se convierte en vendedor cuando realiza por primera vez una publicación   |

#### Views (Reportes) <a name="id2"></a>
| Nombre  | Descripción  |
| ------------ | ------------ |
| GENERO_USUARIOS   |  Define un porcentaje de cada género en base a los usuarios registrados en la base de datos |
| EDADES_USUARIOS  | Muestre las edades actuales de los usuarios en base a la fecha de nacimiento  |
| USUARIOS_POR_PAÍS | Define un porcentaje de los usuarios por país |
| INTERES_USUARIOS | Define un porcentaje en base a las visualizaciones de productos por categoría  |
| CALIDAD_MERCADOLIBRE | Estima la credibilidad del sistema de Mercado Libre a través de una vista que mostrará el promedio de todas las estrellas producto y vendedor de todas la órdenes. Además, a través de condiciones se mostrará la calidad del servicio (Muy mala, Mala, Regular, Buena, Muy Buena) |

#### Stored Procedures (Procedimientos) <a name="id3"></a>

| Nombre   | Parámetros   |
| ------------ | ------------ |
| CREARCUENTA  | usuario, password, nombre, apellido, fechanacimiento, email, telefono, genero  |
| ACTUALIZAR_CUENTA  |   |
| CANCELAR_CUENTA  |   |
| registrarProducto  |   |
| crearPublicacion  |   |
| MODIFICAR_PUBLICACION  |   |
| ELIMINAR_PUBLICACION  |   |
| ENVIAR_PREGUNTA |   |
| RESPONDER_PREGUNTA  |   |
| registrarVisualizacion  |   |
| REALIZARCOMPRA  |  cupon, idproducto, idpago, cantidadproducto, idpublicacion, idcliente, idvendedor, importe, iddireccion, costoenvio, fechaentrega |
| CALIFICARCOMPRA  | estrellasproducto, estrellasvendedor, comentario,  idOrden |
| NUEVADIRECCION  | parroquia, referencias, idCiudad, userid  |
| ELIMINARDIRECCION | idDireccion  |
| NUEVORECLAMO |  tipo, idCliente, idVendedor, idOrden |
| EMITIRFACTURA | descripcion, idVendedor, idCliente, idOrden |
| AGREGAR_CUPON |  |
| AGREGAR_DEPOSITO |   |



#### Índices <a name="id4"></a>

| Índice  | Tabla   | Columnas  | Justificación
| ------------ | ------------ | ------------ | ------------ |
| idx_marca  | Producto | marca  | Agregue este indice porque las personas queremos identificar un producto directamente por la marca, por lo que ahorrariamos buscar en todas las filas la marca cuando podemos establecer este indice que nos lleve directo haciendo mas eficaz el tiempo de ejecucion del query |
|   | Usuario  | nombre   |  |
|   | Usuario  | apellido  |  |
|   | Ciudad  | nombreciudad  |  |
|   | Pais  | nombrepais  |  |


### Control y Seguridad (DCL) <a name="id5"></a>

| Usuario  | Contraseña   | Descripción  | Permisos
| ------------ | ------------ | ------------ | ------------ |
| rafaelrosado  | contrasena1  | Sociólogo  | Views: genero_usuarios, edades_usuarios |
| micarod  | contrasena2  | Analista/Estratega de Marketing  | Views: calidad_mercadolibre, interes_usuarios, edades_usuarios  |
| lupita  | contrasena3  | Banquero del Barrio: Es quien efectúa los pagos mediante depósito en el sistema   | Views: edades_usuarios Procedures: agregar_deposito  |
| astridlopez  | contrasena4  | Talento Humano: Encargado de enviar un correo de felicitación a quienes cumplen años este mes  | Views: edades_usuarios, interes_usuarios  |
| michaelpena  | contrasena5  | Secretario: Encargado de agregar cupones | Views: edades_usuarios, Procedures: agregar_cupones |

