import pymysql
from datetime import datetime

# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'Walboli-18', db='mercadolibre')
cur = mercadolibreconnection.cursor()

def validarUsuario(usuario):
    cur.execute("SELECT USERID FROM USUARIO")
    usuarios = []
    for user in cur.fetchall():
        usuarios.append(user[0])
    if usuario in usuarios:
        return True
    else:
        return False
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

def actualizarUsuario():
    userid = input("Ingrese su usuario actual:\n")
    while not validarUsuario(userid):
        print("Usuario invalido")
        userid = input("Ingrese su usuario:\n")

    dato = input("Ingrese el dato que desea actualizar\nUserID, Email, Pass, Nombre, Apellido, Telefono:\n").lower()
    newvalue = input("Ingrese el/la nuevo/a "+ dato + ":\n")

    if dato == "usuario":
        while validarUsuario(newvalue):
            print("Este usuario ya se encuentra registrado")
            newvalue = input("Ingrese el nuevo usuario:\n")
    try:
        cur.execute("UPDATE USUARIO SET " + dato.upper()+ "= %s WHERE USERID = %s",(newvalue,userid))
        mercadolibreconnection.commit()
        print("¡Su " + dato +" ha sido cambiado con éxito!")
    except Exception as e:
        print(f"Error: {e}")
    cur.close()

def eliminarUsuario(userid):
    validacion = input("¿Está seguro que quiere eliminar su cuenta?\n¡Esta acción no se puede revertir!\nEscriba 'si' para confirmar\n")
    if validacion.lower() == "si":
        try:
            mercadolibreconnection.begin()
            cur.execute("DELETE FROM VISUALIZACION_PUBLICACIONES WHERE USERID = '"+ userid +"' or NOPUBLICACION IN (SELECT NOPUBLICACION FROM PUBLICACION WHERE IDVENDEDOR = '"+ userid +"');")
            cur.execute("DELETE FROM FACTURA WHERE IDCLIENTE = '"+ userid +"' OR IDVENDEDOR = '"+ userid +"';")
            cur.execute("DELETE FROM RECLAMO WHERE CLIENTEID = '"+ userid +"' OR VENDEDORID = '"+ userid +"';")
            cur.execute("DELETE FROM ORDEN WHERE IDCLIENTE = '"+ userid +"' OR IDVENDEDOR = '"+ userid +"';")
            cur.execute("DELETE FROM PAGO WHERE IDCLIENTE = '"+ userid +"';")
            cur.execute("DELETE FROM DIRECCION WHERE USERID = '"+ userid +"';")
            cur.execute("DELETE FROM CUPON WHERE CLIENTEID = '"+ userid +"';")
            cur.execute("DELETE FROM PREGUNTA WHERE IDCLIENTE = '"+ userid +"' OR IDVENDEDOR = '"+ userid +"';")
            cur.execute("DELETE FROM PUBLICACION WHERE  IDVENDEDOR = '"+ userid +"';")
            cur.execute("DELETE FROM CLIENTE WHERE USERID = '"+ userid +"';")
            cur.execute("DELETE FROM VENDEDOR WHERE USERID = '"+ userid +"';")
            cur.execute("DELETE FROM USUARIO WHERE USERID = '"+ userid +"';")
            mercadolibreconnection.commit()
            print("¡Usuario eliminado con éxito!")

        except Exception as e:
            print(f"Error: {e}")
            mercadolibreconnection.rollback()
        finally:
            cur.close()
            mercadolibreconnection.close()
    else:
        print("Acción cancelada")

def  verventas(userid):
    cur.execute("select  idvendedor from orden o natural join producto p where idvendedor = '"+userid+"';")
    if(len(cur.fetchall())) > 0:
        print("--- REPORTE DE ORDENES ---")
        cur.execute("select  p.nombre,o.estado,idcupon, sum(cantidadproducto) sumaproductos from orden o natural join producto p where idvendedor = '"+userid+"' and estado = 'Completada' group by o.idvendedor, p.nombre,o.estado,idcupon;")
        imprimirOrden(cur.fetchall())
        cur.execute("select  p.nombre,o.estado,idcupon, sum(cantidadproducto) sumaproductos from orden o natural join producto p where idvendedor = '"+userid+"' and estado = 'Pendiente' group by o.idvendedor, p.nombre,o.estado,idcupon;")
        imprimirOrden(cur.fetchall())
        cur.execute("select  p.nombre,o.estado,idcupon, sum(cantidadproducto) sumaproductos from orden o natural join producto p where idvendedor = '"+userid+"' and estado = 'En curso' group by o.idvendedor, p.nombre,o.estado,idcupon;")
        imprimirOrden(cur.fetchall())
    else:
        print("Por ahora usted no tiene ordenes realizadas")

