"""
Função para gerar previsões a partir do modelo carregado.
Validação de input pode usar src/middleware ou schemas Pydantic.
"""
import json
from pathlib import Path
from typing import Any, List, Union

import numpy as np
import pandas as pd
import xgboost as xgb

from app.model.load_model import get_feature_names, get_model


def _get_task() -> str:
    """Retorna 'classification' ou 'regression' conforme salvo no treino."""
    base = Path(".").resolve()
    path = base / "models" / "task.json"
    if not path.exists():
        return "regression"
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f).get("task", "regression")
    except Exception:
        return "regression"


def _payload_to_dataframe(data: Union[dict, List[dict]]) -> pd.DataFrame:
    """Converte payload (dict ou lista de dicts) em DataFrame alinhado às feature names."""
    if isinstance(data, dict):
        data = [data]
    df = pd.DataFrame(data)
    feature_names = get_feature_names()
    if not feature_names:
        return df
    # Normalizar chaves: usar encontrar_coluna se necessário; aqui assumimos que podem vir com nomes iguais
    from src.utils import encontrar_coluna

    col_map = {}
    for c in df.columns:
        found = encontrar_coluna(c, feature_names) or (c if c in feature_names else None)
        if found:
            col_map[c] = found
    df = df.rename(columns=col_map)
    # Garantir ordem e colunas esperadas
    out = pd.DataFrame(index=range(len(df)))
    for f in feature_names:
        out[f] = df[f].values if f in df.columns else 0
    return out.astype(float, errors="ignore").fillna(0)


def predict(data: dict[str, Any]) -> dict[str, Any]:
    """
    Gera previsão para o payload recebido.
    Aceita: {"data": [{"ipv": 1, "ips": 2, ...}, ...]} ou {"ipv": 1, "ips": 2, ...} (um registro).
    Regra: usar colunas alinhadas às features do modelo (feature_names.json).
    """
    model = get_model()
    if model is None:
        return {
            "predictions": [],
            "message": "Modelo não carregado. Treine e salve o modelo primeiro (execute src.train.train).",
        }

    feature_names = get_feature_names()
    if not feature_names:
        return {"predictions": [], "message": "Metadados do modelo (feature_names) não encontrados."}

    # Suportar tanto {"data": [...]} quanto um único objeto
    if "data" in data and isinstance(data["data"], list):
        records = data["data"]
    elif isinstance(data, dict) and any(k in data for k in ["ipv", "ips", "iaa", "ieg", "ida"]):
        records = [data]
    else:
        records = [data] if isinstance(data, dict) else []

    if not records:
        return {"predictions": [], "message": "Nenhum registro de entrada fornecido."}

    try:
        X = _payload_to_dataframe(records)
        dmat = xgb.DMatrix(X, feature_names=feature_names)
        preds = model.predict(dmat)
        preds = np.asarray(preds)
        task = _get_task()
        if task == "classification" and preds.ndim == 1 and len(np.unique(preds)) <= 20:
            preds = preds.tolist()
        else:
            preds = [float(x) for x in preds]
        return {"predictions": preds, "message": "ok"}
    except Exception as e:
        return {"predictions": [], "message": f"Erro na previsão: {str(e)}"}
