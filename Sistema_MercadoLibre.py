"""
Sistema de Mercado Libre
Integrantes Grupo #3
- Mario Alvarado
- Xavier Camacho
- Javier Rodriguez
- Owuen Yagual
"""
#imports
import pymysql
from datetime import datetime, date, timedelta
import os
import time
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="localhost", user='invitado', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()

#funciones

def limpiarPantalla():
  if os.name == "posix":
   os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system ("cls")

def opcionnumerica():
   while True:
      option = input("Ingrese: ")
      if(option.isnumeric()):
         return option
      else:
         print("Opcion incorrecta, vuelva a intentar\n")
   
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
      print("-- INICIAR SESION --")
      print("Inicie sesion con sus credenciales, ENTER para salir")
      userName = input("\nIngrese su nombre de usuario: ")

      if userName == "":
         limpiarPantalla()
         return   

      password = input("Ingrese su contraseña: ")

      if password == "":
         limpiarPantalla()
         return   
      
      cur.execute("SELECT USERID,PASS FROM USUARIO WHERE USERID = '"+userName+"'")
      for USERID,PASS in cur.fetchall():
         if(userName.lower() == USERID and password == PASS):
            limpiarPantalla()
            print("Inicio exitoso")
            return userName
      
      limpiarPantalla()
      print("Usuario y/o contraseña incorrectos. Vuelva a intentarlo\n")

def CrearCuenta():
  print("-- CREAR CUENTA --") 
  lusuarios = []

  cur.execute("SELECT USERID FROM USUARIO")
  for USERID in cur.fetchall():
    lusuarios.append(USERID[0])

  print("\n-- Crear usuario")
  print("ENTER para salir\n")
  while True:
    userName = input("Indique un nombre de usuario: ")
    if userName == "":
       limpiarPantalla()
       return
    
    condletras = False

    for caracter in userName:
       if (caracter.isalpha()):
          condletras = True
    
    if(condletras == True):
      userName = userName.lower() #new
      if(userName in lusuarios):
         print("El usuario ya existe en el sistema, intente con otro\n")
      else:
         break
    else:
      print("El usuario debe tener al menos una letra\n")

  print("\n-- Datos personales")
  print("Enter para SALIR")
  while True:
   nombre = input("\nIngrese nombre: ")

   if nombre == "":
      limpiarPantalla()
      return
  
   cond = True

   for c in nombre:
      if c == " " or nombre.isalpha() == False:
         cond = False

   if cond == True:
      break
   else:
      print("Nombre debe contener solo letras y no debe haber espacios")

  nombre = nombre.capitalize() 
  
  while True:
   apellido = input("\nIngrese apellido: ")

   if apellido == "":
      limpiarPantalla()
      return
   
   cond2 = True

   for i in apellido:
      if i == " " or apellido.isalpha() == False:
         cond2 = False
   
   if cond2 == True:
      break
   else:
      print("Apellido debe contener solo letras y no debe haber espacios")

  apellido = apellido.capitalize()
  while True:
    fechanacimiento = input("\nIngrese su fecha de nacimiento en formato YYYY-MM-DD: ")
    
    if fechanacimiento == "":
       limpiarPantalla()
       return

    if validar_fecha(fechanacimiento):
      if es_mayor_de_edad(fechanacimiento):
        break
      else:
       print("No puede registrarse debido a que es menor de edad\n")
    else:
      print("La fecha no es válida\n")

  print("\n-- Autoidentificacion de genero")
  print("1. Masculino")
  print("2. Femenino")
  print("3. LGBTI")
  print("0. SALIR")
  
  optgen = validaropcion(0,3)
  genero = None

  if optgen == 0:
     limpiarPantalla()
     return
  
  if optgen == 1:
     genero = 'Masculino'

  if optgen == 2:
     genero = 'Femenino'

  if optgen == 3:
     genero = 'LGBTI'
     
  
  print("\n-- Datos de contacto")
  print("ENTER para SALIR\n")

  while True:
     telefono = input("Ingrese su numero de telefono (10 digitos): ")

     if telefono == "":
        limpiarPantalla()
        return

     if(len(telefono)==10 and telefono.isnumeric()==True):
        break
     else:
        print("Error, vuelva a intentar\n")

  while True:
     email = input("Ingrese su correo (ej. 'usuario@dominio.com'): ")
     
     if email == "":
        limpiarPantalla()
        return

     separ = email.split('@')
     sepun = email.split('.')
     if('@' in email and len(separ)==2 and '.' in email and len(sepun)==2):
        break
     else:
        print("Incorrecto, vuelva a intentarlo\n")

  email = email.lower()
  
  print("\n-- Seguridad")
  print("ENTER para SALIR\n")
  
  while True:
     password = input("Ingrese su contraseña (Max. 16 caracteres): ")
     
     if password == "":
        limpiarPantalla()
        return

     conpassword = input("Confirme de nuevo su contraseña: ")

     if conpassword == "":
        limpiarPantalla()
        return
     
     if (password == conpassword):
      if(len(password)<=16):
         break
      else:
         print("No valida, debe ser max. 16 caracteres\n")
     else:
        print("Contraseñas no coinciden, intente de nuevo\n")
        
  cur.callproc("CREARCUENTA", [userName, password, nombre, apellido,fechanacimiento,email,telefono,genero])
  limpiarPantalla()
  print(userName,"creado exitosamente!")

  return userName

def AccionarInvitado(opcion):
    
    if opcion == 0:
      print("Adios")
      exit()

    if opcion == 1:
        limpiarPantalla()
        usuario = IniciarSesion()

        if usuario == None:
           imprimirMenuPrincipalInvitado()

        imprimirMenuPrincipalUsuario(usuario)

    if opcion == 2:
       limpiarPantalla()
       usuario = CrearCuenta()

       if usuario == None:
          imprimirMenuPrincipalInvitado()

       imprimirMenuPrincipalUsuario(usuario)

    if opcion == 3:
      print("\n1. Buscar Publicaciones")
      print("2. Todas las publicaciones")
      print("0. SALIR")
      filt1 = validaropcion(0,2)

      if filt1 == 0:
          limpiarPantalla()
       
      if filt1 == 1:
          filtrarPublicaciones()
          input("\nPresione ENTER para REGRESAR -->")
          limpiarPantalla()
      
      if filt1 == 2:
         mostrarPublicaciones()
         input("\nPresione ENTER para REGRESAR -->")
         limpiarPantalla()

