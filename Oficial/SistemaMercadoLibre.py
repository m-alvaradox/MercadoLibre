"""
Sistema de Mercado Libre
Integrantes Grupo #6
- Mario Alvarado
- Xavier Camacho
- Javier Rodriguez
- Owuen Yagual
"""
#imports
import pymysql
from datetime import datetime

# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='invitado', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()

#funciones
   
def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validaropcion(desde,hasta):
   while True:
    opcion = input('\nSeleccione una opcion: ')
    if(opcion.isnumeric() and int(opcion) >=desde and int(opcion) <=hasta):
       if(int(opcion) == 0):
          print("Adios")
          exit()
       return int(opcion)
    else:
       print("Opcion incorrecta, vuelva a intentar")
    
def es_mayor_de_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad >= 18

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

  return userName

def AccionarInvitado(opcion):
    if opcion == 1:
        usuario = IniciarSesion()
        imprimirMenuPrincipalUsuario(usuario)

    if opcion == 2:
       usuario = CrearCuenta()
       imprimirMenuPrincipalUsuario(usuario)

    if opcion == 3:
       mostrarPublicaciones()

    if opcion == 4:
       mostrarPublicaciones2023()

    if opcion == 5:
       mostrarAccesoriosAutos()


def AccionarUsuario(opcion,user):
    if opcion == 1:
      print("Sesion cerrada exitosamente")
      imprimirMenuPrincipalInvitado()

    if opcion == 2:
       mostrarPublicaciones()

    if opcion == 3:
       mostrarPublicaciones2023()

    if opcion == 4:
       mostrarAccesoriosAutos()

    if opcion == 5:
       mostrarCupones(user)
      
def mostrarcaratula():
   print("\n----- MERCADO LIBRE -----")
   print("Compra más facil y seguro")

def imprimirMenuPrincipalInvitado():
    op = ""
    while op !=0:
        mostrarcaratula()
        print("Bienvenido")
        print('1. Iniciar sesión')
        print('2. Crear Cuenta')
        print('3. Ver Publicaciones')
        print('4. Ver Recientes Publicaciones 2023')
        print('6. Productos existentes de categoria Autos')
        print('0. SALIR')
        op = validaropcion(0,6)
        AccionarInvitado(op)
    

def imprimirMenuPrincipalUsuario(nomuser):
    op = ""
    while op !=0:
       mostrarcaratula()
       cur.execute("SELECT NOMBRE FROM USUARIO WHERE USERID = '"+nomuser+"'")
       for NOMBRE in cur.fetchall():
          print("Bienvenido,",NOMBRE[0])
          print('1. Cerrar Sesion')
          print('2. Ver Publicaciones')
          print('3. Ver Recientes Publicaciones 2023')
          print('4. Productos existentes de categoria Autos')
          print('5. Mis Cupones')
          print('0. SALIR')
          op = validaropcion(0,6)
          AccionarUsuario(op,nomuser)

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
  cur.execute("SELECT ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO,CLIENTEID FROM CUPON WHERE CLIENTEID ='"+user+"'")
  resultado = cur.fetchall()

  if(len(resultado) == 0):
     print("No tiene cupones disponibles")
     return
  else:
     print("\nSus cupones\n")

  for ID,NOMBRE,DESCUENTO,FECHAVENCIMIENTO,CLIENTEID in resultado:
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




       
#Programa Principal
imprimirMenuPrincipalInvitado()


mercadolibreconnection.close()