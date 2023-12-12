# import pymysql

# miConexion = pymysql.connect(host="localhost", user='root', passwd= 'password123', db='rent_car')
# cur = miConexion.cursor()
# cur.execute("select VIN, Model from car")

# for VIN, Model in cur.fetchall():
#     print(VIN, Model)

# miConexion.close()

def bienvenida() :
    print("----- MERCADO LIBRE -----")

bienvenida()


