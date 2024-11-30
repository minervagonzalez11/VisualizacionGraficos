import os
from typing import List, Dict

# Ruta base donde se almacenan las imágenes de los gráficos
BASE_DIR = "static/graficas/"

# Listas para almacenar los gráficos y sus detalles
list_graficos: List[str] = []
list_detalles = []

# Función para obtener todos los gráficos
def all_graficos() -> List[Dict]:
    if not list_graficos:
        # Listar todos los archivos en el directorio de gráficos
        list_graficos.extend([file for file in os.listdir(BASE_DIR) if file.endswith((".png", ".jpg", ".jpeg"))])

    # Crear una lista con información básica de cada gráfico
    return [{"id": i + 1, "imagen": f"{BASE_DIR}{file}"} for i, file in enumerate(list_graficos)]

# Función para obtener detalles de cada gráfico
def graficos_details() -> List[Dict]:
    if not list_detalles:
        all_graficos()  # Asegurarse de que los gráficos estén listados

        # Crear detalles ficticios para cada gráfico (puedes personalizarlos)
        for i, grafico in enumerate(list_graficos):
            detalles = {
                "id": i + 1,
                "titulo": f"Gráfico {i + 1}",
                "descripcion": f"Este es el gráfico número {i + 1}.",
                "imagen": f"{BASE_DIR}{grafico}",
            }
            list_detalles.append(detalles)

    return list_detalles
