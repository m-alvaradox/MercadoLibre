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
def mostrarPublicacionCategoria(categoria, cur):
  cur.execute()
