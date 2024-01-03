import pymysql
from datetime import datetime

mercadolibreconnection = pymysql.connect(host="servergroup3.mysql.database.azure.com", user='invitado', passwd= 'root', db='mercadolibre')
cur = mercadolibreconnection.cursor()

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

    cur.execute("SELECT NOMBREPUBLICACION, STOCK, PRECIOVENTA FROM PUBLICACION WHERE NOPUBLICACION ="+str(nopublicacion)+"")
    detallespublicacion = cur.fetchone()

    while True:
        cantidad = int(input("Ingrese la cantidad deseada: "))
        if cantidad <= detallespublicacion[1]:
            break
        else:
            print("Sin stock\n")

    print("Como desea la entrega?\n"+
          "1.Entrega a domicilio\n"+
          "2.Entrega a acordar con el vendedor")
    
    op = validaropcion(1,2)

    if op == 1:
       mostrarDirecciones(user)
       

    

    
    subtotal = detallespublicacion[2] * cantidad
    print("Usted desea adquirir:",detallespublicacion[0])
    print("Cantidad:",cantidad)
    print("Subtotal:",subtotal)


generarOrden(1,'malvaradox')