def AccionarUsuario(opcion,user):
    
    if opcion == 0:
       print("Adios")
       exit()
       
    if opcion == 1:
      limpiarPantalla()
      print("Sesion cerrada exitosamente")
      imprimirMenuPrincipalInvitado()

    if opcion == 9:
       print("\n1. Buscar Publicaciones")
       print("2. Todas las publicaciones (Escoger)")
       print("0. SALIR")
       filt = validaropcion(0,2)

       if filt == 0:
          limpiarPantalla()
          return
       
       if filt == 1:
          filtrarPublicaciones()
          input("\nPresione ENTER para REGRESAR -->")
          limpiarPantalla()
          return
          
       if filt == 2:
         mostrarPublicaciones()
         print("\nSeleccione la publicacion de su interés\nPara SALIR digite 0")
         pub = opcionnumerica()

         if(pub == "0"):
            limpiarPantalla()
            return
         else:
            cond = registrarVisualizacion(user,pub)
            if cond == False:
               return
            mostrarDetallesPublicacion(pub)

            print("\n1. GENERAR ORDEN")
            print("2. VER INFORMACION DEL VENDEDOR")
            print("3. REALIZAR UNA PREGUNTA")
            print("O. SALIR")
            option1 = validaropcion(0,3)

            if option1 == 0:
               limpiarPantalla()
               return
          
            if option1 == 1:
               generarOrden(pub,user)

            if option1 == 2:
               limpiarPantalla()
               cur.execute("SELECT IDVENDEDOR, NOMBRE FROM PUBLICACION JOIN VENDEDOR ON IDVENDEDOR = USERID JOIN USUARIO USING(USERID) WHERE NOPUBLICACION = "+str(pub)+"")
               resultado1 = cur.fetchone()
               print("\nMostrando reputacion de ",resultado1[1])
               mostrarReputacion(resultado1[0])
               input("\nPresione ENTER para REGRESAR -->")
               limpiarPantalla()

            if option1 == 3:
               realizarPregunta(pub,user)
             
          
    if opcion == 2:
       limpiarPantalla()
       print("--- MI CUENTA ---\n")
       mostrarPerfil(user)
       print("\n1. Actualizar Cuenta")
       print("2. Eliminar Cuenta")
       print("3. Direcciones Registradas")
       print("4. Cupones Registrados")
       print("5. Metodos de Pago Registrados")
       print("0. SALIR")
       opc4 = validaropcion(0,5)
       
       if opc4 == 0:
          limpiarPantalla()
          return
       
       if opc4 == 1:
         limpiarPantalla()
         conduser = actualizarUsuario(user)

         if (conduser != None):
            user = conduser
            imprimirMenuPrincipalUsuario(user)

       if opc4 == 2:
        limpiarPantalla()
        conduser2 = eliminarUsuario(user)        
        if(conduser2 == None):
           imprimirMenuPrincipalInvitado()

       if opc4 == 3:
         limpiarPantalla()
         mostrarDirecciones(user)
         print("\n1. Añadir direccion")
         print("2. Eliminar direccion")
         print("0. SALIR")
         opdir = validaropcion(0,2)

         if (opdir == 0):
            limpiarPantalla()
            return
       
         if (opdir == 1):
            limpiarPantalla()
            anadirDireccion(user)

         if (opdir == 2):
            eliminarDireccion(user)

       if opc4 == 4:
         limpiarPantalla()
         mostrarCupones(user)
         input("\nPresione ENTER para regresar -->")
         limpiarPantalla()

       if opc4 == 5:
          limpiarPantalla()
          mostrarMetodosPago(user)
          print("\n1. Añadir Tarjeta")
          print("2. Eliminar Tarjeta")
          print("0. SALIR")
          opdmet = validaropcion(0,2)

          if (opdmet == 0):
            limpiarPantalla()
            return
       
          if (opdmet == 1):
            limpiarPantalla()
            registrarTarjeta(user)

          if (opdmet == 2):
            eliminarTarjeta(user)
          
          
    if opcion == 7:
       limpiarPantalla()
       verReclamos(user)
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 5:
       limpiarPantalla()
       val = mostrarcompras(user)

       if val == False:
          return

       print("\n1. Calificar Compra")
       print("2. Hacer un reclamo")
       print("0. SALIR")
       opt = validaropcion(0,2)

       if opt == 0:
          limpiarPantalla()
          return
       
       if opt == 1 or opt == 2:
          print("\nSeleccione Compra, 0 para SALIR")
          while True:
             comp = opcionnumerica()

             if comp == "0":
                limpiarPantalla()
                return

             cur.execute("SELECT * FROM ORDEN WHERE ORDERID = "+comp+" AND IDCLIENTE = '"+user+"'")
             if(cur.fetchone() == None):
               print("\nNo corresponde, intenta de nuevo")
             else:
                break
             
       if opt == 1:
          calificarCompra(comp,user)
       
       if opt == 2:
          realizarReclamo(comp,user)
             
    if opcion == 8:
       print('1. Facturas Recibidas')
       print('2. Facturas Emitidas')
       print('3. Emitir Factura')
       print('0. SALIR')

       optc = validaropcion(0,3)

       if optc == 0:
          limpiarPantalla()
          return

       if optc == 1:
          mostrarFacturas(user)
          input("\nPresione ENTER para regresar -->")
          limpiarPantalla()

       if optc == 2:
          mostrarFacturasEmitidas(user)
          input("\nPresione ENTER para regresar -->")
          limpiarPantalla()

       if optc == 3:
          EmitirFactura(user)

    if opcion == 4:
       limpiarPantalla()
       crearpublicacion(user)

    if opcion == 6:
       limpiarPantalla()
       print("--- VENTAS ---\n")
       print("1. Ver Ventas")
       print("2. Preguntas")
       print("3. Reputacion")
       print("4. Publicaciones")
       print("0. SALIR")
       opven = validaropcion(0,4)

       if opven == 0:
          limpiarPantalla()
          return
       
       if opven == 1:
         limpiarPantalla()
         verventas(user)
         input("\nPresione ENTER para regresar -->")
         limpiarPantalla()
         
       if opven == 2:
          limpiarPantalla()
          responderpregunta(user)
          limpiarPantalla()

       if opven == 3:
         limpiarPantalla()
         mostrarReputacion(user)
         input("\nPresione ENTER para regresar -->")
         limpiarPantalla()

       if opven == 4:
         limpiarPantalla()
         gestionarPublicaciones(user)
               

    if opcion == 3:
       limpiarPantalla()
       mostrarPublicacionesDeInteres(user)
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 10:
      limpiarPantalla()
      verRespuestas(user)
      input("\nPresione ENTER para regresar -->")
      limpiarPantalla()


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
        print('0. SALIR')
        op = validaropcion(0,3)
        AccionarInvitado(op)
    
def imprimirMenuPrincipalUsuario(nomuser):
    op = ""
    while op !=0:
       cur.execute("SELECT NOMBRE FROM USUARIO WHERE USERID = '"+nomuser+"'")
       mostrarcaratula()
       print("Hola!",cur.fetchone()[0])
       print('1. Cerrar Sesion')
       print('2. Cuenta')
       print("3. Historial")
       print("4. Vender")
       print('5. Compras')
       print("6. Ventas")
       print('7. Reclamos') 
       print("8. Facturacion")
       print("9. Publicaciones")
       print("10. Respuestas")
       print('0. SALIR')
       op = validaropcion(0,10)

       AccionarUsuario(op,nomuser)

def mostrarPublicaciones():
   print("\n-- PUBLICACIONES --\n")
   
   query = "SELECT NOPUBLICACION AS PUB, NOMBREPUBLICACION AS NOMBRE, IDVENDEDOR AS VENDEDOR, PRECIOVENTA AS PRECIO, FECHAPUBLICACION AS PUBLICADO, STOCK from PUBLICACION ORDER BY FECHAPUBLICACION DESC"
   data = pd.read_sql(query, mercadolibreconnection)
   print(data.to_string(index=False, show_dimensions=False))
   
def mostrarPublicaciones2024():    
 query = "SELECT NOPUBLICACION AS PUB, NOMBREPUBLICACION AS NOMBRE, IDVENDEDOR AS VENDEDOR, PRECIOVENTA AS PRECIO, FECHAPUBLICACION AS PUBLICADO from PUBLICACION WHERE YEAR(FECHAPUBLICACION) = 2024 ORDER BY FECHAPUBLICACION DESC"
 data = pd.read_sql(query, mercadolibreconnection)
 print(data.to_string(index=False, show_dimensions=False))
    
def mostrarCupones(user):
  query = "SELECT ID AS COD, NOMBRE, DESCUENTO, FECHAVENCIMIENTO AS VENCE,CLIENTEID AS CLIENTE, VECES AS DISPONIBLE FROM CUPON WHERE CLIENTEID ='"+user+"'"
  data = pd.read_sql(query, mercadolibreconnection)

  if data.empty:
     print("No tiene cupones disponibles")
     return
  else:
     print("\nSus cupones\n")
     print(data.to_string(index=False, show_dimensions=False))

def mostrarPerfil(user):
   print("--Mi Perfil--")

   cur.execute ("SELECT USERID, EMAIL, NOMBRE, APELLIDO, TELEFONO, GENERO FROM USUARIO WHERE USERID = '"+user+"'")
   detalleperfil = cur.fetchone()

   print("\n--Datos de cuenta")
   print("Usuario:",detalleperfil[0])
   print("Email:",detalleperfil[1])

   print("\n--Datos personales")
   print("Nombre y Apellido:",detalleperfil[2],detalleperfil[3])
   print("Telefono:",detalleperfil[4])
   print("Autoidentificacion de genero:",detalleperfil[5])

