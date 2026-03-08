"""
Funções de avaliação: AUC, F1, etc.
(Integrar métricas conforme definição do desafio PEDE 2024.)
"""
from typing import Dict, Optional

import numpy as np


def compute_metrics(
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_score: Optional[np.ndarray] = None,
        task: str = "auto",
) -> Dict[str, float]:
    """
    Calcula métricas de avaliação (AUC, F1 para classificação; MSE, MAE para regressão).
    y_score opcional para AUC (probabilidades da classe positiva).
    task: "classification", "regression" ou "auto" (inferido pelo número de valores únicos em y_true).
    """
    from sklearn.metrics import (
        accuracy_score,
        f1_score,
        mean_absolute_error,
        mean_squared_error,
        roc_auc_score,
        r2_score,
    )

    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()
    n_unique = len(np.unique(y_true[~np.isnan(y_true)]))

    if task == "auto":
        task = "classification" if n_unique <= 20 else "regression"

    metrics: Dict[str, float] = {}

    if task == "classification":
        metrics["accuracy"] = float(accuracy_score(y_true, y_pred))
        # F1 macro para multiclasse, binary para binário
        average = "binary" if n_unique == 2 else "macro"
        metrics["f1"] = float(f1_score(y_true, y_pred, average=average, zero_division=0))
        if y_score is not None and n_unique == 2:
            try:
                metrics["roc_auc"] = float(roc_auc_score(y_true, y_score))
            except ValueError:
                metrics["roc_auc"] = 0.0
    else:
        metrics["mse"] = float(mean_squared_error(y_true, y_pred))
        metrics["mae"] = float(mean_absolute_error(y_true, y_pred))
        metrics["r2"] = float(r2_score(y_true, y_pred))

    return metrics
