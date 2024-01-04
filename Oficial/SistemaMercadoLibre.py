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
from datetime import datetime, date, timedelta

# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='invitado', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()

#funciones

def opcionnumerica():
   while True:
      option = input("Ingrese opcion: ")
      if(option.isnumeric()):
         return option
      else:
         print("Opcion incorrecta, vuelva a intentar")
   
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
     telefono = input("Ingrese su numero de telefono (10 digitos): ")
     if(len(telefono)==10):
        break
     else:
        print("Error, vuelva a intentar\n")

  while True:
     email = input("Ingrese su correo (ej. 'usuario@dominio.com'): ")
     separ = email.split('@')
     sepun = email.split('.')
     if('@' in email and len(separ)==2 and '.' in email and len(sepun)==2):
        break
     else:
        print("Incorrecto, vuelva a intentarlo\n")

  while True:
     password = input("Ingrese su contraseña (Max. 16 caracteres): ")
     if(len(password)<16):
        break
     else:
        print("No valida, debe ser max. 16 caracteres")
        
  cur.execute("INSERT INTO USUARIO(USERID,PASS,NOMBRE,APELLIDO,FECHANACIMIENTO,ESCLIENTE,ESVENDEDOR,EMAIL,TELEFONO) VALUES ('"+userName+"','"+password+"','"+nombre+"','"+apellido+"','"+fechanacimiento+"',true,false,'"+email+"','"+telefono+"')")
  cur.execute("INSERT INTO CLIENTE VALUES ('"+userName+"')")
  mercadolibreconnection.commit()
  print(userName,"creado exitosamente!")

  return userName

def AccionarInvitado(opcion):
    
    if opcion == 0:
      print("Adios")
      exit()

    if opcion == 1:
        usuario = IniciarSesion()
        imprimirMenuPrincipalUsuario(usuario)

    if opcion == 2:
       usuario = CrearCuenta()
       imprimirMenuPrincipalUsuario(usuario)

    if opcion == 3:
       mostrarPublicaciones()
       print("\nPara generar una orden, debe iniciar sesión o crear una cuenta en Mercado Libre")

    if opcion == 4:
       mostrarPublicaciones2023()

    if opcion == 5:
       mostrarAccesoriosAutos()


def AccionarUsuario(opcion,user):
    
    if opcion == 0:
       print("Adios")
       exit()
       
    if opcion == 1:
      print("Sesion cerrada exitosamente")
      imprimirMenuPrincipalInvitado()

    if opcion == 2:
       mostrarPublicaciones()
       print("\nSeleccione la publicacion de su interés\nPara SALIR digite 0")
       pub = opcionnumerica()

       if(pub == "0"):
          return
       else:
          generarOrden(pub,user)

    if opcion == 3:
       mostrarPublicaciones2023()

    if opcion == 4:
       mostrarAccesoriosAutos()

    if opcion == 5:
       mostrarCupones(user)

    if opcion == 6:
       mostrarPerfil(user)
       
      
def mostrarcaratula():
   print("\n----- MERCADO LIBRE -----")
   print("Compra más facil y seguro")

def imprimirMenuPrincipalInvitado():
    op = ""
    while op !=0:
        mostrarcaratula()
        print("Hola!")
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
       cur.execute("SELECT NOMBRE FROM USUARIO WHERE USERID = '"+nomuser+"'")
       mostrarcaratula()
       print("Hola!",cur.fetchone()[0])
       print('1. Cerrar Sesion')
       print('2. Ver Publicaciones')
       print('3. Ver Recientes Publicaciones 2023')
       print('4. Productos existentes de categoria Autos')
       print('5. Mis Cupones')
       print('6. Mi Perfil')
       print('0. SALIR')
       op = validaropcion(0,6)
       AccionarUsuario(op,nomuser)

