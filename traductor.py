import sqlite3
conexion=sqlite3.connect("bdTraductor.db")
try:
    conexion.execute("""create table traductor (
                        id integer primary key autoincrement,
                        espanol text,
                        ingles text
                        )""")
    print("se creo la tabla traductor")
except sqlite3.OperationalError:
    print("La tabla traductor ya existe")
conexion.close()

#cargar datos , mejorar el codigo
conexion=sqlite3.connect("bdTraductor.db")
conexion.execute("insert into traductor(espanol,ingles) values (?,?)", ('casa', 'house'))
conexion.execute("insert into traductor(espanol,ingles) values (?,?)", ('lapiz', 'pen'))
conexion.execute("insert into traductor(espanol,ingles) values (?,?)", ('oro', 'gold'))
conexion.commit()
conexion.close()

while True:
    print("Traductor ESPAÑOL a INGLES")
    palabra = input("Ingrese una palabra a traducir: ")
    conexion=sqlite3.connect("bdTraductor.db")
    sentencia = f"select ingles from traductor where espanol = '{palabra}'"
    cursor=conexion.execute(sentencia)

    for registro in cursor:
        print(f"{palabra} : {registro[0]}")
    conexion.close()