def mostrarDirecciones(user):
   cur.execute("SELECT ID, PARROQUIA, REFERENCIAS, NOMBRECIUDAD, NOMBREPROVINCIA, NOMBREPAIS"+
               " FROM DIRECCION JOIN CIUDAD ON IDCIUDAD=CITYID NATURAL JOIN PROVINCIA NATURAL JOIN PAIS"+
               " WHERE USERID = '"+user+"'")
   
   print("\nSus direcciones registradas\n")
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
    
    limpiarPantalla()
    
    print("-- GENERAR ORDEN --")

    while True:
        print("Ingrese la cantidad deseada, 0 para cancelar")
        cantidad = int(opcionnumerica())

        if cantidad == 0:
           limpiarPantalla()
           print("Orden Cancelada")
           return
           
        if cantidad <= detallespublicacion[1]:
            break
        else:
            print("Sin stock\n")

    print("\nComo desea la entrega?\n"+
          "1.Entrega a domicilio (Entrega en 5 dias)\n"+
          "2.Entrega a acordar con el vendedor\n"+
          "0.Cancelar")
    
    op = validaropcion(0,2)

    if op == 0:
      limpiarPantalla()
      print("Orden Cancelada")
      return

    direccionid=None
    fechaentrega = None
    costoenvio = 0

    if op == 1:
       mostrarDirecciones(user)

       while True:
         print("Seleccione direccion, 0 para cancelar")
         opc = int(opcionnumerica())

         if opc == 0:
            limpiarPantalla()
            print("Orden Cancelada")
            return

         cur.execute("SELECT ID FROM DIRECCION WHERE USERID = '"+user+"'")
         resultado = cur.fetchall()

         if(opc > len(resultado)):
            print("Error. Seleccione la opcion correcta\n")
         else:
            direccionid = resultado[opc-1][0]
            costoenvio = 2
            fechaentrega = date.today() + timedelta(days=5)
            break

    subtotal = detallespublicacion[2] * cantidad
    total = subtotal + costoenvio
    total = round(total,2)
    print("\nUsted desea adquirir:",detallespublicacion[0])
    print("Cantidad:",cantidad)
    print("Subtotal:",subtotal)
    print("Costo envio:",costoenvio)
    print("Total:",total)
    print("Fecha de Entrega estimada:",fechaentrega)

    print("\nDesea ingresar cupon? 1. SI 2. NO 0. CANCELAR")
    op2 = validaropcion(0,2)
    idCupon = None
    descuento = 0

    if op2 == 0:
      limpiarPantalla()
      print("Orden Cancelada")
      return

    if op2==1:
       mostrarCupones(user)
       while True:
         print("\nEscribe el numero del cupón, 0 para cancelar")
         opc2 = opcionnumerica()

         if(int(opc2) == 0):
            limpiarPantalla()
            print("Orden Cancelada")
            return

         cur.execute("SELECT ID, NOMBRE, DESCUENTO, FECHAVENCIMIENTO,CLIENTEID, VECES FROM CUPON WHERE CLIENTEID ='"+user+"' AND ID = "+opc2+"")
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
               total = round(total,2)
               print("Cupon ingresado correctamente")
               print("\nUsted desea adquirir:",detallespublicacion[0])
               print("Cantidad:",cantidad)
               print("Subtotal:",subtotal)
               print("Costo envio (+):",costoenvio)
               print("Descuento "+str(int(detallescupon[2]))+"% (-):",descuento)
               print("Total:",total)
               print("Fecha de Entrega estimada:",fechaentrega)
               break

    print("\nDesea proceder con la compra? 1.SI 2.NO")
    op3 = validaropcion(1,2)

    if op3 == 2:
      limpiarPantalla()
      print("Orden Cancelada")
      return
    
    tarjeta = None

    if op3 == 1:
      print("\n-- PAGO")
      print("Escoja un método de pago")
      print("1. Tarjeta de Credito")
      print("2. Transferencia Bancaria")
      print("0. SALIR")
      opti = validaropcion(0,2)

      detallespago = None

      if opti == 0:
         limpiarPantalla()
         print("Orden Cancelada")
         return
      
      if opti == 1:
         cur.execute("SELECT * FROM TARJETA WHERE USERID = '"+user+"'")
         tarjetas = cur.fetchall()

         if (len(tarjetas) == 0):
            print("\nNo tiene ninguna tarjeta asociada a su cuenta!")
            print("Desea asociar una tarjeta?")
            print("1. SI\n0. CANCELAR")
            asop = validaropcion(0,1)

            if asop == 0:
               limpiarPantalla()
               print("Orden Cancelada")
               return
            
            if asop == 1:
               print("")
               tarjeta = registrarTarjeta(user)
               if tarjeta == None:
                  limpiarPantalla()
                  print("Orden Cancelada")
                  return
         else:
            contador = 0
            for card in range(len(tarjetas)):
               contador += 1
               print("\nMetodo de Pago # ",contador)
               print("Tarjeta No.",tarjetas[card][1])
               print(tarjetas[card][2])
               anio1,mes1,dia1 = str(tarjetas[card][4]).split("-") 
               print("Vence:",anio1+"/"+mes1)
               print("--------------------------------")

            print("Escoja un metodo de pago\n0 para SALIR")
            metodo = validaropcion(0,contador)

            if metodo == 0:
               limpiarPantalla()
               print("Orden Cancelada")
               return
            
            metodo = metodo -1
            
            fechavencestr = tarjetas[metodo][4].strftime("%Y-%m-%d")

            anio, mes, dia = fechavencestr.split("-")

            if verificar_tarjeta_vencida(int(anio), int(mes), int(dia)) == False:
               tarjeta = tarjetas[metodo][1]
            else:
               limpiarPantalla()
               print("Su tarjeta esta vencida, cancelando compra...")
               print("Orden Cancelada")
               return

         print("Validando Transaccion...")
            
      if opti == 2:
         print("Asocie un numero de transaccion para generar la orden, 0 para CANCELAR")
         trans = opcionnumerica()

         if(int(trans) == 0):
            limpiarPantalla()
            print("Orden Cancelada")
            return

         cur.execute("SELECT TRANSID, METODO, MONTO, CUOTA, CARDNUMBER FROM PAGO WHERE TRANSID = "+trans+" AND ROUND(MONTO,2) = "+str(total)+" AND IDCLIENTE = '"+user+"'")
         detallespago = cur.fetchone()

         print("Validando Transaccion...")

         registropagos = []
         cur.execute("SELECT IDPAGO FROM ORDEN")
         for IDPAGO in cur.fetchall():
            registropagos.append(IDPAGO[0])
         
         if (detallespago == None or (int(trans) in registropagos)):
            limpiarPantalla()
            print("TRANSACCION RECHAZADA")
            print("Lo sentimos, no tiene ningún pago asociado por el momento o fue usado en otra orden, intente de nuevo\n")
            return
         
    
    limpiarPantalla()

    if tarjeta == None:
      metod = 'Depósito'
      transid = detallespago[0]
      importe = detallespago[2]
      cuota = detallespago[3]
      creditcard = None

    else:
      metod = 'Crédito'
      importe = total
      cuota = 1
      creditcard = tarjeta
      cur.execute("INSERT INTO PAGO (METODO, MONTO, CUOTA, CARDNUMBER, IDCLIENTE) VALUES ('"+metod+"',"+str(importe)+","+str(cuota)+",'"+creditcard+"','"+user+"')") #espero SP Xavier
      cur.execute("SELECT LAST_INSERT_ID()")
      transid = cur.fetchone()[0]
      mercadolibreconnection.commit()


    print("\n--- Transaccion valida")
    print("\nDetalles de la transaccion:")
    print("No.Transaccion:",transid)
    print("Metodo:",metod)
    print("Monto:",importe)
    print("Cuota:",cuota)
    print("Tarjeta No.",creditcard)


    print("\nGenerando orden...")
            
    args = (idCupon, detallespublicacion[3], transid, cantidad, nopublicacion, user, detallespublicacion[4], importe, direccionid, costoenvio, fechaentrega)

    cur.callproc("REALIZARCOMPRA", args)
    cur.execute("SELECT LAST_INSERT_ID()")
    numorden = cur.fetchone()[0]
    print("Orden",numorden,"realizada con éxito!")
    print("Gracias por comprar en Mercado Libre :)")