def mostrarPublicaciones():
   cur.execute("SELECT NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION, STOCK from PUBLICACION")
   print("\n-- PUBLICACIONES --\n")
   for NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION, STOCK in cur.fetchall():
    print('Publicacion #',NOPUBLICACION,
          '\nNombre:',NOMBREPUBLICACION,
          '\nVendedor:',IDVENDEDOR,
          '\nPrecio:',PRECIOVENTA,
          '\nStock:',STOCK,
          '\nPublicado el:',FECHAPUBLICACION,
          '\n-----------------------------------')
   

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
  cur.execute("SELECT ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO,CLIENTEID, VECES FROM CUPON WHERE CLIENTEID ='"+user+"'")
  resultado = cur.fetchall()

  if(len(resultado) == 0):
     print("No tiene cupones disponibles")
     return
  else:
     print("\nSus cupones\n")

  for ID,NOMBRE,DESCUENTO,FECHAVENCIMIENTO,CLIENTEID, VECES in resultado:
          print('Cupon #',ID,
          '\nNombre:',NOMBRE,
          '\nDescuento:',DESCUENTO,
          '\nVence:',FECHAVENCIMIENTO,
          '\nPuede usarlo:',VECES,'veces',
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

def mostrarPerfil(user):
   print("--Mi Perfil--")

   cur.execute ("SELECT USERID, EMAIL, NOMBRE, APELLIDO, TELEFONO FROM USUARIO WHERE USERID = '"+user+"'")
   detalleperfil = cur.fetchone()

   print("\n--Datos de cuenta")
   print("Usuario:",detalleperfil[0])
   print("Email:",detalleperfil[1])

   print("\n--Datos personales")
   print("Nombre y Apellido:",detalleperfil[2],detalleperfil[3])
   print("Telefono:",detalleperfil[4])

def mostrarDirecciones(user):
   cur.execute("SELECT ID, PARROQUIA, REFERENCIAS, NOMBRECIUDAD, NOMBREPROVINCIA, NOMBREPAIS"+
               " FROM DIRECCION JOIN CIUDAD ON IDCIUDAD=CITYID NATURAL JOIN PROVINCIA NATURAL JOIN PAIS"+
               " WHERE USERID = '"+user+"'")
   
   print("Sus direcciones registradas\n")
   contador = 1
   for ID,PARROQUIA,REFERENCIAS,NOMBRECIUDAD,NOMBREPROVINCIA,NOMBREPAIS in cur.fetchall():
      print("-- Direccion #",contador)
      print(PARROQUIA+",",REFERENCIAS)
      print(NOMBRECIUDAD+","+NOMBREPROVINCIA+","+NOMBREPAIS+"\n")
      contador += 1

def generarOrden(nopublicacion, user):
    

    
    fecha_actual = date.today()

    cur.execute("SELECT NOMBREPUBLICACION, STOCK, PRECIOVENTA, PRODUCTID, IDVENDEDOR FROM PUBLICACION WHERE NOPUBLICACION ="+str(nopublicacion)+"")
    detallespublicacion = cur.fetchone()

    if(detallespublicacion == None):
       print("\nPublicacion no encontrada!")
       return
    
    print("\n-- GENERAR ORDEN --")

    while True:
        cantidad = int(input("Ingrese la cantidad deseada: "))
        if cantidad <= detallespublicacion[1]:
            break
        else:
            print("Sin stock\n")

    print("Como desea la entrega?\n"+
          "1.Entrega a domicilio (Entrega en 5 dias)\n"+
          "2.Entrega a acordar con el vendedor")
    
    op = validaropcion(1,2)

    direccionid=None
    fechaentrega = None
    costoenvio = 0

    if op == 1:
       mostrarDirecciones(user)
       opc = int(input("Seleccione direccion: "))
       cur.execute("SELECT ID FROM DIRECCION WHERE USERID = '"+user+"'")
       direccionid = cur.fetchall()[opc-1][0]
       costoenvio = 2
       fechaentrega = date.today() + timedelta(days=5)

       
    
    subtotal = detallespublicacion[2] * cantidad
    total = subtotal + costoenvio
    print("Usted desea adquirir:",detallespublicacion[0])
    print("Cantidad:",cantidad)
    print("Subtotal:",subtotal)
    print("Costo envio:",costoenvio)
    print("Total:",total)
    print("Fecha de Entrega estimada:",fechaentrega)

    print("\nDesea ingresar cupon? 1. SI 2. NO")
    op2 = validaropcion(1,2)
    idCupon = None
    descuento = 0

    if op2==1:
       mostrarCupones(user)
       while True:
         opc2 = input("\nEscribe el numero del cupón: ")
         cur.execute("SELECT ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO,CLIENTEID, VECES FROM CUPON WHERE CLIENTEID ='"+user+"' AND ID = "+str(opc2)+"")
         detallescupon = cur.fetchone()

         if (detallescupon == None):
            print("Intente de nuevo")
         else:
            if(detallescupon[3] <= fecha_actual or detallescupon[5] == 0):
               print("Cupón vencido o usado, ingrese otro cupón\n")
            else:
               idCupon = detallescupon[0]
               descuento = subtotal * (detallescupon[2]/100)
               total = subtotal + costoenvio - descuento
               print("Cupon ingresado correctamente")
               print("\nUsted desea adquirir:",detallespublicacion[0])
               print("Cantidad:",cantidad)
               print("Subtotal:",subtotal)
               print("Costo envio (+):",costoenvio)
               print("Descuento "+str(int(detallescupon[2]))+"% (-):",descuento)
               print("Total:",total)
               print("Fecha de Entrega estimada:",fechaentrega)
               break

    print("\nDesea proceder con la compra? 1.SI 2.NO ")
    op3 = validaropcion(1,2)

    if op3 == 1:
      print("\n-- PAGO")
      while True:
         trans = input("Asocie un numero de transaccion para generar la orden: ")
         cur.execute("SELECT TRANSID, METODO, MONTO, CUOTA, CARDNUMBER FROM PAGO WHERE TRANSID = "+trans+" AND MONTO = "+str(total)+" AND IDCLIENTE = '"+user+"'")
         detallespago = cur.fetchone()

         print("Validando Transaccion...")

         registropagos = []
         cur.execute("SELECT IDPAGO FROM ORDEN")
         for IDPAGO in cur.fetchall():
            registropagos.append(IDPAGO[0])
         
         if (detallespago == None or (int(trans) in registropagos)):
            print("Lo sentimos, no tiene ningún pago asociado por el momento o fue usado en otra orden, intente de nuevo\n")
         else:
            print("\n--- Transaccion valida")
            print("\nDetalles de la transaccion:")
            print("No.Transaccion:",detallespago[0])
            print("Metodo:",detallespago[1])
            print("Monto:",detallespago[2])
            print("Cuota:",detallespago[3])
            print("Tarjeta No.",detallespago[4])

            print("\nGenerando orden...")

            if(idCupon == None):
               idCupon = 'NULL'
            
            if(direccionid == None):
               direccionid = 'NULL'

            if(fechaentrega == None):
               fechaentrega = 'NULL'
            else:
               fechaentrega = "'"+fechaentrega.strftime('%Y-%m-%d')+"'"


            
            fecha_actual_str = fecha_actual.strftime('%Y-%m-%d')
            


            cur.execute("INSERT INTO ORDEN (FECHACREACION,ESTADO,IDCUPON,PRODUCTID,IDPAGO,CANTIDADPRODUCTO,IDPUBLICACION,IDCLIENTE,IDVENDEDOR,IMPORTE,IDDIRECCION,COSTOENVIO,FECHAENTREGA) VALUES "+
                        "('"+fecha_actual_str+"','Pendiente',"+str(idCupon)+","+str(detallespublicacion[3])+","+str(detallespago[0])+","+str(cantidad)+","+str(nopublicacion)+",'"+user+"','"+detallespublicacion[4]+"',"+str(total)+","+str(direccionid)+","+str(costoenvio)+","+fechaentrega+")")
            
            mercadolibreconnection.commit()

            cur.execute("SELECT ORDERID FROM ORDEN WHERE IDCLIENTE = '"+user+"' ORDER BY ORDERID DESC LIMIT 1")
            ordenes = cur.fetchone()
            print("Orden",ordenes[0],"realizada con éxito!")
            print("Gracias por comprar en Mercado Libre :)")
            break

#Programa Principal
imprimirMenuPrincipalInvitado()


mercadolibreconnection.close()