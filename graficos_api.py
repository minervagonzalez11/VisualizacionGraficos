import os
from typing import List, Dict

#ruta base donde se almacenan las imagenes de los graficos
BASE_DIR = "static/graficas/"

#listas para almacenar los graficos y sus detalles
list_graficos: List[str] = []
list_detalles = []

#funcion para obtener todos los graficos
def all_graficos() -> List[Dict]:
    if not list_graficos:
        #listar todos los archivos en el directorio de graficos
        list_graficos.extend([file for file in os.listdir(BASE_DIR) if file.endswith((".png", ".jpg", ".jpeg"))])

    #crear una lista con informacion basica de cada grafico
    return [{"id": i + 1, "imagen": f"{BASE_DIR}{file}"} for i, file in enumerate(list_graficos)]

#funcion para obtener detalles de cada grafico
def graficos_details() -> List[Dict]:
    if not list_detalles:
        all_graficos()  #asegura de que los graficos esten listados

        #crea  detalles ficticios para cada gráfico (puedes personalizarlos)
        for i, grafico in enumerate(list_graficos):
            detalles = {
                "id": i + 1,
                "titulo": f"Gráfico {i + 1}",
                "descripcion": f"Este es el gráfico número {i + 1}.",
                "imagen": f"{BASE_DIR}{grafico}",
            }
            list_detalles.append(detalles)

    return list_detalles
