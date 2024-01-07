from flask import Flask

#Funciones principales
def imprimirMenuPrincipal():
  print("\n----- MERCADO LIBRE -----")
  print("Compra más facil y seguro")
  print('\nSeleccione una opcion del menu principal:')
  print('1. Explorar Productos')
  print('2. Ver Carrito de Compras')
  print('3. Realizar Pedido')
  print('4. Ver Historial de Compras')
  print('5. Vender')
  print('6. Ayuda')
  print('7. Cerrar Sesión')
  print('8. Más Opciones')

def imprimirMenuPrincipalUsuario():
  print('Bienvenido a Mercado Libre' + '\n' + 'Seleccione una opcion del menu principal:')
  print('1. Iniciar Sesión')
  print('2. Crear Cuenta')
  print('3. Explorar Productos')
  print('4. Ver Carrito de Compras')
  print('5. Realizar Pedido')
  print('6. Ver Historial de Compras')
  print('7. Vender')
  print('8. Ayuda')
  print('9. Más Opciones')

def verificarCadenaVacia(lista):
  for i in lista:
    if i == '':
      return True
  return False

#Aplicacion - Iniciar Sesion
mercadoLibre = pymysql.connect(host='localhost', user='root', password='', db='mercado_libre')

a = mercadoLibre.cursor()
sinUsuario = ''
while (sinUsuario != 'salir'):
  a.execute('SELECT USER_ID FROM USUARIO')
  lista = []
  for USER_ID in a.fetchall():
    lista.append(str(USER_ID))
  funciones.imprimirMenuPrincipalUsuario()
  sinUsuario = input("Escoja una opcion del menu(1 - 9) o ingrese salir para abandonar la aplicacion: ")
  if (sinUsuario == '1'):
    userName = ''
    i = 0
    while (userName not in lista):
      if i == 0:
        userName = input("Ingrese su nombre de usuario: ")
      else:
        userName = input("Ingrese un nombre de usuario válido: ")
      i += 1
    a.execute('SELECT PASSWORD FROM USUARIO WHERE USER_ID = %s', (userName,))
    consulta = a.fetchone()
    password = ''
    j = 0
    while (password != consulta[0]):
      print(userName)
      if j == 0:
        password = input("Ingrese su contraseña: ")
      else:
        password = input("Ingrese una contraseña válida: ")
      j+= 1
    print('Ingreso exitoso a la aplicacion, puede continuar')
    sinUsuario = 'salir'
  elif (sinUsuario == '2'):
    userName = input('Ingrese su nombre de usuario (campo obligatorio): ')
    password = input('Ingrese su contraseña (campo obligatorio): ')
    nombre = input('Ingrese su nombre (campo obligatorio): ')
    apellido = input('Ingrese su apellido (campo obligatorio): ')
    fechaNacimiento = input('Ingrese su fecha de nacimiento (DD/MM/AAAA - campo obligatorio): ')
    cliente = bool(input('Ingrese si desea ser cliente (True / False): '))
    vendedor = bool(input('Ingrese si desea ser vendedor (True / False): '))
    listaCadenas = [userName, password, nombre, apellido, fechaNacimiento, cliente, vendedor]
    while (userName in lista or (funciones.verificarCadenaVacia(listaCadenas))):
      if userName in lista and funciones.verificarCadenaVacia(listaCadenas):
        userName = input("Ese nombre de usuario ya existe, ingrese uno nuevo: ")
        password = input('Ingrese su contraseña (campo obligatorio): ')
        nombre = input('Ingrese su nombre (campo obligatorio): ')
        apellido = input('Ingrese su apellido (campo obligatorio): ')
        fechaNacimiento = input('Ingrese su fecha de nacimiento (DD/MM/AAAA - campo obligatorio): ')
        cliente = bool(input('Ingrese si desea ser cliente (True / False): '))
        vendedor = bool(input('Ingrese si desea ser vendedor (True / False): '))
        listaCadenas = [userName, password, nombre, apellido, fechaNacimiento, cliente, vendedor]
      elif userName in lista:
        userName = input("Ese nombre de usuario ya existe, ingrese uno nuevo: ")
      else:
        password = input('Ingrese su contraseña (campo obligatorio): ')
        nombre = input('Ingrese su nombre (campo obligatorio): ')
        apellido = input('Ingrese su apellido (campo obligatorio): ')
        fechaNacimiento = input('Ingrese su fecha de nacimiento (DD/MM/AAAA - campo obligatorio): ')
        cliente = bool(input('Ingrese si desea ser cliente (True / False): '))
        vendedor = bool(input('Ingrese si desea ser vendedor (True / False): '))
        listaCadenas = [userName, password, nombre, apellido, fechaNacimiento, cliente, vendedor]
    a.execute('INSERT INTO USUARIO (USER_ID, PASSWORD, NOMBRE, APELLIDO, FECHA_NACIMIENTO, ES_CLIENTE, ES_VENDEDOR) VALUES (?, ?, ?, ?, ?, ?, ?)', (userName, password, nombre, apellido, fechaNacimiento, cliente, vendedor,))
    mercadoLibre.commit()
    print('!Su cuenta ha sido creada exitosamente, se lo redirigirá al menú principal¡')
  else:
    print('Primero debes iniciar sesion, o crear una cuenta para poder acceder a las diferentes opciones')