def anadirDireccion(user):
   print("--- NUEVA DIRECCION ---\n")
   print("-- Seleccion de pais")
   print("0 para SALIR\n")
   cur.execute("SELECT * FROM PAIS")
   listapaises = cur.fetchall()
   contador = 0
   for pais in listapaises:
      contador +=1
      print(str(contador)+"."+pais[1])

   seleccionpais = validaropcion(0,contador)
   
   if seleccionpais == 0:
      limpiarPantalla()
      return
   
   idpais = listapaises[seleccionpais-1][0]

   print("\n-- Seleccion de estado")
   print("0 para SALIR\n")

   cur.execute("SELECT PROVID, NOMBREPROVINCIA FROM PAIS JOIN PROVINCIA USING (COUNTRYID) WHERE COUNTRYID ="+str(idpais)+"")

   listaestados = cur.fetchall()
   contador2 = 0

   for estado in listaestados:
      contador2 += 1
      print(str(contador2)+"."+estado[1])

   seleccionestado = validaropcion(0,contador2)

   if seleccionestado == 0:
      limpiarPantalla()
      return
   
   idestado = listaestados[seleccionestado-1][0]

   print("\n-- Seleccion de ciudad")
   print("0 para SALIR\n")

   cur.execute("SELECT CITYID, NOMBRECIUDAD FROM PROVINCIA JOIN CIUDAD USING (PROVID) WHERE PROVID ="+str(idestado)+"")

   listaciudades = cur.fetchall()
   contador3 = 0

   for ciudad in listaciudades:
      contador3 +=1
      print(str(contador3)+"."+ciudad[1])

   seleccionciudad = validaropcion(0,contador3)

   if seleccionciudad == 0:
      limpiarPantalla()
      return
   
   idciudad = listaciudades[seleccionciudad-1][0]

   print("\n-- Detalles de Direccion\n0 para SALIR\n")
   while True:
      parroquia = input("Ingrese parroquia: ")

      if parroquia == "0":
         limpiarPantalla()
         return

      if(parroquia.isalpha()):
         break
      else:
         print("Ingrese solo caracteres\n")

   
   referencias = input("Especifique una referencia: ")

   if referencias == "0":
      limpiarPantalla()
      return

   limpiarPantalla()
   print("Añadiendo dirección...")

   args = (parroquia, referencias, idciudad, user)
   cur.callproc("NUEVADIRECCION",args)

   print("Direccion añadida correctamente!")

def eliminarDireccion(user):
   print ("\n--- ELIMINAR DIRECCION ---\n")

   while True:
         print("Seleccione la direccion a eliminar, 0 para cancelar")
         opc = int(opcionnumerica())

         if opc == 0:
            limpiarPantalla()
            return

         cur.execute("SELECT ID FROM DIRECCION WHERE USERID = '"+user+"'")
         resultado = cur.fetchall()

         if(opc > len(resultado)):
            print("Error. Seleccione la opcion correcta\n")
         else:
            direccionid = resultado[opc-1][0]
            break

   print("\nRecuerde que si borra su direccion, también se borrará en las ordenes que haya realizado")
   print("¿Seguro que desea eliminar la direccion #",opc,"?")
   print("1. SI"+
         "\n0. CANCELAR")
   
   opconf = validaropcion(0,1)

   if opconf == 0:
      limpiarPantalla()
      return
   
   limpiarPantalla()
   print("Eliminando direccion...")

   cur.execute("CALL ELIMINARDIRECCION("+str(direccionid)+")")

   print("Direccion eliminada exitosamente")

def mostrarcompras(user):
   print("--- MIS COMPRAS ---\n")
   query = "SELECT ORDERID AS ORDEN, FECHACREACION AS CREADO, ORD.ESTADO, CANTIDADPRODUCTO AS CANTIDAD, COSTOENVIO AS ENVIO, IMPORTE, NOMBRE AS PRODUCTO, NOMBREPUBLICACION AS PUBLICACION, METODO, CARDNUMBER FROM PAGO JOIN ORDEN ORD ON TRANSID = IDPAGO  JOIN PRODUCTO USING(PRODUCTID) LEFT JOIN PUBLICACION USING (PRODUCTID) WHERE ORD.IDCLIENTE = '"+user+"'"
   data = pd.read_sql(query, mercadolibreconnection)

   if data.empty:
      print("Hasta el momento, no ha realizado compras!")
      return False
   else:
     print(data.to_string(index=False, show_dimensions=False))
     return True

def calificarCompra(comp,user):
   print("\n--- CALIFICAR COMPRA #"+comp+" ---\n")
   cur.execute("SELECT ORDERID, ESTADO, ESTRELLASPRODUCTO, ESTRELLASVENDEDOR, COMENTARIO, IDVENDEDOR FROM ORDEN WHERE ORDERID = "+comp+" AND IDCLIENTE = '"+user+"'")
   detallesorden = cur.fetchone()

   if (detallesorden[1] == 'Completada'):
      if(detallesorden[2] == None and detallesorden[3] == None and detallesorden[4] == None):
         print("Estimado usuario, la encuesta esta disponible para su calificacion")
      else:
         limpiarPantalla()
         print("Estimado "+user+", Su compra ya fue calificada!")
         return
   else:
      limpiarPantalla()
      print("Estimado usuario, solo puede calificar ordenes completadas")
      return
   
   print("\n-- Estado del producto")
   print("Del 0 al 5 califique el estado del producto")
   estrellasproducto = validaropcion(0,6)

   if(estrellasproducto == 6):
      limpiarPantalla()
      return
   
   estrellasvendedor = None
   if detallesorden[5] != None:
      print("\n-- Calificacion del Vendedor")
      print("¿Que tal le parecio la atencion del vendedor "+detallesorden[5]+"?")
      print("Califique del 0 al 5")
      estrellasvendedor = validaropcion(0,6)

      if(estrellasvendedor == 6):
         limpiarPantalla()
         return
   
   while True:
      comentario = input("Escriba un comentario (Max.100), caso contrario ENTER, para salir escriba EXIT: ")
      if(len(comentario)<=100):
         break
      else:
         print("Ha excedido los 100 caracteres, intente de nuevo\n")

   if comentario.lower() == 'exit':
      limpiarPantalla()
      return
   
   if comentario == "":
      comentario = None
      
   args = (estrellasproducto, estrellasvendedor, comentario, comp)
   cur.callproc("CALIFICARCOMPRA", args)

   limpiarPantalla()
   print("\nOrden calificada!")

def mostrarProductos():
   print("\n--- PRODUCTOS ---\n")
   query = "SELECT PRODUCTID AS ID, NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA FROM PRODUCTO"
   data = pd.read_sql(query, mercadolibreconnection)
   print(data.to_string(index=False, show_dimensions=False))

def crearpublicacion(user):
   print("\n--- VENDER ---\n")
   lusuarios = []
   cur.execute("SELECT USERID FROM USUARIO")
   for USERID in cur.fetchall():
    lusuarios.append(USERID[0])

   print("\n-- ¡Hola! Antes que nada cuéntanos, ¿Cómo quieres que se muestre tu publicación?")
   print("\n1.Gratuita \n2.Clásica \n3.Premium")
   print("ENTER para salir\n")
   while True:
      tipoExposicion = input("Ingrese el número de la opción de tu preferencia: ")
      if tipoExposicion == "":
         limpiarPantalla()
         return
    
      if(tipoExposicion == "1"):
         tipoExposicion == "Gratuita"
         break
      elif(tipoExposicion == "2"):
         tipoExposicion == "Clásica"
         break
      elif(tipoExposicion == "3"):
         tipoExposicion == "Premium"
         break
      else:
         print("Ingrese una opción válida")
         

   print("\n-- Busquemos tu producto en nuestro catálogo, si tu producto a vender no esta en lista, ingresa 0 para agregarlo")


   while True:
      lproductos = []

      cur.execute("SELECT PRODUCTID FROM PRODUCTO")
      for PRODUCTOID in cur.fetchall():
         lproductos.append(PRODUCTOID[0])


      mostrarProductos()
      idProducto = input("\nIngrese el ID del producto o ingrese 0 para agregar uno nuevo, ENTER para SALIR: ")
      
      if(idProducto == ""):
         limpiarPantalla()
         print("Operacion cancelada!")
         return
      
      
      if(idProducto!= "0"):
         if(int(idProducto) in lproductos):
            break
         else:
            print("\nIngrese una ID existente")
      else:
         print("\nRegistrando Producto")
         

         nProducto = input("Ingrese el nombre del producto: ")
         if nProducto == "":
            limpiarPantalla()
            print("Operacion cancelada!")
            return
         
         mProducto = input("Ingrese la marca del producto: ")
         if mProducto == "":
            limpiarPantalla()
            print("Operacion cancelada!")
            return
         
         cProducto = input("Ingrese la categoria del producto: ")
         if cProducto == "":
            limpiarPantalla()
            print("Operacion cancelada!")
            return
         
         scProducto = input("Ingrese la subcategoria del producto: ")
         if scProducto == "":
            limpiarPantalla()
            print("Operacion cancelada!")
            return
         
         print("\nRegistrando Producto")
         args1 = nProducto, mProducto, cProducto, scProducto
         cur.callproc("registrarProducto", args1)  #Falto el SP para registrar producto
         
         print("\nProducto registrado existosamente")
      
   nombrePublicacion = input("Ingresa el nombre para tu publicación: ")
   descrpicion = input("Redacta la descripción que deseas que los clientes observen en tu publicación: ")
   precio = input("Ingresa el precio de venta al público: $")

   while True:
      stock = input("Ingresa la cantidad de stock que posees: ")
      if stock > "0":
         break
      else:
         print("\nEl stock no puede ser 0\n")
      
   limpiarPantalla()
   print("Creando Publicacion...")
   args = descrpicion,tipoExposicion,idProducto,user,precio,nombrePublicacion,stock
   cur.callproc("crearPublicacion", args)
   cur.execute("SELECT LAST_INSERT_ID()")
   pubid = cur.fetchone()[0]
   print("Venta#",pubid," publicada con exito")

