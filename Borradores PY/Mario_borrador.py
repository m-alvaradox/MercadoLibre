import pymysql
from datetime import datetime, date, timedelta

mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='invitado', passwd= 'root', db='mercadolibre')
#mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()


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


