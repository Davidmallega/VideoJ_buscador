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
