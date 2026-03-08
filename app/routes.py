"""
Definição dos endpoints (ex.: /predict).
"""
from typing import Any

from fastapi import APIRouter

from app.model.predict import predict

router = APIRouter()


@router.post("/predict", tags=["Prediction"],
             summary="Previsão com o modelo de dados da Passos Mágicos",
             response_description="Lista de previsões e mensagem de status")
async def predict_endpoint(data: dict[str, Any]):
    """
    Recebe dados de entrada (indicadores: ipv, ips, iaa, ieg, nº_av, ida) e retorna
    previsão usando o modelo XGBoost carregado.

    **Formato:** um objeto com as features ou `{"data": [{"ipv": 1, "ips": 2, ...}, ...]}` para lote.
    Use a interface em **/ui** para prever sem chamar a API diretamente.
    """
    return predict(data)
