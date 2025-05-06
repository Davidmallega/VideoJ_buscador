from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Pedir al usuario qué juego buscar
juego = input("Ingresa el nombre del videojuego a buscar: ").strip()

# Crear el nombre del archivo de screenshot
archivo_screenshot = f"resultado_{juego.replace(' ', '_')}.png"

# Configurar el driver
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5000")
    time.sleep(1)

    # Ingresar término de búsqueda
    campo = driver.find_element(By.ID, "busqueda")
    campo.send_keys(juego)

    # Click en buscar
    boton = driver.find_element(By.XPATH, "//button[text()='Buscar']")
    boton.click()
    time.sleep(2)

    # Verificar si aparece en los resultados
    tabla = driver.find_element(By.TAG_NAME, "table")
    if juego.lower() in tabla.text.lower():
        print(f"Éxito: '{juego}' fue encontrado.")
    else:
        print(f"Advertencia: '{juego}' NO fue encontrado.")

    # Guardar pantalla
    driver.save_screenshot(archivo_screenshot)
    print(f"Captura guardada como: {archivo_screenshot}")

except Exception as e:
    print(f"Error durante la prueba: {e}")
    driver.save_screenshot("error_prueba.png")

finally:
    driver.quit()
