import pymysql
from datetime import datetime

# Conexion a la base de datos de mercadolibre
mercadolibreconnection = pymysql.connect(host="localhost", user='root', passwd= 'user2', db='mercadolibre')
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

def eliminarUsuario():
    userid = input("Ingrese su usuario a eliminar:\n")
    while not validarUsuario(userid):
        print("Usuario invalido")
        userid = input("Ingrese su usuario:\n")
    validacion = input("¿Está eguro que quiere eliminar su cuenta?\n¡Esta acción no se puede revertir!\nEscriba 'si' para confirmar\n")
    if validacion.lower() == "si":
        try:
            mercadolibreconnection.begin()
            cur.execute("DELETE FROM VISUALIZACION_PUBLICACIONES WHERE USERID = '"+ userid +"' or NOPUBLICACION IN (SELECT NOPUBLICACION FROM PUBLICACION WHERE IDVENDEDOR = '"+ userid +"');")
            cur.execute("DELETE FROM FACTURA WHERE IDCLIENTE = '"+ userid +"' OR IDVENDEDOR = '"+ userid +"';")
            cur.execute("DELETE FROM RECLAMO WHERE CLIENTEID = '"+ userid +"' OR VENDEDORID = '"+ userid +"';")
            cur.execute("DELETE FROM ORDEN WHERE IDCLIENTE = '"+ userid +"' OR IDVENDEDOR = '"+ userid +"';")
            cur.execute("DELETE FROM PAGO WHERE IDCLIENTE = '"+ userid +"';")
            cur.execute("DELETE FROM DIRECCION WHERE USERID = '"+ userid +"';")
            cur.execute("DELETE FROM DETALLECONTACTO WHERE IDCLIENTE = '"+ userid +"' OR IDVENDEDOR = '"+ userid +"' OR IDPUBLICACION IN (SELECT NOPUBLICACION FROM PUBLICACION WHERE IDVENDEDOR = '"+ userid +"');")
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

def  verventas():
    userid = input("Ingrese su usuario:\n")
    while not validarUsuario(userid):
        print("Usuario invalido")
        userid = input("Ingrese su usuario:\n")
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


