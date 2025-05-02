🎮 VideoJuegos Buscador — Tkinter CRUD + Flask + Selenium
Este repositorio contiene el desarrollo completo de un sistema de gestión y búsqueda de videojuegos. La aplicación fue originalmente construida en Tkinter como un sistema de CRUD (Crear, Leer, Actualizar, Eliminar), y luego migrada a Flask para su integración con herramientas de prueba como Selenium y Apache JMeter.

 Estructura del repositorio

├── conexion.py              # Conexión a MySQL
├── interfaz.py              # Interfaz gráfica Tkinter (CRUD)
├── modelo.py                # Operaciones CRUD en MySQL
├── assets/                  # Recursos visuales (logo, íconos)

├── flask_version/           # Versión para pruebas web
│   ├── app.py               # Aplicación web en Flask
│   ├── conexion.py
│   ├── modelo.py
│   ├── test_busqueda.py     # Script Selenium
│   ├── templates/
│   │   └── index.html
│   └── static/uploads/      # Multimedia de pruebas

Funcionalidades
🖥Tkinter (Escritorio)
Sistema CRUD de videojuegos (agregar, editar, eliminar, consultar)

Gestión visual de datos con interfaz gráfica amigable

🌐 Flask (Web)
Migración básica para habilitar búsquedas vía navegador

Permite realizar pruebas HTTP sobre localhost:5000

🤖 Selenium (Automatización)
Prueba de integración que automatiza una búsqueda en la app Flask

Captura de pantalla y validación del resultado esperado

📊 Apache JMeter (Rendimiento)
Simulación de múltiples usuarios haciendo búsquedas

Verificación de carga, rendimiento y estabilidad del sistema
