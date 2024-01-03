def generarOrden(nopublicacion, user):
    while True:
        cantidad = int(input("Ingrese la cantidad deseada: "))
        cur.execute("SELECT STOCK FROM PUBLICACION WHERE NOPUBLICACION = ",cantidad)
        for STOCK in cur.fetchall():
            if cantidad <= STOCK:
                break
            else:
                print("Sin stock\n")

generarOrden("")