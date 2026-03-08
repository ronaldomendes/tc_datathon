"""
Função para carregar modelo salvo.
(Regra: modelo treinado em src/train.py; API usa este loader.)
"""
import os
import glob
import json
import logging
from pathlib import Path
from typing import Any, List, Optional

import xgboost as xgb

logger = logging.getLogger(__name__)

_modelo: Optional[Any] = None
_feature_names: Optional[List[str]] = None


def _default_model_path() -> list[str]:
    return glob.glob("./mlartifacts/*/models/*/artifacts/model.ubj")


def load_model(path: list[str] = None) -> Any:
    """
    Carrega o modelo XGBoost a partir de path (model.ubj).
    Se path for None, usa caminho padrão do projeto (models/model.ubj).
    Retorna o objeto modelo (ou None se arquivo não existir).
    """
    global _modelo
    path = path if path is not None else _default_model_path()
    if not path:
        logger.warning("Arquivo de modelo não encontrado: %s", path)
        return None
    try:
        # XGBRegressor e XGBClassifier compartilham load_model; usamos Booster para ser neutro
        latest_model = max(path, key=os.path.getmtime)
        _modelo = xgb.Booster()
        _modelo.load_model(latest_model)
        logger.info("Modelo carregado de %s", path)
        return _modelo
    except Exception as e:
        logger.exception("Erro ao carregar modelo: %s", e)
        _modelo = None
        return None


def get_model() -> Optional[Any]:
    """Retorna o modelo já carregado (singleton)."""
    global _modelo
    if _modelo is None:
        _modelo = load_model()
    return _modelo


def get_feature_names() -> Optional[List[str]]:
    """Retorna a lista de nomes de features na ordem esperada pelo modelo."""
    global _feature_names
    if _feature_names is not None:
        return _feature_names
    meta_path = "./app/models/feature_names.json"

    try:
        with open(meta_path, encoding="utf-8") as f:
            _feature_names = json.load(f)
        return _feature_names
    except Exception as e:
        logger.exception("Erro ao carregar feature_names: %s", e)
        return None
