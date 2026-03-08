"""
Criação de atributos derivados a partir dos dados PEDE 2024.
(Reservado para features adicionais identificadas na análise exploratória.)
"""
import pandas as pd


def criar_atributos_derivados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona colunas derivadas ao DataFrame.
    Por enquanto retorna cópia; expandir conforme necessidade do modelo.
    """
    return df.copy()