def registrarVisualizacion(user,noPublicacion):
   cur.execute("SELECT NOPUBLICACION FROM PUBLICACION WHERE NOPUBLICACION = "+str(noPublicacion)+"")

   if cur.fetchone() == None:
      limpiarPantalla()
      print("\nPublicacion no encontrada")
      return False
   
   cur.execute("SELECT REGID, USERID, NOPUBLICACION, FECHA FROM VISUALIZACION_PUBLICACIONES WHERE NOPUBLICACION = "+str(noPublicacion)+" AND USERID = '"+user+"'")
   resultado = cur.fetchone()

   if(resultado == None):
      args = user,noPublicacion
      cur.callproc("registrarVisualizacion",args)

   else:
      cur.execute("UPDATE VISUALIZACION_PUBLICACIONES SET FECHA = now() WHERE NOPUBLICACION = "+noPublicacion+" AND USERID = '"+user+"'")
      mercadolibreconnection.commit()
   return True

def mostrarPublicacionesDeInteres(user):
   print("--- HISTORIAL ---\n") 
   query = "SELECT p.NOPUBLICACION AS PUB, p.NOMBREPUBLICACION AS NOMBRE, p.IDVENDEDOR AS VENDEDOR, p.PRECIOVENTA AS PRECIO, p.FECHAPUBLICACION AS PUBLICADO, FECHA AS VISTO from VISUALIZACION_PUBLICACIONES vp JOIN PUBLICACION p USING (NOPUBLICACION) WHERE USERID = '"+user+"' ORDER BY FECHA DESC"
   data = pd.read_sql(query, mercadolibreconnection)

   if data.empty:
      print("Historial vacio")
   else:
     print(data.to_string(index=False, show_dimensions=False))

def mostrarFacturas(user):
   limpiarPantalla()
   print("\n--- MIS FACTURAS ---\n")
   query = "SELECT FACTID AS FACTURA, FECHA AS EMITIDO, DESCRIPCION, FACT.IDVENDEDOR AS VENDEDOR, FACT.IDCLIENTE AS CLIENTE, FACT.IDORDEN AS ORDEN, NOMBRE AS PRODUCTO FROM FACTURA FACT JOIN ORDEN USING (IDCLIENTE) JOIN PRODUCTO USING (PRODUCTID) WHERE FACT.IDCLIENTE = '"+user+"'"
   data = pd.read_sql(query, mercadolibreconnection)

   if data.empty:
      print("No hay Facturas")
   else:
     print(data.to_string(index=False, show_dimensions=False))
   
def mostrarFacturasEmitidas(user):
   limpiarPantalla()
   print("--- FACTURAS EMITIDAS ---\n")

   query = "SELECT FACTID AS FACTURA, FECHA AS EMITIDO, DESCRIPCION, FACT.IDCLIENTE AS CLIENTE, FACT.IDORDEN AS ORDEN, NOMBRE AS PRODUCTO FROM PRODUCTO PROD JOIN ORDEN ORD USING(PRODUCTID) JOIN FACTURA FACT ON IDORDEN = ORDERID JOIN VENDEDOR V ON FACT.IDVENDEDOR = USERID WHERE FACT.IDVENDEDOR ='"+user+"'"
   data = pd.read_sql(query, mercadolibreconnection)
   
   if data.empty:
      print("No dispone de facturas emitidas actualmente!")
   else:
     print(data.to_string(index=False, show_dimensions=False))
   
def EmitirFactura(user):
   limpiarPantalla()
   print("\n--- EMISION DE FACTURA ---\n")
   query = "SELECT ORDERID AS ORDEN, FACT.IDORDEN, ORDEN.IDCLIENTE AS CLIENTE, ORDEN.IDVENDEDOR, ESTADO, NOMBRE AS PRODUCTO FROM FACTURA FACT RIGHT JOIN  ORDEN ON IDORDEN = ORDERID NATURAL JOIN PRODUCTO WHERE FACT.IDORDEN IS NULL AND ORDEN.IDVENDEDOR = '"+user+"' AND ESTADO = 'Completada'"
   data = pd.read_sql(query, mercadolibreconnection)
   columnasmostrar = ['ORDEN', 'PRODUCTO','CLIENTE','ESTADO']
   data2 = data[columnasmostrar]

   if data.empty:
      print("Estimado usuario, no tiene ordenes que facturar!")
      return
   else:
     print("Estimado usuario, les presentamos las siguientes ordenes a facturar\n")
     print(data2.to_string(index=False, show_dimensions=False))

   cur.execute(query)
   ordenespendientesfacturar = cur.fetchall()

   cond = False
   indice = None

   while cond == False:
      print("\nSeleccione la orden a facturar, 0 para SALIR")
      ordenafacturar = opcionnumerica()

      if ordenafacturar == "0":
         limpiarPantalla()
         return
      
      for orden in ordenespendientesfacturar:
         if(int(ordenafacturar) == orden[0]):
            indice = ordenespendientesfacturar.index(orden)
            cond = True
            break
      
      if cond == False:
         print("Opcion incorrecta, vuelva a intentar")

   descripcion = None

   print("\nAñada una descripcion (Max.100), EXIT para SALIR, ENTER para saltar")

   while True:
      descripcion = input("Ingrese: ")
      if (descripcion.lower() == 'exit'):
         limpiarPantalla()
         return
      if(len(descripcion)<=100):
         break
      else:
         print("La descripcion no debe exceder de los 100 caracteres\n")

   if(descripcion == ""):
      descripcion = 'NULL'
   else:
      descripcion = "'"+descripcion+"'"

   

   print("\nSeguro que desea emitir la factura? No se puede revertir esta accion")
   print("1. SI\n0. SALIR")
   opf = validaropcion(0,1)

   if opf == 0:
      limpiarPantalla()
      print("Facturacion cancelada!")
      return
   
   fecha_actual = date.today()
   fecha_actual_str = fecha_actual.strftime('%Y-%m-%d')

   limpiarPantalla()
   print("Generando Factura...")
   args = descripcion, ordenespendientesfacturar[indice][3], ordenespendientesfacturar[indice][2], ordenespendientesfacturar[indice][0]
   cur.callproc("EMITIRFACTURA", args)
   cur.execute("SELECT LAST_INSERT_ID()")
   factid = cur.fetchone()[0]
   print("FACT#",factid,"generada con exito")
 
def realizarReclamo(comp,user):
   print("\n--- EMITIR RECLAMO COMPRA #",comp,"---")
   print("ENTER para SALIR\n")

   cur.execute("SELECT R.ID, R.TIPO, R.ESTADO, R.VENDEDORID, NOMBRE FROM RECLAMO R JOIN ORDEN USING(ORDERID) JOIN PRODUCTO USING(PRODUCTID) WHERE ORDERID = "+comp+" AND CLIENTEID = '"+user+"'")
   resultado = cur.fetchone()

   if resultado != None:
      limpiarPantalla()
      print("Estimado usuario, usted ya realizo un reclamo anteriormente\n")
      print("Reclamo #",resultado[0])
      print("Tipo:",resultado[1])
      print("Estado:",resultado[2])
      print("Vendedor:",resultado[3])
      print("Producto:",resultado[4])
      return

   while True:
      tipo = input("Especifique TIPO: ")

      if tipo == "":
         limpiarPantalla()
         print("Reclamo cancelado!")
         return
      
      if tipo.isalpha() == True:
         break
      else:
         print("\nError, intente de nuevo")

   print("\nSeguro que desea enviar el reclamo?")
   print("1. SI\n0. SALIR")
   opt = validaropcion(0,1)

   if opt == 0:
      limpiarPantalla()
      print("Reclamo Cancelado!")
      return
   
   limpiarPantalla()
   print("Generando reclamo...")
   cur.execute("SELECT IDVENDEDOR FROM ORDEN WHERE ORDERID = "+comp+" AND IDCLIENTE = '"+user+"'")
   idvendedor = cur.fetchone()[0]

   args = (tipo, user, idvendedor, comp)

   cur.callproc("NUEVORECLAMO", args)
   cur.execute("SELECT LAST_INSERT_ID()")
   reclamoid = cur.fetchone()[0]
   print("Reclamo #"+str(reclamoid)+" generado con exito!")

