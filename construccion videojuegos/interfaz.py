import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import ttk
from modelo import obtener_videojuegos

root = tk.Tk()
root.title("Gestión de Videojuegos")
root.geometry("900x800")
root.resizable(False, False)

ruta_logo = os.path.join(os.path.dirname(__file__), "assets", "logo_game.png")

try:
    if os.path.exists(ruta_logo):  
        logo_image = Image.open(ruta_logo)
        logo_image = logo_image.resize((120, 120), Image.Resampling.LANCZOS)  
        logo = ImageTk.PhotoImage(logo_image)
        tk.Label(root, image=logo).pack(pady=5)
    else:
        print(f"Error: La imagen no existe en: {ruta_logo}")
except Exception as e:
    print(f"Error cargando el logo: {e}")

tk.Label(root, text="🎮 Zona de Juegos 🎮", font=("Arial", 16, "bold")).pack(pady=5)

# Añadir un Frame para agrupar elementos
frame_buscador = tk.Frame(root)
frame_buscador.pack(pady=5)

# Etiqueta y campo de texto
tk.Label(frame_buscador, text="Buscar Juego:").grid(row=0, column=0)
buscador_entry = tk.Entry(frame_buscador, width=30)
buscador_entry.grid(row=0, column=1, padx=10)

# Función para probar la búsqueda
def buscar_juego():
    texto = buscador_entry.get()
    print(f"Buscando: {texto}")

tk.Button(frame_buscador, text="Buscar", command=buscar_juego).grid(row=0, column=2)

# Frame para la tabla
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

# Scrollbar
tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

# Definir columnas
columnas = ("ID", "Título", "Género", "Clasificación", "Plataforma")
lista_videojuegos = ttk.Treeview(tree_frame, columns=columnas, show="headings", yscrollcommand=tree_scroll.set)
lista_videojuegos.pack()

tree_scroll.config(command=lista_videojuegos.yview)

# Configurar encabezados
for col in columnas:
    lista_videojuegos.heading(col, text=col, anchor="w")
    lista_videojuegos.column(col, anchor="w", width=150 if col != "ID" else 40)

def cargar_lista():
    lista_videojuegos.delete(*lista_videojuegos.get_children())  # Limpia la tabla
    datos = obtener_videojuegos()

    for videojuego in datos:
        # Cada fila es una tupla (ID, Título, Género, Clasificación, Plataforma)
        lista_videojuegos.insert("", "end", values=videojuego)

# Tras configurar la tabla, llamamos la función
cargar_lista()
botones_frame = tk.Frame(root)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Añadir Nuevo Videojuego", command=lambda: abrir_ventana_crud(None), width=20).grid(row=0, column=0, padx=10)
tk.Button(botones_frame, text="Editar Videojuego", command=lambda: abrir_edicion(), width=15).grid(row=0, column=1, padx=10)
tk.Button(botones_frame, text="Actualizar Lista", command=lambda: actualizar_lista(), width=15).grid(row=0, column=2, padx=10)

if __name__ == "__main__":
    root.mainloop()