# -- Preguntas: El usuario vendedor puede revisar las preguntas que hacen los clientes en cada publicacion, 
# -- asimismo puede enviar una respuesta, considerar enviar la fecha/hora de respuesta. Consultas, Modificaciones tabla preguntas
def responderpregunta(userid):
    cur.execute("SELECT IDPREGUNTA,CONTENIDO,MENSAJERESPUESTA,IDCLIENTE FROM PREGUNTA WHERE IDVENDEDOR = '"+ userid +"';")
    preguntas = cur.fetchall()
    print("\n-- PREGUNTAS --")
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

# Mis reclamos: El usuario vendedor/cliente puede ver los reclamos que ha generado o que tiene que resolver y en que estado están. Consultas
def verReclamos(userid):
    print("")
    cur.execute("select * from reclamo where clienteid = '"+userid+"'")
    reclamosGenerados = cur.fetchall()
    if(len(reclamosGenerados)>0):
        print("-- Reclamos que usted ha hecho: --")
    else:
        print("¡Usted no ha generado reclamos!")
    for reclamo in reclamosGenerados:
        id,tipo,estado,clienteid, vendedorid,orderid = reclamo
        print("ID DEL RECLAMO: " + str(id))
        print("Tipo: " + tipo)
        print("Estado: "+ estado) 
        print("Cliente: " + clienteid)
        print("Vendedor: " + vendedorid)
        print("")

    cur.execute("select * from reclamo where vendedorid = '"+userid+"'")
    reclamosPorResolver = cur.fetchall()
    if(len(reclamosPorResolver)>0):
        print("-- Reclamos por resolver: --")
    else:
        print("¡Usted no tiene reclamos!")
    for reclamo in reclamosPorResolver:
        id,tipo,estado,clienteid, vendedorid,orderid = reclamo
        print("ID DEL RECLAMO: " + str(id))
        print("Tipo: " + tipo)
        print("Estado: "+ estado) 
        print("Cliente: " + clienteid)
        print("Vendedor: " + vendedorid)
        print("")
    print("")

# Publicaciones: El usuario puede conocer las publicaciones que ha realizado (activas, no activas, etc) modificar y eliminar publicaciones. 
# Es necesario hacer joins con otras tablas para el efecto Eliminacion, modificaciones
    
def imprimirPublicaciones(userid,estado):
    cur.execute("select nopublicacion, nombrepublicacion,descripcion,precioventa, estado, stock from Publicacion where idvendedor = '"+userid+"' and estado = '"+estado+"';")
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
    for pub in publicaciones:
        id, producto,descripcion,precio,estado,stock = pub
        print("Id: " + str(id))
        print("Producto: " + producto)
        print("Descripcion: " + descripcion)
        print("Precio: $" + str(precio))
        print("Estado " + estado)
        print("Stock: " + str(stock))
    print("")

def editarPublicacion(idPublicacion):
    campoNumero = input("Seleccione el campo que desee modificar:\n1=Producto -- 2=Descripcion -- 3=Precio -- 4=Estado -- 5=Stock \nPresione otra tecla para volver\n")
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
        cur.execute("delete from pregunta where nopublicacion = "+idpublicacion+";")
        cur.execute("delete from factura where idorden = (select orderid from orden where idpublicacion = "+idpublicacion+");")
        cur.execute("delete from reclamo where orderid = (select orderid from orden where idpublicacion = "+idpublicacion+");")
        cur.execute("delete from orden where idpublicacion = "+idpublicacion+";")
        cur.execute("delete from visualizacion_publicaciones where nopublicacion = "+idpublicacion+";")
        cur.execute("delete from publicacion where nopublicacion = "+idpublicacion+";")
        mercadolibreconnection.commit()
    except Exception as e:
        print(f"Error{e}")
        mercadolibreconnection.rollback()


def verPublicacion(userid):
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
        editar = input("¿Desea editar/eliminar alguna publicacion?\nEditar/Eliminar/VOLVER\n").lower()
        while(editar in ["editar","eliminar"]):
            if editar == "editar":
                idpub = input("Seleccione el id de la publicacion\n")
                while idpub not in lids:
                    idpub = input("¡Id invalido! Intente nuevamente:\n")
                editarPublicacion(idpub)
            elif editar == "eliminar":
                idpub = input("Seleccione el id de la publicacion a eliminar\n")
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

verPublicacion("javirod")