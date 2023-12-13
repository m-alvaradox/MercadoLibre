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

mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'password123', db='rent_car')
cur = mercadolibreconnection.cursor()
#cur.execute("select VIN, Model from car")

imprimirMenuPrincipal()

mercadolibreconnection.close()
