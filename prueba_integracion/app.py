from flask import Flask, request, render_template, redirect, flash
import os
from werkzeug.utils import secure_filename
import mysql.connector

app = Flask(__name__)
app.secret_key = "clave_secreta"
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def guardar_mensaje_en_bd(nombre_archivo):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rafaela13",
            database="bd_videos_juegos"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Mensajes (archivo) VALUES (%s)", (nombre_archivo,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Error al guardar en BD:", e)
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        archivo = request.files["archivo"]
        if archivo:
            nombre_seguro = secure_filename(archivo.filename)
            ruta = os.path.join(app.config['UPLOAD_FOLDER'], nombre_seguro)
            archivo.save(ruta)

            # PRUEBA DE INTEGRACIÓN:
            guardado = guardar_mensaje_en_bd(nombre_seguro)
            if guardado:
                flash("Mensaje multimedia enviado con éxito.")
            else:
                flash("Error al registrar mensaje en la base de datos.")

            return redirect("/")
    return render_template("formulario.html")

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
