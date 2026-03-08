# Datathon Passos Mágicos

## Como executar o projeto
- Para executar o MLFlow: ``mlflow ui``
- Para executar o Front-end: ``uvicorn app.main:app --reload``

---

## Arquitetura do Projeto

```
tc_datathon/
├── app/                        # API e lógica de aplicação
│   ├── __init__.py
│   ├── main.py                 # Inicialização da API (Flask/FastAPI) e interface Gradio
│   ├── routes.py               # Definição dos endpoints (ex.: /predict)
│   ├── run_pipeline.py         # Executa treinamento do modelo e salvamento no MLFlow
│   └── model/                  # Modelos e carregamento
│   │   ├── __init__.py
│   │   ├── load_model.py       # Função para carregar modelo salvo
│   │   └── predict.py          # Função para gerar previsões
│   └── models/                 # Dependências locais do modelo XGBoost
│       ├── feature_names.json  # Features utilizadas para o treinamento do modelo
│       ├── model.json          # Último modelo em formato json
│       └── task.json           # Configuração do último modelo executado
├── notebooks/                  # Exploração e prototipagem
│   ├── test.ipynb              # Notebooks com testes do modelo
│   └── eda.ipynb               # Análise exploratória dos dados
├── src/                        # Pipeline de ML
│   ├── __init__.py
│   ├── evaluate.py             # Funções de avaliação (AUC, F1, etc.)
│   ├── feature_engineering.py  # Criação de atributos derivados
│   ├── middleware.py           # Intermediários (ex.: validação de input)
│   ├── preprocessing.py        # Limpeza e transformação dos dados
│   ├── train.py                # Treinamento e salvamento do modelo
│   └── utils.py                # Funções auxiliares (logs, configs)
├── tests/                      # Testes unitários
│   ├── __init__.py
│   ├── test_model.py           # Testes de inferência e performance
│   └── test_preprocessing.py   # Testes de limpeza e transformação
├── docker-compose.yml          # Orquestração local
├── Dockerfile                  # Containerização da API
├── mkdocs.yml                  # Arquivo de configuração MkDocs
├── mkdocs-requirements.txt     # Dependências da documentação MkDocs
└── requirements.txt            # Dependências do projeto
```
