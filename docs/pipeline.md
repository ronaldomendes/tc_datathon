# Etapas do pipeline de Machine Learning

1. **Pré-processamento** (`src.preprocessing`):
    - Carregar o Excel PEDE (todas as abas concatenadas).
    - Selecionar colunas de interesse (com normalização de nomes: `ipv`, `ips`, `iaa`, `ieg`, `nº_av`, `ida`, `Defasagem`).
    - Binarizar o target: `Defasagem` < 0 → 1, caso contrário → 0.

2. **Engenharia de features** (`src.feature_engineering`):
    - Módulo para atributos derivados; atualmente retorna cópia do DataFrame (expansão conforme EDA).

3. **Treino e validação** (`src.train`):
    - Separação de features e target; preenchimento de faltantes (mediana); apenas colunas numéricas.
    - Split treino/validação (ex.: 80/20), com estratificação em tarefas de classificação.
    - Inferência automática da tarefa (classificação binária/multiclasse ou regressão) a partir do target.
    - XGBoost (XGBClassifier ou XGBRegressor) com parâmetros configuráveis; métricas (AUC, F1, precision, recall, etc.) e figuras (matriz de confusão, curva ROC) registradas no MLflow.
    - Modelo e metadados salvos em disco; artefato também registrado no MLflow.

4. **Avaliação** (`src.evaluate`):
    - Cálculo de métricas (accuracy, F1, ROC-AUC para classificação; MSE, MAE, R² para regressão).

5. **Pós-processamento / uso**:
    - A API carrega o modelo mais recente em `mlartifacts` e aplica as mesmas features (`feature_names.json`) na ordem esperada; conversão de payload para DataFrame e previsão via XGBoost.
