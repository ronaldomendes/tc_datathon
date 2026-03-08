"""
Limpeza e transformação dos dados PEDE 2024.
Regras: carregar aba definida, selecionar apenas colunas de interesse existentes (normalização).
"""
import logging
from pathlib import Path
from typing import List, Optional

import pandas as pd

from src.utils import (
    COLUNAS_INTERESSE,
    SHEET_NAME,
    encontrar_coluna,
    get_data_path,
)

logger = logging.getLogger(__name__)


def carregar_excel(
        path_excel: Optional[Path] = None,
        sheet_name: Optional[str] = None,
) -> pd.DataFrame:
    """
    Carrega o Excel PEDE 2024 na aba indicada.
    Se path_excel não for passado, usa get_data_path().
    """
    path = path_excel or get_data_path()
    sheet = sheet_name or SHEET_NAME
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    df = pd.read_excel(path, sheet_name=sheet)
    logger.info("Dimensões do dataset carregado: %s linhas, %s colunas", df.shape[0], df.shape[1])
    return df


def selecionar_colunas_interesse(
        df: pd.DataFrame,
        colunas: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Seleciona apenas as colunas de interesse que existem no arquivo.
    Regra: para cada nome em colunas, usa encontrar_coluna(); colunas não encontradas são ignoradas com aviso.
    """
    colunas = colunas or COLUNAS_INTERESSE
    colunas_ok = []
    for c in colunas:
        encontrada = encontrar_coluna(c, list(df.columns))
        if encontrada is not None:
            colunas_ok.append(encontrada)
        else:
            logger.warning("Coluna '%s' não encontrada no arquivo.", c)
    out = df[colunas_ok].copy()
    logger.info("Colunas utilizadas na análise (%s): %s", len(out.columns), list(out.columns))
    return out


def preparar_dados(
        path_excel: Optional[Path] = None,
        sheet_name: Optional[str] = None,
        colunas: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Pipeline: carrega o Excel e retorna apenas as colunas de interesse (existentes).
    """
    df = carregar_excel(path_excel=path_excel, sheet_name=sheet_name)
    df['Defasagem'] = df['Defasagem'].apply(lambda x: 1 if x < 0 else 0)
    return selecionar_colunas_interesse(df, colunas=colunas)
