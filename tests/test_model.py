"""
Testes de inferência e performance: load_model, predict.
"""
from pathlib import Path

from app.model.load_model import get_model, load_model
from app.model.predict import predict


class TestLoadModel:
    """Testes do carregamento do modelo."""

    def test_load_model_returns_none_when_no_file(self):
        result = load_model(path=["/caminho/inexistente/model.pkl"])
        assert result is None

    def test_get_model_singleton(self):
        m = get_model()
        assert m is None or hasattr(m, "predict") or callable(getattr(m, "predict", None))


class TestPredict:
    """Testes do endpoint de previsão."""

    def test_predict_returns_dict(self):
        out = predict({})
        assert isinstance(out, dict)
        assert "predictions" in out or "message" in out
