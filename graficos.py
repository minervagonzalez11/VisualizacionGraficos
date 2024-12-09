from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
import os

#crea las rutas de graficos
graficos = APIRouter()

#configura el directorio de plantillas
templates = Jinja2Templates(directory="templates/")

#montar la carpeta static
graficos.mount("/static", StaticFiles(directory="static/"), name="static")

#datos de los graficos
graficos_info = [
    {"name": "Ventas por Categoría y Genero de Cliente", "file": "CategoriaGenero.png", "description": "Gráfico de categorías y genero de cliente.","pdf_file": "interpretaciones/VentasCategoriayGeneroCliente.pdf"},
    {"name": "Distribución de Clientes Activos e Inactivos", "file": "ClientesActivosInactivos.png", "description": "Gráfico de clientes activos e inactivos.","pdf_file": "interpretaciones/ClientesActivoseInactivos.pdf"},
    {"name": "Frecuencia de Ventas por Método de Pago", "file": "MetodoPago.png", "description": "Distribución de métodos de pago utilizados.","pdf_file": "interpretaciones/VentasporMetodoPago.pdf"},
    {"name": "Analisis de productos no vendidos o con baja de ventas", "file": "ProductosNoVendidos.png", "description": "Productos que no tuvieron ventas en el mes.","pdf_file": "interpretaciones/ProductosmenosVendidos.pdf"},
    {"name": "Ventas por Categoría", "file": "VentasCategoria.png", "description": "Gráfico de ventas por categoría.","pdf_file": "interpretaciones/VentasporCategoria.pdf"},
    {"name": "Ventas por Mes", "file": "VentasMes.png", "description": "Evolución de las ventas durante el mes.","pdf_file": "interpretaciones/VentasporMes.pdf"},
]

# Ruta de inicio: redirige a /graficos
@graficos.get("/")
def redirect_to_graficos():
    return RedirectResponse(url="/graficos")

# Ruta de inicio
@graficos.get("/")
def redirect_to_graficos():
    return RedirectResponse(url="/graficos")


#ruta principal para mostrar todos los graficos
@graficos.get("/graficos")
def show_all_graficos(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "title": "Graficos de la Tienda", "text": "Tienda de Ropa Haro", "graficos": graficos_info}
    )

#ruta para detalles de cada grafico
@graficos.get("/graficos/{grafico_name}")
def show_grafico_detail(request: Request, grafico_name: str):
    grafico = next((g for g in graficos_info if g["file"] == grafico_name), None)
    if grafico:
        return templates.TemplateResponse(
            "detalle.html",
            {"request": request, "title": grafico["name"], "grafico": grafico}
        )
    return {"error": "Gráfico no encontrado"}

@graficos.get("/diccionario-datos")
def get_diccionario_pdf():
    pdf_path = os.path.join("static", "interpretaciones", "Diccionario.pdf")
    return FileResponse(pdf_path, media_type="application/pdf", filename="Diccionario.pdf", headers={"Content-Disposition": "inline; filename=Diccionario.pdf"})



#uvicorn api:app --reload