a.execute('SELECT NOMBRE, MARCA, CATEGORIA, PRECIO FROM PRODUCTO')
usuario = ''
while (usuario != 'salir'):
  funciones.imprimirMenuPrincipal()
  usuario = input("Escoja una opcion del menu(1 - 8) o ingrese salir para abandonar la aplicacion: ")
  if (usuario == '1'):
    a.execute()
    for NOMBRE, MARCA, CATEGORIA, PRECIO in a.fetchall():
      print('Nombre del producto: ' + NOMBRE, 'Marca: ' + MARCA, 'Categoria: ' + CATEGORIA, 'Precio: ' + PRECIO)

#Aplicacion - Ver publicaciones (vista del cliente)
def listarAtributosClientes(cur):
  categorias = []
  productos = []
  marcas = []
  vendedores = []
  cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE ESTADO = ACTIVA")
  for CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, PRECIOVENTA, IDVENDEDOR, STOCK, FECHAPUBLICACION in cur.fetchall():
    categorias.append(CATEGORIA)
    productos.append(PRODUCTO.NOMBRE)
    marcas.append(PRODUCTO.MARCA)
    vendedores.append(IDVENDEDOR)
  return categorias, productos, marcas, vendedores

def mostrarPublicacionCliente(cur):
  cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE ESTADO = ACTIVA")
  for CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, PRECIOVENTA, IDVENDEDOR, STOCK, FECHAPUBLICACION in cur.fetchall():
    print('Categoria:', CATEGORIA,
          '\nNombre:',NOMBREPUBLICACION,
          '\nProducto:',PRODUCTO.NOMBRE,
          '\nMarca:',PRODUCTO.MARCA,
          '\nDescripcion:',DESCRIPCION,
          '\nPrecio:',PRECIOVENTA,
          '\nVendedor:',IDVENDEDOR,
          '\nStock:',STOCK,
          '\nPublicado el:',FECHAPUBLICACION,
          '\n-----------------------------------')