def validarUsuario(usuario):
    cur.execute("SELECT USERID FROM USUARIO")
    usuarios = []
    for user in cur.fetchall():
        usuarios.append(user[0])
    if usuario in usuarios:
        return True
    else:
        return False
        
def actualizarUsuario(user):
    print("\n--- MODIFICAR CUENTA ---")
    print("Enter para SALIR\n")

    dato = input("Ingrese el dato que desea actualizar\nUserID, Email, Pass, Nombre, Apellido, Telefono, Genero:\n").lower()
    if dato == "":
       limpiarPantalla()
       return
    newvalue = input("Ingrese el/la nuevo/a "+ dato + ":\n")

    if newvalue == "":
       limpiarPantalla()
       return

    if dato == "userid":
        while validarUsuario(newvalue):
            print("Este usuario ya se encuentra registrado")
            newvalue = input("Ingrese el nuevo usuario:\n")

            if newvalue == "":
               limpiarPantalla()
               return
            
    if dato == "genero":
       while newvalue.upper() not in ['MASCULINO', 'FEMENINO', 'LGBTI']:
          print("Error, las opciones son ['Masculino','Femenino','LGBTI']")
          newvalue = input("Ingrese genero: ")

          if newvalue == "":
             limpiarPantalla()
             return
          
          
    try:
        cur.execute("UPDATE USUARIO SET " + dato.upper()+ "= %s WHERE USERID = %s",(newvalue,user))
        mercadolibreconnection.commit()

        limpiarPantalla()
        print("¡Su " + dato +" ha sido cambiado con éxito!")

        if dato == "userid":
           return newvalue
        else:
           return None

    except Exception as e:
        print(f"Error: {e}")
    cur.close()

def eliminarUsuario(user):
    print("--- ELIMINAR CUENTA "+user+" ---")
    print("Te echaremos de menos :(\n")
    
    validacion = input("¿Está seguro que quiere eliminar su cuenta?\n¡Esta acción no se puede revertir!\nEscriba 'si' para confirmar\nENTER para SALIR\n")
    if validacion.lower() == "si":
        try:
            print("Eliminando usuario...")
            mercadolibreconnection.begin()
            cur.execute("DELETE FROM USUARIO WHERE USERID = '"+ user +"';") 
            mercadolibreconnection.commit()
            

            limpiarPantalla()
            print("¡Usuario eliminado con éxito!")
            print("Vuelve pronto :), estamos para servirte!")
            return None

        except Exception as e:
            print(f"Error: {e}")
            mercadolibreconnection.rollback()
    else:
        limpiarPantalla()
        print("Acción cancelada")
        return user

def imprimirOrden(registros):
    try:
        if len(registros) > 0:
            print(" -- ORDENES CON ESTADO '" + registros[0][1].upper()+"': --")
            for registro in registros:
                nombre,estado,cupon,suma = registro
                print("PRODUCTO: "+nombre)
                print("Cantidad: "+ str(suma))
                print("Estado: "+estado)
                if(cupon != None):
                    print("Cupon: "+str(cupon))
                else:
                    print("No se usaron cupones")
                print("")
    except Exception as e:
        print(f"Error: {e}")

def verventas(user):
    cur.execute("select  idvendedor from orden o natural join producto p where idvendedor = '"+user+"';")
    if(len(cur.fetchall())) > 0:
        print("--- REPORTE DE ORDENES ---")
        cur.execute("select  p.nombre,o.estado,idcupon, sum(cantidadproducto) sumaproductos from orden o natural join producto p where idvendedor = '"+user+"' and estado = 'Completada' group by o.idvendedor, p.nombre,o.estado,idcupon;")
        imprimirOrden(cur.fetchall())
        cur.execute("select  p.nombre,o.estado,idcupon, sum(cantidadproducto) sumaproductos from orden o natural join producto p where idvendedor = '"+user+"' and estado = 'Pendiente' group by o.idvendedor, p.nombre,o.estado,idcupon;")
        imprimirOrden(cur.fetchall())
        cur.execute("select  p.nombre,o.estado,idcupon, sum(cantidadproducto) sumaproductos from orden o natural join producto p where idvendedor = '"+user+"' and estado = 'En curso' group by o.idvendedor, p.nombre,o.estado,idcupon;")
        imprimirOrden(cur.fetchall())
    else:
        limpiarPantalla()
        print("Por ahora usted no tiene ordenes realizadas")

def realizarPregunta(pub,user):
   print("\n--- REALIZAR PREGUNTA ---")
   print("Presione ENTER para SALIR\n")

   while True:
      mensaje = input("Ingrese el contenido del mensaje que desea enviarle al vendedor: ")

      if mensaje == "":
         limpiarPantalla()
         return
      
      if (len(mensaje) > 50):
         print("Estimado usuario, solo es permitido hasta 50 caracteres\n")

      else:
         break

   cur.execute("SELECT IDVENDEDOR FROM PUBLICACION WHERE NOPUBLICACION = "+pub+"")
   vendedor = cur.fetchone()[0]
   cur.execute("INSERT INTO PREGUNTA (CONTENIDO, IDCLIENTE, IDVENDEDOR, NOPUBLICACION) VALUES (%s, %s, %s, %s)", (mensaje, user, vendedor, pub))
   mercadolibreconnection.commit()
   
   limpiarPantalla()
   print("La pregunta ha sido enviada correctamente.")
   print("Muchas gracias por su tiempo, esperamos que sus dudas sean resueltas lo mas pronto posible.\nAdios.")

def responderpregunta(userid):
    cur.execute("SELECT IDPREGUNTA,CONTENIDO,MENSAJERESPUESTA,IDCLIENTE FROM PREGUNTA WHERE IDVENDEDOR = '"+ userid +"';")
    preguntas = cur.fetchall()
    for pregunta in preguntas:
        idpregunta,contenido,respuesta,cliente = pregunta
        print("")
        print("Id: " + str(idpregunta))
        print("Pregunta: " + contenido)
        print("By: " + cliente)
        if respuesta != None:
            print("Respuesta: " + respuesta)
        else:
            print("¡No hay respuesta!")
    print("") 
    responder = input("Desea responder algún comentario\nSI/NO\n").lower()
    
    while(responder == "si"):
        print("Ids disponibles : ", end= "")
        cur.execute("SELECT IDPREGUNTA FROM PREGUNTA WHERE IDVENDEDOR = '"+ userid +"';")
        lIdPreg = cur.fetchall()
        idDisponibles = []
        c = 0
        for ids in lIdPreg:
            c+=1
            print(ids[0],end="")
            idDisponibles.append(ids[0])
            if(c != len(lIdPreg)):
                print(" , ", end= "")
        preg = input("\nSeleccione el id de la pregunta que desea responder: \n")
        while(int(preg) not in idDisponibles):
            print("¡ID no encontrado!")
            preg = input("Seleccione el id de la pregunta que desea responder: \n")
        newrespuesta = input("Escriba su respuesta: \n")
        cur.execute("UPDATE PREGUNTA SET MENSAJERESPUESTA = '"+newrespuesta+"' where idpregunta = "+preg+";")
        cur.execute("UPDATE PREGUNTA SET FECHAHORARESPUESTA = NOW() where idpregunta = "+preg+";")
        responder = input("¿Desea responder otro comentario?\nSI/NO\n").lower()
        mercadolibreconnection.commit()

def verReclamos(userid):
    print("")
    cur.execute("select * from reclamo where clienteid = '"+userid+"'")
    reclamosGenerados = cur.fetchall()
    if(len(reclamosGenerados)>0):
        print("-- Reclamos que usted ha hecho: --")
    else:
        print("¡Usted no ha generado reclamos!")
    for reclamo in reclamosGenerados:
        print("ID DEL RECLAMO:",reclamo[0])
        print("Tipo:",reclamo[1])
        print("Estado:",reclamo[2]) 
        print("Cliente:", reclamo[3])
        print("Vendedor:", reclamo[4])
        print("")

    cur.execute("select * from reclamo where vendedorid = '"+userid+"'")
    reclamosPorResolver = cur.fetchall()
    if(len(reclamosPorResolver)>0):
        print("-- Reclamos por resolver: --")
    else:
        print("¡Usted no tiene reclamos!")
    for reclamo in reclamosPorResolver:
        print("ID DEL RECLAMO:",reclamo[0])
        print("Tipo:",reclamo[1])
        print("Estado:",reclamo[2]) 
        print("Cliente:", reclamo[3])
        print("Vendedor:", reclamo[4])
        print("")
    print("")

