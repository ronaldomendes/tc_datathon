# Como executar o projeto

## Ambiente local

1. **MLflow** (opcional, para ver experimentos e artefatos):
   ```bash
   mlflow ui
   ```
   Rota padrão: `http://localhost:5000`.

2. **API (FastAPI + Gradio)**:
   ```bash
   uvicorn app.main:app --reload
   ```
   - API: `http://localhost:8000`
   - Documentação Swagger: `http://localhost:8000/documentation/swagger`
   - ReDoc: `http://localhost:8000/documentation/redoc`
   - Interface Gradio: `http://localhost:8000/ui`

## Docker

```bash
docker compose up --build
```

O serviço sobe na porta **8000**, com volume somente leitura `./mlartifacts:/app/mlartifacts` para usar os modelos registrados no MLflow. Healthcheck usa `GET /documentation/redoc`.

---

# Deploy e pré-requisitos

## Pré-requisitos

- **Python**: 3.11 (recomendado).
- **Dados**: planilha PEDE no caminho esperado (ex.: `files/BASE DE DADOS PEDE 2024 - DATATHON.xlsx`), conforme `src.utils.get_data_path()`.

## Instalação de dependências

```bash
pip install -r requirements.txt
```

No Docker, o `Dockerfile` ignora `pywin32` do `requirements.txt` para compatibilidade Linux.

## Comandos principais

| Ação            | Comando |
|-----------------|--------|
| Treinar modelo  | `python -m app.run_pipeline` (usa `src.train` com MLflow em `localhost:5000` por padrão) |
| Argumentos      | `--save_path`, `--mlflow_tracking_uri`, `--experiment_name`, `--test_size`, `--random_state` |
| Rodar API       | `uvicorn app.main:app --host 0.0.0.0 --port 8000` |
| Testes          | `pytest tests/` |

> Obs.: não é necessário instalar as dependências do arquivo mkdocs-requirements.txt, pois apenas são necessárias para o deploy desta documentação.
