import pymysql

def imprimirMenuPrincipal():
  print("\n----- MERCADO LIBRE -----")
  print("Compra más facil y seguro")
  print('1. Ver Publicaciones')
  print('2. Ver Recientes Publicaciones 2023')
  print('3. Mis Cupones')
  print('4. Productos existentes de categoria Autos')
  opcion = int(input('\nSeleccione una opcion: '))

  return opcion

def mostrarPublicaciones(cursor):
   cur.execute("SELECT NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION from PUBLICACION")
   for NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION in cur.fetchall():
    print('Publicacion #',NOPUBLICACION,
          '\nNombre: ',NOMBREPUBLICACION,
          '\nVendedor: ',IDVENDEDOR,
          '\nPrecio: ',PRECIOVENTA,
          '\nPublicado el: ',FECHAPUBLICACION,
          '\n-----------------------------------\n')
    
def mostrarPublicaciones2023(cursor):
 cur.execute("SELECT NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION from PUBLICACION WHERE YEAR(FECHAPUBLICACION) = 2023")
 for NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION in cur.fetchall():
    print('Publicacion #',NOPUBLICACION,
          '\nNombre: ',NOMBREPUBLICACION,
          '\nVendedor: ',IDVENDEDOR,
          '\nPrecio: ',PRECIOVENTA,
          '\nPublicado el: ',FECHAPUBLICACION,
          '\n-----------------------------------\n')
    
def mostrarCupones(cursor, user):
  cur.execute("SELECT ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO,CLIENTEID FROM CUPON")
  print("\nSus cupones\n")

  for ID,NOMBRE,DESCUENTO,FECHAVENCIMIENTO,CLIENTEID in cur.fetchall():
    if(CLIENTEID == user) :
          print('Cupon #',ID,
          '\nNombre: ',NOMBRE,
          '\nDescuento: ',DESCUENTO,
          '\nVence: ',FECHAVENCIMIENTO,
          '\n-----------------------------------\n')

def mostrarAccesoriosAutos(cursor):
  cur.execute("SELECT PRODUCTID, NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA FROM PRODUCTO WHERE CATEGORIA LIKE 'AUTOS'")
  for PRODUCTID, NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA in cur.fetchall():
          print('ID#',PRODUCTID,
          '\nNombre: ',NOMBRE,
          '\nMarca: ',MARCA,
          '\nCategoria: ',CATEGORIA,
          '\nSubcategoria: ',SUBCATEGORIA,
          '\n-----------------------------------\n')


mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'password123', db='mercadolibre')
cur = mercadolibreconnection.cursor()

#Menu Principal Mercado Libre

op = imprimirMenuPrincipal()

# Mostrar todas las publicaciones

if op == 1:
  mostrarPublicaciones(cur)

elif op == 2:
  mostrarPublicaciones2023(cur)

elif op == 3:
  user = input("Ingrese su nombre de usuario: ")
  mostrarCupones(cur,user)

elif op == 4:
  mostrarAccesoriosAutos(cur)


  
  
  

  

mercadolibreconnection.close()