def mostrarReputacion(user):
   print ("--- REPUTACION ---")
   print("La reputacion se calcula en base al promedio de estrellas en todas las ordenes\n")

   cur.execute("SELECT * FROM VENDEDOR WHERE USERID = '"+user+"'")
   resultado = cur.fetchone()

   if(resultado == None):
      limpiarPantalla()
      print(user," no tiene reputacion disponible porque no es un vendedor")
      print("Empiece a vender!")
      return

   if resultado[1] == None:
      limpiarPantalla()
      print("Reputacion no disponible por el momento")
      return()
   else:
      print("-- Reputacion de ",resultado[0])
      print("Promedio: ",resultado[1])
      
def imprimirPublicaciones(userid,estado):
    cur.execute("select nopublicacion, nombrepublicacion, descripcion, precioventa, estado, stock from Publicacion where idvendedor = '"+userid+"' and estado = '"+estado+"';")
    publicaciones= cur.fetchall()
    palabra = ""
    if(estado.lower() == "activa"):
        palabra = "ACTIVAS"
    elif(estado.lower()=="agotado"):
        palabra = "AGOTADAS"
    elif(estado.lower()=="no activa"):
        palabra = "NO ACTIVAS"
    if(len(publicaciones)):
        print("-- PUBLICACIONES "+palabra+" --")
    else:
        print("No dispone de publicaciones",palabra)
        return
   
    for pub in publicaciones:
        id, producto,descripcion,precio,estado,stock = pub
        print("Id: " + str(id))
        print("Publicacion: " + producto)
        print("Descripcion: " + descripcion)
        print("Precio: $" + str(precio))
        print("Estado " + estado)
        print("Stock: " + str(stock))

    print("")

def editarPublicacion(idPublicacion):
    campoNumero = input("Seleccione el campo que desee modificar:\n1=NombrePublicacion -- 2=Descripcion -- 3=Precio -- 4=Estado -- 5=Stock \nPresione otra tecla para volver\n")
    while campoNumero in ["1","2","3","4","5"]:
        campo = ""
        if campoNumero == "1":
            campo = 'nombrepublicacion'
        elif campoNumero == "2":
            campo = 'descripcion'
        elif campoNumero == "3":
            campo = 'precioventa'
        elif campoNumero == "4":
            campo = 'estado'
        elif campoNumero == "5":
            campo = 'stock'
        valor = input("Escriba el nuevo valor\n")
        cur.execute("UPDATE PUBLICACION SET "+campo+" = '"+valor+"' where nopublicacion = " + str(idPublicacion))
        campoNumero = input("Seleccione el campo que desee modificar:\n1 = Producto -- 2 = Descripcion -- 3 = Precio -- 4 = Estado -- 5 = Stock \nPresione otra tecla para volver\n")
    mercadolibreconnection.commit()
    print("¡Datos actualizados correctamente!")

def eliminarPublicacion(idpublicacion):
    try:
        mercadolibreconnection.begin()
        cur.execute("delete from publicacion where nopublicacion = "+str(idpublicacion)+";")
        mercadolibreconnection.commit()
    except Exception as e:
        print(f"Error{e}")
        mercadolibreconnection.rollback()

def gestionarPublicaciones(userid):
    cur.execute("SELECT NOPUBLICACION FROM PUBLICACION WHERE IDVENDEDOR = '" + userid + "';")
    registros = cur.fetchall()
    lids = []
    for registro in registros:
        lids.append(str(registro[0]))
    totalpublicaciones = len(registros)

    if totalpublicaciones > 0: 
        print("")
        imprimirPublicaciones(userid,"Activa")
        imprimirPublicaciones(userid,"Agotado")
        imprimirPublicaciones(userid,"No Activa")
        editar = input("\n¿Desea editar/eliminar alguna publicacion?\nEditar/Eliminar/VOLVER\n").lower()
        while(editar in ["editar","eliminar"]):
            if editar == "editar":
                idpub = input("Seleccione el id de la publicacion\n")
                while idpub not in lids:
                    idpub = input("¡Id invalido! Intente nuevamente:\n")
                editarPublicacion(idpub)
            elif editar == "eliminar":
                while True:
                  idpub = input("Seleccione el id de la publicacion a eliminar\n")
                  if(idpub not in lids):
                     print("Id Invalido! Intente nuevamente\n")
                  else:
                     break
                conf = input("¿Seguro que quiere eliminar la publicación? (Esta acción no se puede revertir)\nSI/NO\n").lower()
                if conf == "si":
                    eliminarPublicacion(idpub)
                    print("¡Publicación eliminada con éxito!")
            else:
                print("Acción finalizada")
            editar = input("¿Desea editar/eliminar otra publicacion?\nEditar/Eliminar/Volver\n").lower()  
        print("¡Cambios realizados correctamente!")
    else:
        print("Usted no tiene productos publicados")

def registrarTarjeta(user):
   print ("\n--- REGISTRAR METODO PAGO ---")
   print("American Express (3)") #primera cifra
   print("Visa (4)")
   print("MasterCard (5)")
   print("17 cifras")
   print("ENTER PARA SALIR")

   cur.execute("SELECT ID, NUMERO FROM TARJETA WHERE USERID = '"+user+"'")
   listatarjetas = []
   for ID, NUMERO in cur.fetchall():
      listatarjetas.append(NUMERO)
   
   while True:
      creditcard = input("Numero de Tarjeta XXXXXXXXXXXXXXXXX: ")
      if creditcard == "":
         limpiarPantalla()
         return None


      if len(creditcard) != 17 or creditcard.isnumeric() == False or creditcard[0] not in ['3','4','5']:
         print("\nError, intente de nuevo")

      else:
         creditcard = separarDigitos(creditcard)
         if creditcard in listatarjetas:
            print("\nEsta tarjeta ya ha sido asociada a su cuenta, agregue otra")
         else:
            break
   

   if creditcard[0] == '3':
      tipo = "AMERICAN EXPRESS"

   if creditcard[0] == '4':
      tipo = "VISA"

   if creditcard[0] == '5':
      tipo = "MASTERCARD"

   while True:
      print("CVV, O PARA SALIR")
      cvv = opcionnumerica()
      
      if cvv == "0":
         limpiarPantalla()
         return None

      if len(cvv) != 3:
         print("CVV debe ser de 3 cifras\n")
      else:
         break
   
   while True:
      fecha_actual = datetime.now()

      print("\nMes de Vencimiento")
      mes = opcionnumerica()
      print("\nAnio de Vencimiento: ")
      anio = opcionnumerica()
      dia = 1

      if 1 <= int(mes) <= 12 and anio.isnumeric() == True:
         if verificar_tarjeta_vencida(int(anio), int(mes), dia) == False:
            break
         else:
            limpiarPantalla()
            print("Esta tarjeta esta vencida, intente de nuevo")
            return None
      else:
         print("Ingrese el mes y anio correcto")
   
   limpiarPantalla()
   print("\nAgregando Tarjeta...")

   cur.execute("INSERT INTO TARJETA (NUMERO, MARCA, CVV, FECHAVENCIMIENTO, USERID) VALUES ('"+creditcard+"','"+tipo+"',"+cvv+",'"+anio+"-"+mes+"-"+str(dia)+"','"+user+"')")
   mercadolibreconnection.commit()

   print("Tarjeta Agregada con éxito!")
   return creditcard

def separarDigitos(tarjeta):
   numbercard = ""
   espacios = 0
   contador = 1

   for i in tarjeta:
      if espacios == 3:
         numbercard = numbercard+i

      elif contador !=4:
         numbercard = numbercard+i
         contador += 1
      else:
         numbercard = numbercard+i+" "
         espacios += 1
         contador = 1

   return numbercard

