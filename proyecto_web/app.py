from flask import Flask, render_template, request
from modelo import obtener_videojuegos, buscar_videojuegos

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    juegos = []
    if request.method == "POST":
        termino = request.form.get("busqueda")
        juegos = buscar_videojuegos(termino)
    else:
        juegos = obtener_videojuegos()
    return render_template("index.html", videojuegos=juegos)

if __name__ == "__main__":
    app.run(debug=True)
