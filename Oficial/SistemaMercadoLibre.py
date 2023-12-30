#imports
import pymysql
from datetime import datetime

# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='root', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()

#funciones
def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def es_mayor_de_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad >= 18

def imprimirMenuPrincipal(nomuser):
  print("\n----- MERCADO LIBRE -----")
  print("Compra más facil y seguro")
  if nomuser == "":
     print("Bienvenido")
  else:
     cur.execute("SELECT NOMBRE FROM USUARIO WHERE USERID = '"+nomuser+"'")
     for NOMBRE in cur.fetchall():
      print("Bienvenido,",NOMBRE[0])

  print('1. Iniciar sesión')
  print('2. Crear Cuenta')
  print('3. Ver Publicaciones')
  print('4. Ver Recientes Publicaciones 2023')
  print('5. Mis Cupones')
  print('6. Productos existentes de categoria Autos')

  opcion = int(input('\nSeleccione una opcion: '))

  return opcion

def mostrarPublicaciones():
   cur.execute("SELECT NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION from PUBLICACION")
   for NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION in cur.fetchall():
    print('Publicacion #',NOPUBLICACION,
          '\nNombre: ',NOMBREPUBLICACION,
          '\nVendedor: ',IDVENDEDOR,
          '\nPrecio: ',PRECIOVENTA,
          '\nPublicado el: ',FECHAPUBLICACION,
          '\n-----------------------------------\n')
    
def mostrarPublicaciones2023():
 cur.execute("SELECT NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION from PUBLICACION WHERE YEAR(FECHAPUBLICACION) = 2023")
 for NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION in cur.fetchall():
    print('Publicacion #',NOPUBLICACION,
          '\nNombre: ',NOMBREPUBLICACION,
          '\nVendedor: ',IDVENDEDOR,
          '\nPrecio: ',PRECIOVENTA,
          '\nPublicado el: ',FECHAPUBLICACION,
          '\n-----------------------------------\n')
    
def mostrarCupones(user):
  cur.execute("SELECT ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO,CLIENTEID FROM CUPON")
  print("\nSus cupones\n")

  for ID,NOMBRE,DESCUENTO,FECHAVENCIMIENTO,CLIENTEID in cur.fetchall():
    if(CLIENTEID == user) :
          print('Cupon #',ID,
          '\nNombre: ',NOMBRE,
          '\nDescuento: ',DESCUENTO,
          '\nVence: ',FECHAVENCIMIENTO,
          '\n-----------------------------------\n')

def mostrarAccesoriosAutos():
  cur.execute("SELECT PRODUCTID, NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA FROM PRODUCTO WHERE CATEGORIA LIKE 'AUTOS'")
  for PRODUCTID, NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA in cur.fetchall():
          print('ID#',PRODUCTID,
          '\nNombre: ',NOMBRE,
          '\nMarca: ',MARCA,
          '\nCategoria: ',CATEGORIA,
          '\nSubcategoria: ',SUBCATEGORIA,
          '\n-----------------------------------\n')

def IniciarSesion():
   while True:
      userName = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contraseña: ")
      
      cur.execute("SELECT USERID,PASS FROM USUARIO WHERE USERID = '"+userName+"'")
      for USERID,PASS in cur.fetchall():
         if(userName.lower() == USERID and password == PASS):
            print("Inicio exitoso")
            return userName
      print("Usuario y/o contraseña incorrectos. Vuelva a intentarlo\n")

def CrearCuenta():
  lusuarios = []

  cur.execute("SELECT USERID FROM USUARIO")
  for USERID in cur.fetchall():
    lusuarios.append(USERID[0])

  while True:
    userName = input("Indique un nombre de usuario: ")
    if(userName in lusuarios):
      print("El usuario ya existe en el sistema, intente con otro\n")
    else:
       break

  nombre = input("Ingrese nombre: ")
  apellido = input("Ingrese apellido: ")

  while True:
    fechanacimiento = input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: ")
    if validar_fecha(fechanacimiento):
      if es_mayor_de_edad(fechanacimiento):
        break
      else:
       print("No puede registrarse debido a que es menor de edad\n")
    else:
      print("La fecha no es válida\n")

  while True:
     password = input("Ingrese su contraseña (Max. 16 caracteres): ")
     if(len(password)<16):
        break
     else:
        print("No valida, debe ser max. 16 caracteres")
        
  cur.execute("INSERT INTO USUARIO(USERID,PASS,NOMBRE,APELLIDO,FECHANACIMIENTO,ESCLIENTE,ESVENDEDOR) VALUES ('"+userName+"','"+password+"','"+nombre+"','"+apellido+"','"+fechanacimiento+"',true,false)")
  mercadolibreconnection.commit()
  print(userName,"creado exitosamente!")


       
#Programa Principal           
op = imprimirMenuPrincipal("")


if op == 1:
   usuario = IniciarSesion()
   imprimirMenuPrincipal(usuario)

if op == 2:
   CrearCuenta()

if op == 3:
  mostrarPublicaciones()

elif op == 4:
  mostrarPublicaciones2023()

elif op == 5:
  user = input("Ingrese su nombre de usuario: ")
  mostrarCupones(user)

elif op == 6:
  mostrarAccesoriosAutos()


  
  
  

  

mercadolibreconnection.close()