def mostrarMetodosPago(user):
   print("--- METODOS DE PAGO REGISTRADOS ---")
   cur.execute("SELECT * FROM TARJETA WHERE USERID = '"+user+"'")
   tarjetas = cur.fetchall()

   if len(tarjetas) == 0:
      print("\nNo tiene ninguna tarjeta asociada a su cuenta!")

   else:
      contador = 0
      for card in range(len(tarjetas)):
         contador += 1
         print("\nMetodo de Pago # ",contador)
         print("Tarjeta No.",tarjetas[card][1])
         print(tarjetas[card][2])
         anio, mes, dia = str(tarjetas[card][4]).split("-")
         print("Vence:",anio+"/"+mes)
         print("--------------------------------")

def eliminarTarjeta(user):
   print("\n--- ELIMINAR METODO PAGO ---")

   while True:
         print("Seleccione el metodo a eliminar, 0 para cancelar")
         opc = int(opcionnumerica())

         if opc == 0:
            limpiarPantalla()
            return
         
         cur.execute("SELECT ID FROM TARJETA WHERE USERID = '"+user+"'")
         resultado = cur.fetchall()

         if(opc > len(resultado)):
            print("Error. Seleccione la opcion correcta\n")
         else:
            tarjetaid = resultado[opc-1][0]
            break

   print("¿Seguro que desea eliminar el metodo #",opc,"?")
   print("1. SI"+
         "\n0. CANCELAR")
   
   opconf = validaropcion(0,1)

   if opconf == 0:
      limpiarPantalla()
      return
   
   limpiarPantalla()
   print("Eliminando metodo de pago...")

   cur.execute("DELETE FROM TARJETA WHERE ID = "+str(tarjetaid)+"")
   mercadolibreconnection.commit()

   print("Metodo Pago eliminado exitosamente")

def mostrarDetallesPublicacion(pub):
  print("\n-- DETALLE PUBLICACION")
  cur.execute(f"SELECT CATEGORIA, NOMBREPUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, PRECIOVENTA, IDVENDEDOR, STOCK, FECHAPUBLICACION FROM PUBLICACION JOIN PRODUCTO ON PUBLICACION.PRODUCTID=PRODUCTO.PRODUCTID WHERE NOPUBLICACION = "+pub+"")
  for CATEGORIA, NOMBREPUBLICACION, NOMBRE, MARCA, DESCRIPCION, PRECIOVENTA, IDVENDEDOR, STOCK, FECHAPUBLICACION in cur.fetchall():
    print('Categoria:', CATEGORIA,
          '\nNombre:',NOMBREPUBLICACION,
          '\nProducto:',NOMBRE,
          '\nMarca:',MARCA,
          '\nDescripcion:',DESCRIPCION,
          '\nPrecio:',PRECIOVENTA,
          '\nVendedor:',IDVENDEDOR,
          '\nStock:',STOCK,
          '\nPublicado el:',FECHAPUBLICACION)
    
def listarAtributosClientes(cur):
  categorias = []
  productos = []
  marcas = []
  vendedores = []
  activa = "Activa"
  cur.execute(f"SELECT CATEGORIA, NOMBRE, MARCA, IDVENDEDOR FROM PUBLICACION JOIN PRODUCTO ON PUBLICACION.PRODUCTID=PRODUCTO.PRODUCTID WHERE ESTADO = '{activa}'")
  for CATEGORIA, NOMBRE, MARCA, IDVENDEDOR in cur.fetchall():
    categorias.append(CATEGORIA)
    productos.append(NOMBRE)
    marcas.append(MARCA)
    vendedores.append(IDVENDEDOR)
  return categorias, productos, marcas, vendedores
    
def mostrarPublicacionfiltrada(cur, prod=None, marc=None, categ=None, vend=None, ord=None, prec=None, ord_price=None):
  print("\n-- PUBLICACIONES --\n")
  categorias, productos, marcas, vendedores= listarAtributosClientes(cur)
  activa = "Activa"
  consulta = f"SELECT PRODUCTO.CATEGORIA, NOMBREPUBLICACION AS PUBLICACION, PRODUCTO.NOMBRE, PRODUCTO.MARCA, DESCRIPCION, PRECIOVENTA AS PRECIO, IDVENDEDOR AS VENDEDOR, STOCK, FECHAPUBLICACION AS PUBLICADO FROM PUBLICACION JOIN PRODUCTO ON PUBLICACION.PRODUCTID=PRODUCTO.PRODUCTID WHERE ESTADO = '{activa}'"
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

  data = pd.read_sql(consulta, mercadolibreconnection)
  columnasmostrar1 = ['PUBLICACION', 'MARCA', 'PRECIO','VENDEDOR','STOCK','PUBLICADO']
  data2 = data[columnasmostrar1]
  print(data2.to_string(index=False, show_dimensions=False))

def filtrarPublicaciones():
   print("\n--- FILTRADO\n")
   print("1. Filtrar por PRODUCTO")
   print("2. Filtrar por MARCA")
   print("3. Filtrar por CATEGORIA")
   print("4. Filtrar por Vendedor")
   print("5. Filtrar por MAS RECIENTE")
   print("6. Filtrar por MAS ANTIGUA")
   print("7. Filtrar por PRECIO")
   print("8. PUBLICACIONES 2024")
   print("0. SALIR")
   
   op = validaropcion(0,8)

   if (op == 0):
      return
   
   if op == 8:
      mostrarPublicaciones2024()
      return
   
   if op == 7:
      while True:
         precio = input("Ingrese precio (ENTER PARA SALIR): ")
         if (precio == ""):
            return
         
         if precio.isnumeric() == True:
            break
         else:
            print("\nError, Ingrese un numero entero")

      print("1. Orden MAYOR")
      print("2. Orden MENOR")
      print("0. SALIR")
      opti = validaropcion(0,2)

      if opti == 0:
         return
      
      if opti == 1:
         cond = 'Mayor'
      
      if opti == 2:
         cond = 'Menor'

      limpiarPantalla()
      mostrarPublicacionfiltrada(cur,prec = precio, ord_price = cond)
      return

   if op == 5 or op == 6:
      if op == 5:
         condvis = 'Mas reciente'

      if op == 6:
         condvis = 'Mas antigua'

      limpiarPantalla()
      mostrarPublicacionfiltrada(cur, ord = condvis)
      return
   
   
   busq = input("\nIngrese palabra para BUSCAR: ")
   limpiarPantalla()
   
   if op == 1:
      mostrarPublicacionfiltrada(cur,prod = busq)
      return
   
   if op == 2:
      mostrarPublicacionfiltrada(cur, marc= busq)
      return
   
   if op == 3:
      mostrarPublicacionfiltrada(cur, categ = busq)
      return
   
   if op == 4:
      mostrarPublicacionfiltrada(cur,vend = busq)
      
def verificar_tarjeta_vencida(año_expiracion, mes_expiracion, dia_expiracion):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Verificar si la tarjeta está vencida
    if año_expiracion < fecha_actual.year or \
       (año_expiracion == fecha_actual.year and mes_expiracion < fecha_actual.month) or \
       (año_expiracion == fecha_actual.year and mes_expiracion == fecha_actual.month and dia_expiracion < fecha_actual.day):
        return True  # Tarjeta vencida
    else:
        return False  # Tarjeta no vencida

def verRespuestas(user):
   print("--- RESPUESTAS ---\n")

   consulta = "SELECT PREG.IDVENDEDOR AS VENDEDOR, MENSAJERESPUESTA AS RESPUESTA, FECHAHORARESPUESTA AS RESPONDIO, CONTENIDO AS TU_PREGUNTA, TIEMPOENVIADO AS ENVIADO, NOMBREPUBLICACION AS PUBLICACION FROM PREGUNTA PREG NATURAL JOIN PUBLICACION PUB WHERE IDCLIENTE = '"+user+"'"
   cur.execute(consulta)
   resultado = cur.fetchall()

   if len(resultado) == 0:
      print("Hasta el momento no ha realizado preguntas!")
      return
   
   for VENDEDOR, RESPUESTA, RESPONDIO, TU_PREGUNTA, ENVIADO, PUBLICACION in resultado:
      print("VENDEDOR:", VENDEDOR)

      if RESPONDIO == None:
         RESPONDIO = 'No ha respondido'
      else:
         if RESPUESTA == "":
            RESPUESTA = "No hay respuesta"

         print("RESPUESTA: ", RESPUESTA)
      
      print("RESPONDIO: ",RESPONDIO)
      print("TU PREGUNTA: ",TU_PREGUNTA)
      print("ENVIADO: ",ENVIADO)
      print("PUBLICACION: ", PUBLICACION)

      print("\n-------------------------------------------------\n")



#Programa Principal

imprimirMenuPrincipalInvitado()

mercadolibreconnection.close()

