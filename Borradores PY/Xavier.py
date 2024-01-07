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
  precios = []
  cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE CATEGORIA = %s AND ESTADO = ACTIVA", (categoria,))
  for CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, PRECIOVENTA, IDVENDEDOR, STOCK, FECHAPUBLICACION in cur.fetchall():
    categorias.append(CATEGORIA)
    productos.append(PRODUCTO.NOMBRE)
    marcas.append(PRODUCTO.MARCA)
    vendedores.append(IDVENDEDOR)
    precios.append(PRECIOVENTA)
  return categorias, productos, marcas, vendedores, precios

def mostrarPublicacionCliente(cur):
  cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE CATEGORIA = %s AND ESTADO = ACTIVA", (categoria,))
  print("\n-- PUBLICACIONES --\n")
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
  
def mostrarPublicacionCategoria(categoria, cur):
  cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE CATEGORIA = %s", (categoria,))
  print("\n-- PUBLICACIONES --\n")
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

def mostrarPublicacionOrdFecha(arg, cur):
  if (arg == "Mas reciente"):
    cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO ORDER BY FECHAPUBLICACION DESC")
    print("\n-- PUBLICACIONES --\n")
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
  elif (arg == "Mas antigua"):
    cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO ORDER BY FECHAPUBLICACION ASC")
    print("\n-- PUBLICACIONES --\n")
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
  else:
    mostrarPublicacionCliente(cur)

def mostrarPublicacionProductoMarca(prod, marc, categ, vend, ord, prec, ord_price, cur):
  print("\n-- PUBLICACIONES --\n")
  categorias, productos, marcas, vendedores, precios = listarAtributosClientes(cur)
  if ((prod in productos) and (marc in marcas) and (categ in categorias) and (vend in vendedores) and (ord == "Mas reciente") and (prec in precios) and (ord_price == "Mayor")):
    cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE CATEGORIA = %s AND ESTADO = ACTIVO AND PRODUCTO.NOMBRE = %s AND PRODUCTO.MARCA = %s AND IDVENDEDOR = %s AND PRECIOVENTA >= %s ORDER BY FECHAPUBLICACION DESC", (categ, prod, marc, vend, prec))
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
  elif ((prod in productos) and (marc in marcas) and (categ in categorias) and (vend in vendedores) and (ord == "Mas antiguo") and (prec in precios) and (ord_price == "Menor")):
    cur.execute("SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION NATURAL JOIN PRODUCTO WHERE CATEGORIA = %s AND ESTADO = ACTIVO AND PRODUCTO.NOMBRE = %s AND PRODUCTO.MARCA = %s AND IDVENDEDOR = %s AND PRECIOVENTA <= %s ORDER BY FECHAPUBLICACION ASC", (categ, prod, marc, vend, prec))
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
    
