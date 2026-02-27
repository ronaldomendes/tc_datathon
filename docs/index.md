## Arquitetura do Projeto

```
tc_datathon/
├── app/                        # API e lógica de aplicação
│   ├── __init__.py
│   ├── routes.py               # Definição dos endpoints (ex.: /predict)
│   ├── main.py                 # Inicialização da API (Flask/FastAPI)
│   └── model/                  # Modelos e carregamento
│       ├── __init__.py
│       ├── load_model.py       # Função para carregar modelo salvo
│       └── predict.py          # Função para gerar previsões
├── notebooks/                  # Exploração e prototipagem
│   ├── test.ipynb
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
├── Dockerfile                  # Containerização da API
├── docker-compose.yml          # Orquestração local
└── requirements.txt            # Dependências do projeto
```
