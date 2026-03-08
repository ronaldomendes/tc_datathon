"""
Testes de limpeza e transformação: normalização de colunas, seleção de colunas de interesse.
Regras validadas: normalizar(), encontrar_coluna(), selecionar_colunas_interesse().
"""
import pytest

from src.utils import COLUNAS_INTERESSE, normalizar, encontrar_coluna


class TestNormalizar:
    """Testes da função normalizar (regra do notebook)."""

    def test_lowercase(self):
        assert normalizar("IPV") == "ipv"

    def test_strip(self):
        assert normalizar("  ipv  ") == "ipv"

    def test_underscore_to_space(self):
        assert normalizar("nº_av") == "n av"

    def test_collapse_spaces(self):
        assert normalizar("a   b") == "a b"


class TestEncontrarColuna:
    """Testes da função encontrar_coluna (regra do notebook)."""

    def test_match_exact_after_normalize(self):
        cols = ["IPV", "IPS", "IAA"]
        assert encontrar_coluna("ipv", cols) == "IPV"

    def test_match_with_underscore(self):
        cols = ["nº_av", "ida"]
        assert encontrar_coluna("nº_av", cols) == "nº_av"
        assert encontrar_coluna("n av", cols) == "nº_av"

    def test_no_match_returns_none(self):
        cols = ["IPV", "IPS"]
        assert encontrar_coluna("inexistente", cols) is None


class TestColunasInteresse:
    """Regra: colunas de interesse definidas no notebook."""

    def test_colunas_definidas(self):
        assert "ipv" in COLUNAS_INTERESSE
        assert "Defasagem" in COLUNAS_INTERESSE
        assert "ida" in COLUNAS_INTERESSE
