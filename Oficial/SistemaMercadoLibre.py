import pymysql

# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='root', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()

def imprimirMenuPrincipal():
  print("\n----- MERCADO LIBRE -----")
  print("Compra más facil y seguro")
  print('1. Iniciar sesión')
  print('2. Crear Cuenta')
  print('3. Ver Publicaciones')
  print('4. Ver Recientes Publicaciones 2023')
  print('5. Mis Cupones')
  print('6. Productos existentes de categoria Autos')

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

def IniciarSesion(cursor):
   while True:
      userName = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contraseña: ")
      
      cur.execute("SELECT USERID,PASS FROM USUARIO WHERE USERID = '"+userName+"'")
      for USERID,PASS in cur.fetchall():
         if(userName == USERID and password == PASS):
            print("Inicio exitoso")
            return
         
            
               


op = imprimirMenuPrincipal()


if op == 1:
   IniciarSesion(cur)

if op == 3:
  mostrarPublicaciones(cur)

elif op == 4:
  mostrarPublicaciones2023(cur)

elif op == 5:
  user = input("Ingrese su nombre de usuario: ")
  mostrarCupones(cur,user)

elif op == 6:
  mostrarAccesoriosAutos(cur)


  
  
  

  

mercadolibreconnection.close()
