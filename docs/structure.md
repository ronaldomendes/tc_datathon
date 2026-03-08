Este projeto foi desenvolvido com a seguinte estrutura:

```
tc_datathon/
├── app/                          # API e lógica de aplicação
│   ├── __init__.py
│   ├── main.py                    # FastAPI + montagem da interface Gradio em /ui
│   ├── routes.py                  # Endpoints (ex.: POST /predict)
│   ├── run_pipeline.py            # Script para treinar e registrar no MLflow
│   ├── model/                     # Carregamento e predição
│   │   ├── __init__.py
│   │   ├── load_model.py          # Carrega modelo (mlartifacts/*/model.ubj)
│   │   └── predict.py             # Previsões a partir do payload
│   └── models/                    # Metadados usados pela API
│       ├── feature_names.json     # Features na ordem esperada (IPV, IPS, IAA, IEG, Nº Av, IDA)
│       └── task.json              # Tipo de tarefa (classification/regression)
├── notebooks/
│   ├── eda.ipynb                  # Análise exploratória dos dados
│   └── test.ipynb                 # Testes do modelo
├── src/                           # Pipeline de ML
│   ├── __init__.py
│   ├── preprocessing.py           # Carrega Excel PEDE, seleciona colunas, prepara target
│   ├── feature_engineering.py     # Atributos derivados (expandível)
│   ├── train.py                   # Treino XGBoost, MLflow, salva modelo e metadados
│   ├── evaluate.py                 # Métricas (AUC, F1, accuracy; ou MSE, MAE, R²)
│   ├── middleware.py              # CORS, logging, /health, /metrics
│   └── utils.py                   # Caminhos, normalização de colunas (PEDE 2024)
├── tests/
│   ├── __init__.py
│   └── test_model.py              # Testes de load_model e predict
├── mlartifacts/                   # Artefatos MLflow (model.ubj por run)
├── docker-compose.yml             # Serviço API (porta 8000, volume mlartifacts)
├── Dockerfile                     # Imagem da API (Python 3.11, uvicorn)
├── mkdocs.yml                     # Configuração MkDocs
├── mkdocs-requirements.txt        # Dependências da documentação
└── requirements.txt               # Dependências do projeto
```

O modelo em tempo de execução é carregado localmente de 
`./mlartifacts/*/models/*/artifacts/model.ubj` (versão mais recente), 
já os arquivos em `app/models/` definem as features e o tipo de tarefa para a API.
