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
import os
import time


# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='invitado', passwd= 'root', db='mercadolibre')
#mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'root', db='mercadolibre')
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
        
  cur.execute("INSERT INTO USUARIO(USERID,PASS,NOMBRE,APELLIDO,FECHANACIMIENTO,ESCLIENTE,ESVENDEDOR,EMAIL,TELEFONO) VALUES ('"+userName+"','"+password+"','"+nombre+"','"+apellido+"','"+fechanacimiento+"',true,false,'"+email+"','"+telefono+"')")
  cur.execute("INSERT INTO CLIENTE VALUES ('"+userName+"')")
  mercadolibreconnection.commit()
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
       limpiarPantalla()
       mostrarPublicaciones()
       print("\nPara generar una orden, debe iniciar sesión o crear una cuenta en Mercado Libre")
       input("Presione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 4:
       limpiarPantalla()
       mostrarPublicaciones2023()
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 5:
       limpiarPantalla()
       mostrarAccesoriosAutos()
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

def AccionarUsuario(opcion,user):
    
    if opcion == 0:
       print("Adios")
       exit()
       
    if opcion == 1:
      limpiarPantalla()
      print("Sesion cerrada exitosamente")
      imprimirMenuPrincipalInvitado()

    if opcion == 12:
       mostrarPublicaciones()
       print("\nSeleccione la publicacion de su interés\nPara SALIR digite 0")
       pub = opcionnumerica()

       if(pub == "0"):
          limpiarPantalla()
          return
       else:
          generarOrden(pub,user)
          imprimirMenuPrincipalUsuario(user)

    if opcion == 2:
       limpiarPantalla()
       conduser = actualizarUsuario(user)

       if (conduser != None):
          user = conduser
          imprimirMenuPrincipalUsuario(user)

    if opcion == 3:
       limpiarPantalla()
       conduser2 = eliminarUsuario(user)

       if(conduser2 == None):
          imprimirMenuPrincipalInvitado()

    if opcion == 4:
       limpiarPantalla()
       verReclamos(user)
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()


    if opcion == 5:
       limpiarPantalla()
       mostrarCupones(user)
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 6:
       limpiarPantalla()
       mostrarPerfil(user)
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 7:
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

    if opcion == 8:
       limpiarPantalla()
       mostrarcompras(user)
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
             
    if opcion == 9:
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

    if opcion == 10:
       limpiarPantalla()
       crearpublicacion(user)

    if opcion == 11:
       limpiarPantalla()
       verventas(user)
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 13:
       limpiarPantalla()
       responderpregunta(user)
       limpiarPantalla()

    if opcion == 14:
       limpiarPantalla()
       mostrarPublicaciones2023()
       input("\nPresione ENTER para regresar -->")
       limpiarPantalla()

    if opcion == 15:
       limpiarPantalla()
       mostrarAccesoriosAutos()
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
        print('4. Ver Recientes Publicaciones 2023')
        print('5. Productos existentes de categoria Autos')

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
       print('2. Modificar Cuenta')
       print('3. Eliminar Cuenta')
       print('4. Reclamos')
       print('5. Mis Cupones')
       print('6. Mi Perfil')
       print('7. Direcciones registradas')
       print('8. Mis Compras')
       print("9. Mis Facturas")
       print("10. Vender")
       print("11. Mis Ventas")
       print("12. Ver Publicaciones")
       print("13. Responder Preguntas")
       print("14. Ver Recientes Publicaciones 2023")
       print("15. Productos existentes de categoria Autos")
       print('0. SALIR')
       op = validaropcion(0,15)

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

    if op3 == 1:
      print("\n-- PAGO")
      while True:
         print("Asocie un numero de transaccion para generar la orden, 0 para CANCELAR")
         trans = opcionnumerica()

         if(int(trans) == 0):
            limpiarPantalla()
            print("Orden Cancelada")
            return


         cur.execute("SELECT TRANSID, METODO, MONTO, CUOTA, CARDNUMBER FROM PAGO WHERE TRANSID = "+trans+" AND MONTO = "+str(total)+" AND IDCLIENTE = '"+user+"'")
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
         else:
            limpiarPantalla()
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

   cur.execute("INSERT INTO DIRECCION (PARROQUIA, REFERENCIAS, IDCIUDAD, USERID) VALUES ('"+parroquia+"','"+referencias+"',"+str(idciudad)+",'"+user+"')")
   mercadolibreconnection.commit()

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

   cur.execute("DELETE FROM DIRECCION WHERE ID = "+str(direccionid)+"")
   mercadolibreconnection.commit()

   print("Direccion eliminada exitosamente")

def mostrarcompras(user):
   print("--- MIS COMPRAS ---\n")
   cur.execute("SELECT * FROM ORDEN WHERE IDCLIENTE = '"+user+"'")
   listacompras = cur.fetchall()
   
   for i in range(len(listacompras)):
      print("---------------------------------------------")
      print("COMPRA #",listacompras[i][0])
      print("Fecha:",listacompras[i][1])
      print("Estado:",listacompras[i][2])
      print("Unidad:",listacompras[i][3])
      print("Envio: ",listacompras[i][5])
      print("Importe:",listacompras[i][4])

      cur.execute("SELECT NOMBRE FROM PRODUCTO WHERE PRODUCTID ="+str(listacompras[i][11])+"")
      print("Producto:",cur.fetchone()[0])

      cur.execute("SELECT NOMBREPUBLICACION FROM PUBLICACION WHERE NOPUBLICACION ="+str(listacompras[i][16])+"")
      print("Publicacion:",cur.fetchone()[0])

      print("Vendedor:",listacompras[i][14])

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

   cur.execute("UPDATE ORDEN SET ESTRELLASPRODUCTO = "+str(estrellasproducto)+", ESTRELLASVENDEDOR = "+str(estrellasvendedor)+", COMENTARIO = '"+comentario+"' WHERE ORDERID = "+comp+"")
   mercadolibreconnection.commit()

   limpiarPantalla()
   print("\nOrden calificada!")

def mostrarProductos():
   print("--- PRODUCTOS ---\n")
   cur.execute("SELECT * FROM PRODUCTO")
   listaProductos = cur.fetchall()
   
   for i in range(len(listaProductos)):
      print("---------------------------------------------")
      print("ID",listaProductos[i][0])
      print("Nombre:",listaProductos[i][1])
      print("Marca:",listaProductos[i][2])
      print("Categoria:",listaProductos[i][3])
      print("Subcategoria: ",listaProductos[i][4])

# Publicaciones
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
      elif(tipoExposicion == "3"): #Premium op3
         tipoExposicion == "Premium"
         break
      else:
         print("Ingrese una opción válida")
         

   print("\n-- Busquemos tu producto en nuestro catálogo, si tu producto a vender no esta en lista, ingresalo 0 para agregarlo")
   print("\nEnter para SALIR")
   #mostrarProductos() eliminado
   
   #mod

   while True:
      lproductos = []

      cur.execute("SELECT PRODUCTID FROM PRODUCTO")
      for PRODUCTOID in cur.fetchall():
         lproductos.append(PRODUCTOID[0]) #lproductos almacena productid


      mostrarProductos()
      idProducto = input("Ingrese el ID del producto o ingrese 0 para agregar uno nuevo:")
      
      # ENTER para SALIR
      if(idProducto == ""):
         limpiarPantalla()
         print("Operacion cancelada!")
         return
      
      
      if(idProducto!= "0"):
         if(int(idProducto) in lproductos): #ProductID es un atributo tipo entero
            break
         else:
            print("\n ingrese una ID existente")
      else:
         print("\nRegistrando Producto")
         
         # ProductID es auto incremental
         """
         idProducto = input("Ingrese un ID para el producto: ")
         if idProducto == "":
            limpiarPantalla()
            return
         if(idProducto in lproductos):
            idProducto = input("\nIngrese un ID no existente: ")

         """

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
         
         #id del producto es autoincremental
         print("\nRegistrando Producto")
         query = "INSERT INTO PRODUCTO (NOMBRE, MARCA, CATEGORIA, SUBCATEGORIA) VALUES (%s, %s, %s, %s)"
         values = (nProducto, mProducto, cProducto, scProducto)
         cur.execute(query, values)
         mercadolibreconnection.commit() # no se insertaba en la bd por esto
         
         print("\nProducto registrado existosamente")
      
   nombrePublicacion = input("Ingresa el nombre para tu publicación: ")
   descrpicion = input(" Redacta la descripción que deseas que los clientes observen en tu publicación: ")
   precio = input("Ingresa el precio de venta al público: $")
   stock = input("Ingresa la cantidad de stock que posees: ")
   now = datetime.now()

   cur.execute("UPDATE USUARIO SET ESVENDEDOR = true WHERE USERID='"+user+"'")
   mercadolibreconnection.commit()
      
   lVenderdores = []
   cur.execute("SELECT USERID FROM VENDEDOR")
   for USERID in cur.fetchall():
         lVenderdores.append(USERID[0])
   if(user not in lVenderdores):
         cur.execute("INSERT INTO VENDEDOR(USERID) VALUES ('"+user+"')")

   limpiarPantalla()
   print("Creando Publicacion...")
   cur.execute("INSERT INTO PUBLICACION (DESCRIPCION,TIPOEXPOSICION,PRODUCTID,IDVENDEDOR,PRECIOVENTA,ESTADO,FECHAPUBLICACION,NOMBREPUBLICACION,STOCK) VALUES ('"+descrpicion+"','"+tipoExposicion+"','"+idProducto+"','"+user+"','"+precio+"','Activa','"+str(now)+"','"+nombrePublicacion+"','"+stock+"')")
   mercadolibreconnection.commit()
   print("\nHas publicado tu venta")

#Visualizacion de publicaciones
#Esta funcion debe ser llamada despues de abrir a detalle una publicacion de eleccion del user, recuperando el numero de
def registrarVisualizacion(user,noPublicacion):
   cur.execute("INSERT INTO VISUALIZACION_PUBLICACIONES (USERID, NOPUBLICACION, FECHA) VALUES ('"+user+"','"+noPublicacion+"','"+str(datetime.now)+"')")
   mercadolibreconnection.commit()

def mostrarPublicacionesDeInteres(user):
   cur.execute("SELECT p.NOPUBLICACION, p.NOMBREPUBLICACION, p.IDVENDEDOR, p.PRECIOVENTA, p.FECHAPUBLICACION from VISUALIZACION_PUBLICACIONES vp JOIN PUBLICACION p USING (NOPUBLICACION) WHERE USERID = '"+user+"'")
   print("\nPubliicaciones Visitadas")
   for NOPUBLICACION, NOMBREPUBLICACION, IDVENDEDOR, PRECIOVENTA, FECHAPUBLICACION, FECHA in cur.fetchall():
      print('Publicacion #',NOPUBLICACION,
          '\nNombre: ',NOMBREPUBLICACION,
          '\nVendedor: ',IDVENDEDOR,
          '\nPrecio: ',PRECIOVENTA,
          '\nPublicado el: ',FECHAPUBLICACION,
          '\nVista el: ',FECHA,
          '\n-----------------------------------\n')


# Facturas
   
def mostrarFacturas(user):
   limpiarPantalla()
   print("\n--- MIS FACTURAS ---\n")

   cur.execute("SELECT FACTID, FECHA, DESCRIPCION, FACT.IDVENDEDOR, FACT.IDCLIENTE, FACT.IDORDEN, NOMBRE FROM FACTURA FACT JOIN ORDEN USING (IDCLIENTE) JOIN PRODUCTO USING (PRODUCTID) WHERE FACT.IDCLIENTE = '"+user+"'")
   detallesfacturas = cur.fetchall()

   if (len(detallesfacturas) == 0):
      limpiarPantalla()
      print("No hay facturas")
      return
   
   for factura in detallesfacturas:
      print("FACT #",factura[0])
      print("Fecha Emision:",factura[1])
      print("Descripcion: ",factura[2])
      print("Vendedor:",factura[3])
      print("Cliente:",factura[4])
      print("Orden:",factura[5])
      print("Producto:",factura[6])
      print("-------------------------------")


def mostrarFacturasEmitidas(user):
   print("--- FACTURAS EMITIDAS ---")
   cur.execute("SELECT FACTID, FECHA, DESCRIPCION, FACT.IDCLIENTE, FACT.IDORDEN, NOMBRE FROM PRODUCTO PROD JOIN ORDEN ORD USING(PRODUCTID) JOIN FACTURA FACT ON IDORDEN = ORDERID JOIN VENDEDOR V ON FACT.IDVENDEDOR = USERID WHERE FACT.IDVENDEDOR ='"+user+"'")
   resultado = cur.fetchall()

   if len(resultado) == 0:
      limpiarPantalla()
      print("No dispone de facturas emitidas actualmente!")
      return
   
   for i in resultado:
      print("FACT #",i[0])
      print("Fecha Emision:",i[1])
      print("Descripcion: ",i[2])
      print("Cliente:",i[3])
      print("Orden:",i[4])
      print("Producto:",i[5])
      print("-------------------------------")

def EmitirFactura(user):
   print("\n--- EMISION DE FACTURA ---\n")

   cur.execute("SELECT ORDERID, FACT.IDORDEN, ORDEN.IDCLIENTE, ORDEN.IDVENDEDOR, ESTADO"+
               " FROM FACTURA FACT RIGHT JOIN  ORDEN ON IDORDEN = ORDERID"+
               " WHERE FACT.IDORDEN IS NULL AND ORDEN.IDVENDEDOR = '"+user+"' AND ESTADO = 'Completada'")

   ordenespendientesfacturar = cur.fetchall()

   if(len(ordenespendientesfacturar) == 0):
      limpiarPantalla()
      print("Estimado usuario, no tiene ordenes que facturar!\n")
      return

   print("Estimado usuario, les presentamos las siguientes ordenes a facturar\n")
   for orden in ordenespendientesfacturar:
      cur.execute("SELECT NOMBRE FROM ORDEN JOIN PRODUCTO USING(PRODUCTID) WHERE ORDERID ="+str(orden[0]))
      print("ORDEN #",orden[0])
      print("Producto:",cur.fetchone()[0])
      print("Cliente:",orden[2])
      print("Estado Orden:",orden[4])
      print("--------------------------------")

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
   cur.execute("INSERT INTO FACTURA (FECHA, DESCRIPCION, IDVENDEDOR, IDCLIENTE, IDORDEN) VALUES ('"+fecha_actual_str+"',"+descripcion+",'"+str(ordenespendientesfacturar[indice][3])+"','"+str(ordenespendientesfacturar[indice][2])+"',"+str(ordenespendientesfacturar[indice][0])+")")
   mercadolibreconnection.commit()
   cur.execute("SELECT FACTID FROM FACTURA WHERE IDORDEN = "+str(ordenespendientesfacturar[indice][0])+"")
   print("FACT#",cur.fetchone()[0],"generada con exito")


# Reclamos
   
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

   cur.execute("INSERT INTO RECLAMO (TIPO, ESTADO, CLIENTEID, VENDEDORID, ORDERID, FECHAINGRESO) VALUES"+
               "('"+tipo+"','Abierto','"+user+"','"+idvendedor+"',"+comp+",now())")
   mercadolibreconnection.commit()
   cur.execute("SELECT ID FROM RECLAMO WHERE ORDERID = "+comp+" AND CLIENTEID = '"+user+"'")
   print("Reclamo #"+str(cur.fetchone()[0])+" generado con exito!")

def validarUsuario(usuario):
    cur.execute("SELECT USERID FROM USUARIO")
    usuarios = []
    for user in cur.fetchall():
        usuarios.append(user[0])
    if usuario in usuarios:
        return True
    else:
        return False

#Funciones Javier
        
def actualizarUsuario(user):  #funcion parametrizada
    print("\n--- MODIFICAR CUENTA ---")
    print("Enter para SALIR\n")

    dato = input("Ingrese el dato que desea actualizar\nUserID, Email, Pass, Nombre, Apellido, Telefono:\n").lower()
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


def eliminarUsuario(user): #funcion parametrizada
    print("--- ELIMINAR CUENTA "+user+" ---")
    print("Te echaremos de menos :(\n")
    
    validacion = input("¿Está seguro que quiere eliminar su cuenta?\n¡Esta acción no se puede revertir!\nEscriba 'si' para confirmar\nENTER para SALIR\n")
    if validacion.lower() == "si":
        try:
            print("Eliminando usuario...")
            mercadolibreconnection.begin()
            cur.execute("DELETE FROM VISUALIZACION_PUBLICACIONES WHERE USERID = '"+ user +"' or NOPUBLICACION IN (SELECT NOPUBLICACION FROM PUBLICACION WHERE IDVENDEDOR = '"+ user +"');")
            cur.execute("DELETE FROM FACTURA WHERE IDCLIENTE = '"+ user +"' OR IDVENDEDOR = '"+ user +"';")
            cur.execute("DELETE FROM RECLAMO WHERE CLIENTEID = '"+ user +"' OR VENDEDORID = '"+ user +"';")
            cur.execute("DELETE FROM ORDEN WHERE IDCLIENTE = '"+ user +"' OR IDVENDEDOR = '"+ user +"';")
            cur.execute("DELETE FROM PAGO WHERE IDCLIENTE = '"+ user +"';")
            cur.execute("DELETE FROM DIRECCION WHERE USERID = '"+ user +"';")
            cur.execute("DELETE FROM CUPON WHERE CLIENTEID = '"+ user +"';")
            cur.execute("DELETE FROM PREGUNTA WHERE IDCLIENTE = '"+ user +"' OR IDVENDEDOR = '"+ user +"';")
            cur.execute("DELETE FROM PUBLICACION WHERE  IDVENDEDOR = '"+ user +"';")
            cur.execute("DELETE FROM CLIENTE WHERE USERID = '"+ user +"';")
            cur.execute("DELETE FROM VENDEDOR WHERE USERID = '"+ user +"';")
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

def verventas(user): #funcion parametrizada
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


def responderpregunta(userid): #funcion parametrizada
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
        #id,tipo,estado,clienteid, vendedorid,orderid = reclamo # ?
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
        #id,tipo,estado,clienteid, vendedorid,orderid = reclamo # ?
        print("ID DEL RECLAMO:",reclamo[0])
        print("Tipo:",reclamo[1])
        print("Estado:",reclamo[2]) 
        print("Cliente:", reclamo[3])
        print("Vendedor:", reclamo[4])
        print("")
    print("")


#Programa Principal
imprimirMenuPrincipalInvitado()


mercadolibreconnection.close()