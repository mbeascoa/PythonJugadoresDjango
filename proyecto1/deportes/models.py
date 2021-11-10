import cx_Oracle

class Jugador:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    def devolverdato(self):
        cursor = self.connection.cursor()
        dato=''
        try:
            cursor.execute("SELECT jugadores.NOMBRE,APELLIDOS,equipos.NOMBRE as equipo,NUMERO_CAMISETA  FROM jugadores "
                           "inner join equipos on jugadores.equipo_cod=equipos.equipo_cod")
        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