def mostrarPublicacionProductoMarca(prod=None, marc=None, categ=None, vend=None, ord=None, prec=None, ord_price=None, cur):
  print("\n-- PUBLICACIONES --\n")
  categorias, productos, marcas, vendedores= listarAtributosClientes(cur)
  consulta = "SELECT PRODUCTO.CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE ESTADO = ACTIVA"
  contador = 0
  if prod is not None and prod in productos:
    consulta += f" AND PRODUCTO.NOMBRE = '{prod}'"
    contador += 1
  if marc is not None and marc in marcas:
    consulta += f" AND PRODUCTO.MARCA = '{marc}'"
    contador += 1
  if categ is not None and categ in categorias:
    consulta += f" AND PRODUCTO.CATEGORIA = '{categ}'"
    contador += 1
  if vend is not None and vend in vendedores:
    consulta += f" AND IDVENDEDOR = '{vend}'"
    contador += 1
  if prec is not None and ord_price is not None:
    if ord_price == "Mayor":
      consulta += f"AND PRECIOVENTA >= '{prec}'"
      contador += 1
    elif ord_price == "Menor":
      consulta += f"AND PRECIOVENTA <= '{prec}'"
      contador += 1
  if ord is not None:
    if ord == "Mas reciente":
      consulta += " ORDER BY FECHAPUBLICACION DESC"
      contador += 1
    elif ord == "Mas antigua":
      consulta += "ORDER BY FECHAPUBLICACION ASC"
      contador += 1
      
  if contador == 0:
    mostrarPublicacionCliente(cur)
  
  cur.execute(consulta)
  for CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, PRECIOVENTA, IDVENDEDOR, STOCK, FECHAPUBLICACION in cur.fetchall():
    print('Categoria:', CATEGORIA,
          '\nNombre:',NOMBREPUBLICACION,
          '\nProducto:',PRODUCTO.NOMBRE,
          '\nMarca:',PRODUCTO.MARCA,
          '\nDescripcion:',DESCRIPCION,
          '\nPrecio:',PRECIOVENTA,
          '\nVendedor:',IDVENDEDOR,
          '\nStock:',STOCK,
          '\nPublicado el:',FECHAPUBLICACION,
          '\n-----------------------------------')

#
def pregunta(idCliente, cur):
  print("Si quiere saber mas sobre una publicacion, puede hacerle una pregunta al vendedor.")
  val = input("¿Tiene alguna pregunta sobre una publicación que le interesa? (Si/No) -> " )
  while ( val == "Si"):
    vendedor = input("Ingrese el nombre del vendedor: ")
    publicacion = input("Ingrese el nombre de la publicacion: ")
    producto = input("Ingrese el atributo (producto) sobre el que desea consultarle: ")
    mensaje = input("Ingrese el contenido del mensaje que desea enviarle al vendedor:\n")
    cur.execute("SELECT IDVENDEDOR, NOMBREPUBLICACION, PRODUCTO.NOMBRE FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE ESTADO = ACTIVA")
    lista = []
    for IDVENDEDOR, NOMBREPUBLICACION, PRODUCTO.NOMBRE in cur.fetchall():
      lista.append(IDVENDEDOR)
      lista.append(NOMBREPUBLICACION)
      lista.append(PRODUCTO.NOMBRE)
    i = 0
    while (lista[i] != vendedor and lista[i + 1] != publicacion and lista[i + 2] != producto):
      if i > len(lista):
        i = 0
        print("Ingrese datos validos para enviar correctamente la pregunta.\nVerifique el nombre del vendedor, el de la publicacion y el del atributo por el que pregunta.")
        vendedor = input("Ingrese el nombre del vendedor: ")
        publicacion = input("Ingrese el nombre de la publicacion: ")
        producto = input("Ingrese el atributo (producto) sobre el que desea consultarle: ")
        mensaje = input("Ingrese el contenido del mensaje que desea enviarle al vendedor:\n")
      i += 3
    
    cur.execute(f"SELECT NOPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE ESTADO = ACTIVA AND IDVENDEDOR = '{vendedor}' AND NOMBREPUBLICACION = {publicacion} AND PRODUCTO.NOMBRE = {producto}")
    noPublicacion = ''
    for NOPUBLICACION in cur.fetchall():
      noPublicacion = NOPUBLICACION
    cur.execute("INSERT INTO PREGUNTA (CONTENIDO, TIEMPOENVIADO, IDCLIENTE, IDVENDEDOR, NOPUBLICACION) VALUES (%s, %s, %s, %s)", (mensaje, datetime.now(), idCliente, vendedor))
    mercadolibre.commit()
    print("La pregunta ha sido enviada correctamente.\n")
    val = input("¿Tiene alguna otra pregunta sobre una publicación que le interesa? (Si/No) -> " )
  print("Muchas gracias por su tiempo, esperemos que sus dudas sean resueltas lo mas pronto posible.\nLe deseamos un excelente dia.")


           
        
        
       
    

  
