"""
Inicialização da API (FastAPI).
"""

import gradio as gr
import requests
from fastapi import FastAPI

from app.routes import router as prediction_router
from src.middleware import register_middleware

tags_metadata = [
    {
        "name": "Prediction",
        "description": "Methods responsible for managing data and make predictions",
    },
]

app = FastAPI(
    version="1.0.0",
    title="Tech Challenge 05 - Datathon",
    description="API collection - Datathon",
    terms_of_service="#",
    license_info={"name": "Apache 2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0"},
    redoc_url="/documentation/redoc",
    docs_url="/documentation/swagger",
    openapi_url="/documentation/openapi.json",
    openapi_tags=tags_metadata
)

register_middleware(app)
app.include_router(prediction_router, prefix="", tags=["Prediction"])


# Interface Gradio para predição sem acessar a documentação
# demo = gradio_interface()
# app = gr.mount_gradio_app(app, demo, path="/ui")

def gradio_interface(ipv, ips, iaa, ieg, num_av, ida):
    """Constrói a interface Gradio para predição."""
    payload = {
        "ipv": float(ipv) if ipv is not None else 0,
        "ips": float(ips) if ips is not None else 0,
        "iaa": float(iaa) if iaa is not None else 0,
        "ieg": float(ieg) if ieg is not None else 0,
        "n_av": float(num_av) if num_av is not None else 0,
        "ida": float(ida) if ida is not None else 0,
    }
    # Chamada ao endpoint REST (ajuste a URL conforme seu servidor)
    response = requests.post("http://localhost:8000/predict", json=payload)
    out = response.json()
    return f"Classe de defasagem prevista: {out}"


# Interface Gradio
demo = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Number(label="IPV", value=0, precision=4),
        gr.Number(label="IPS", value=0, precision=4),
        gr.Number(label="IAA", value=0, precision=4),
        gr.Number(label="IEG", value=0, precision=4),
        gr.Number(label="Nº AV", value=0, precision=0),
        gr.Number(label="IDA", value=0, precision=4),
    ],
    outputs="text",
    title="Predição - Datathon Passos Mágicos",
    description="Informe os indicadores e obtenha a previsão da defasagem escolar."
)

# expondo a interface do Gradio
app = gr.mount_gradio_app(app, demo, path="/ui")
