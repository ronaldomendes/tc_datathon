"""
Funções auxiliares: configs, normalização de nomes de colunas e resolução de caminhos.
Regras extraídas do notebook de análise PEDE 2024.
"""
import logging
from pathlib import Path
from typing import List, Optional

# Configurações do dataset PEDE 2024 (conforme notebook)
COLS_TARGET = ["ipv", "ips", "iaa", "ieg", "nº_av", "ida", "Defasagem"]
EXCEL_FILENAME = "BASE DE DADOS PEDE 2024 - DATATHON.xlsx"
DATA_DIR = "files"

logger = logging.getLogger(__name__)


def get_data_path() -> Path:
    """Retorna o caminho do Excel PEDE 2024 (raiz do projeto ou pai)."""
    base = Path(".").resolve()
    path_excel = base / DATA_DIR / EXCEL_FILENAME
    if not path_excel.exists():
        path_excel = base.parent / DATA_DIR / EXCEL_FILENAME
    return path_excel


def normalizar(s: str) -> str:
    """
    Normaliza string para comparação de nomes de colunas.
    Regra: strip, lower, substitui '_' e 'º' por espaço, colapsa espaços duplos.
    """
    s = s.strip().lower().replace("_", " ").replace("º", " ").replace("  ", " ")
    return s.strip()


def encontrar_coluna(nome: str, colunas_df: List[str]) -> Optional[str]:
    """
    Encontra no DataFrame a coluna que corresponde ao nome desejado (após normalização).
    Regra: compara nome normalizado e variante com underscore.
    """
    nome_norm = normalizar(nome)
    for col in colunas_df:
        col_norm = normalizar(col)
        if nome_norm == col_norm or nome_norm.replace(" ", "_") == col_norm.replace(" ", "_"):
            return col
    return None
