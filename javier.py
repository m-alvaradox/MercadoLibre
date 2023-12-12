import pymysql

miConexion = pymysql.connect(host="localhost", user='root', passwd= 'Walboli-18', db='mercado_libre')
cur = miConexion.cursor()
cur.execute("select PRODUCT_ID, NOMBRE from PRODUCTO")

for PRODUCT_ID, NOMBRE in cur.fetchall():     
    print(PRODUCT_ID, NOMBRE)

miConexion.close()
