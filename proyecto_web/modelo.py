from conexion import obtener_conexion

def obtener_videojuegos():
    conexion = obtener_conexion()
    resultados = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Videojuegos")
            resultados = cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener videojuegos: {e}")
        finally:
            cursor.close()
            conexion.close()
    return resultados

def buscar_videojuegos(nombre):
    conexion = obtener_conexion()
    resultados = []
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Videojuegos WHERE Titulo LIKE %s"
            cursor.execute(consulta, (f"%{nombre}%",))
            resultados = cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar videojuegos: {e}")
        finally:
            cursor.close()
            conexion.close()
    return resultados
