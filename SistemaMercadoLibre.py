import pymysql

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




mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'password123', db='rent_car')
cur = mercadolibreconnection.cursor()
#cur.execute("select VIN, Model from car")


mercadolibreconnection.close()



imprimirMenuPrincipal()
