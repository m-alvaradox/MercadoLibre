# Manual de Usuario

Sistema: Mercado Libre

**Índice**   
1. [Requisitos](#id1)
2. [Menú Principal](#id2)
3. [Funcionalidades del Sistema](#id3)
4. [Menús y Submenús](#id4)


## **Requisitos** <a name="id1"></a>

- Aplicación: Editor de código compatible con Python (Visual Studio Code, Replit, Pycharm, etc...)
- Instalar e importar la biblioteca de `pandas` y `pymysql`

<!--sec data-title="Prompt: Windows" data-id="windows_prompt2" data-collapse=true ces-->

Instalar

    --> pip install pandas
    --> pip install pymysql

<!--endsec-->

<!--sec data-title="Prompt: Windows" data-id="windows_prompt2" data-collapse=true ces-->

Importar

    import pandas as pd
    import pymysql

<!--endsec-->

- Para manejar la base de datos, debe poseer un IDE  (MySQL Workbench, MariaDB, etc...)

##### Servidor de la base de datos de Mercado Libre (Microsoft Azure)

<!--sec data-title="Prompt: Windows" data-id="windows_prompt2" data-collapse=true ces-->

    host="servergroup3.mysql.database.azure.com"

<!--endsec-->

## **Menú Principal** <a name="id2"></a>
### Menú Invitado

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/61268ba8-7c48-407e-9892-463a901bdb27)

### Menú Usuario

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/18832624-fcfb-40a9-95d8-d7558b0b499e)

## **Funcionalidades del Sistema** <a name="id3"></a>

### Inicio de sesión
Verifica que el usuario se encuentre registrado en la base de datos y que su contraseña sea la correcta

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/563c4f6b-5b3e-46a8-81dd-90898092aa5c)


### Creación de Cuenta
El usuario se registra en el sistema de Mercado Libre. Verifica que el usuario ingresado no exista en la base de datos para proceder con el registro y debe ser mayor de edad. 

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/20d7b3f2-1fd2-4fba-850e-07d07181dcfe)

### Visualizar Perfil
El usuario puede gestionar sus datos personales. Visualizar su nombre de usuario, email, genero, nombre y apellido, teléfono.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/77b0dca9-c9ca-48f0-aadc-fd1dc1789a93)

### Modificar Cuenta
El usuario puede modificar sus datos de cuenta y datos personales. Modificar su nombre de usuario, email, nombre y apellido, agregar, eliminar teléfonos de contacto.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/a8191c91-5cff-4e97-bef6-f51f85424039)

### Cancelar Cuenta
El usuario puede eliminar su cuenta permanentemente. Esto implicará borrar cualquier registro que lo asocie

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/db073990-e92c-4a9d-8e0b-ce6adfaaced9)

### Direcciones
El usuario puede ver sus direcciones registradas en el sistema. Asimismo puede modificar, agregar o borrar las ya existentes.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/c8773e07-e825-4680-be58-59103356693e)

### Métodos de Pago
El usuario puede consultar sus métodos de pago registrados (Tarjeta de Crédito), así como la posibilidad de añadir una antes o al momento de hacer una orden. Finalmente, también puede eliminar la tarjeta si no desea. El numero de tarjeta esta compuesta por 17 dígitos y no debe estar vencida. Además, el sistema solo acepta las tarjetas: AMERICAN EXPRESS, VISA O MASTERCARD. Esto se validó por la primera cifra de la tarjeta
1)	AMERICAN EXPRESS
2)	VISA
3)	MASTERCARD

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/cd19197b-df52-49a5-8e87-08a803691c84)

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/2ee5449e-ab2e-4bc3-af07-233a91bdd9c1)

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/aa0de55f-0779-4823-8f81-276fdecfee2c)

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/0cb5d23f-c9e6-4143-ae09-b2e104fd90e5)

### Mostrar Publicaciones
El usuario puede ver diferentes publicaciones. El usuario selecciona la publicación para generar una orden, conocer detalles sobre el vendedor o realizar una pregunta

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/b1e7ff92-fb4a-4f68-8f7e-1d84813a8434)

### Filtrar Publicaciones
El usuario puede ver diferentes publicaciones ACTIVAS a través de las categorías: Por ejemplo (Accesorios para vehículos, Belleza y cuidado personal, Construcción, Tecnología, etc.) El usuario busca la categoría que quiere ver.
El usuario también puede buscar publicaciones relacionadas a un producto, marca, etc. Por ejemplo, puede haber varias publicaciones que ofrecen el Iphone 15 Pro o cualquier dispositivo de la marca Apple. 
El usuario puede filtrar las publicaciones por precio estableciendo un rango (mayor o menor)

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/0c64a54e-5cd6-45b3-9bc2-513b707894c9)

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/adc10005-c5f3-4329-a14c-5584491d7a3a)

