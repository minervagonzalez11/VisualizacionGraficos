from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

# Crear un router para las rutas de gráficos
graficos = APIRouter()

# Configurar el directorio de plantillas
templates = Jinja2Templates(directory="templates/")

# Montar la carpeta `static`
graficos.mount("/static", StaticFiles(directory="static/"), name="static")

# Datos de los gráficos
graficos_info = [
    {"name": "Ventas por Categoría y Genero de Cliente", "file": "CategoriaGenero.png", "description": "Gráfico de categorías y genero de cliente.","pdf_file": "interpretaciones/VentasCategoriayGeneroCliente.pdf"},
    {"name": "Distribución de Clientes Activos e Inactivos", "file": "ClientesActivosInactivos.png", "description": "Gráfico de clientes activos e inactivos.","pdf_file": "interpretaciones/ClientesActivoseInactivos.pdf"},
    {"name": "Frecuencia de Ventas por Método de Pago", "file": "MetodoPago.png", "description": "Distribución de métodos de pago utilizados.","pdf_file": "interpretaciones/VentasporMetodoPago.pdf"},
    {"name": "Analisis de productos no vendidos o con baja de ventas", "file": "ProductosNoVendidos.png", "description": "Productos que no tuvieron ventas en el mes.","pdf_file": "interpretaciones/ProductosmenosVendidos.pdf"},
    {"name": "Ventas por Categoría", "file": "VentasCategoria.png", "description": "Gráfico de ventas por categoría.","pdf_file": "interpretaciones/VentasporCategoria.pdf"},
    {"name": "Ventas por Mes", "file": "VentasMes.png", "description": "Evolución de las ventas durante el mes.","pdf_file": "interpretaciones/VentasporMes.pdf"},
]

# Ruta principal para mostrar todos los gráficos
@graficos.get("/graficos")
def show_all_graficos(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "title": "Gráficos de la Tienda", "text": "Tienda de Ropa Haro", "graficos": graficos_info}
    )

# Ruta para detalles de cada gráfico
@graficos.get("/graficos/{grafico_name}")
def show_grafico_detail(request: Request, grafico_name: str):
    grafico = next((g for g in graficos_info if g["file"] == grafico_name), None)
    if grafico:
        return templates.TemplateResponse(
            "detalle.html",
            {"request": request, "title": grafico["name"], "grafico": grafico}
        )
    return {"error": "Gráfico no encontrado"}


#uvicorn api:app --reload