### Mostrar Detalle Publicación

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/16218919-d921-403b-aa6d-01e4cc4668b3)

### Historial de Visualizaciones
El usuario puede encontrar fácilmente las publicaciones de su interés que ha visto anteriormente.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/12ed17c4-e1d8-4739-b924-b45522d1a488)

### Reputación
El usuario puede consultar su reputación asi mismo puede consultar la reputación de los vendedores para medir la confiabilidad. Se calcula automáticamente en base al promedio de las estrellas vendedor de todas las órdenes. 

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/f807a166-3035-468d-bbf8-cbaa9fe2d134)

### Enviar Preguntas
El usuario cliente interesado puede enviar una pregunta al vendedor sobre una publicación

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/9c5d3293-2a7c-4a66-a84d-90a8c6bb9e82)

### Responder Preguntas
El usuario vendedor puede revisar las preguntas que hacen los clientes en cada publicación, asimismo puede enviar una respuesta

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/db8b63a2-6ba9-4880-85ca-4627b986d25e)

### Mostrar Respuestas
El usuario puede ver si le han respondido a su pregunta

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/3da0723f-dafd-4581-99dc-d5951ba382ff)

### Realizar Compra
El cliente puede crear una orden después de haber escogido la publicación de su interés. Para el efecto, el cliente debe especificar la cantidad del producto (debe verificar que haya stock). Se mostrará un valor subtotal en la aplicación, luego el cliente en caso de tener cupón selecciona el cupón registrado en la tabla Cupón y que esté disponible. Si el cliente desea que la entrega sea a domicilio debe seleccionar la dirección registrada en la BD, en caso de seleccionar. El costo de envío fijo es de $2.00, caso contrario $0.00. Mostrar la fecha de entrega estimada (5 días) Luego mostrará el importe total. El usuario puede asociar un número de tarjeta o registrar el número de transacción para validar el pago (Debe validar que el pago se encuentre en la BD y que el monto de esa transacción sea igual al importe total de la orden). Finalmente se genera la orden con fecha actual y estado pendiente.


![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/9841aec0-8ee7-4bbd-8a9e-aad83a274e6e)
![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/9791e7bd-c60d-44f6-a128-c6fe0bd94c68)

### Mis Compras
El usuario puede revisar las órdenes realizadas anteriormente

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/9bc4ce7b-22f1-40d7-aa84-916a3b7b5c36)

### Calificar Compra
El usuario cliente puede calificar la ordenes completadas, definir estrellasproducto, estrellasvendedor y un comentario.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/88c47cc0-9676-4281-ae92-134ededb6086)

### Hacer Reclamo
El usuario puede realizar un reclamo sobre una orden en cualquier estado.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/35ab1c50-0e00-4a42-8dcf-4a7bddb24359)

### Ver Reclamo
El usuario vendedor/cliente puede ver los reclamos que ha generado o que tiene que resolver y en qué estado están.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/c8e31fac-5a28-4e66-a952-cab83fd18f4d)

### Vender
Un usuario registrado puede Vender (crear una publicación) con productos que consta en la base de datos o agregar nuevos productos

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/73f94e33-885d-4ee1-9408-611b2ada3f85)
![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/e378c6cf-19a7-4a5d-a3a2-3bd9b0030c1a)


### Mis Ventas
El usuario vendedor puede ver las ventas que ha realizado.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/ee6ab062-7e60-4f28-802c-cd95ce3c941c)


### Facturas
El usuario vendedor puede emitir una factura en base a la orden realizada por una sola vez. Es opcional ya que si el cliente lo desea o lo hace por voluntad propia del vendedor. El usuario cliente debe poder ver esa factura en el sistema.

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/8717ba33-3b65-446c-bd7f-98630f838ced)

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/191ee4d1-a3be-4d54-b275-af6a72d57343)
![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/c0d25f9c-f2a8-44a6-95de-94dc47c1f8f2)


## **Menús y Submenús** <a name="id4"></a>

Opción 1: CUENTA

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/d5079b85-1b57-4b7a-800d-7a9a35486c76)


Opción 5: COMPRAS

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/b5008833-766d-43d7-ba24-de9b187d7877)


Opcion 6: VENTAS

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/dd7cac07-cdfd-49fc-bc8c-26b4d2e091c7)

Opción 8: FACTURACION

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/b6ab2e54-7125-4188-8fc1-e6fd878dfccc)

Opción 9: PUBLICACIONES

![image](https://github.com/m-alvaradox/MercadoLibre_G3/assets/96087936/186998e7-a283-4686-9865-823e4d5cca29)
