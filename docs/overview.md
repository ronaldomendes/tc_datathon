### Objetivo

O projeto aborda o problema de **previsão do risco de defasagem escolar** dos estudantes, 
com base nos dados da pesquisa PEDE (Passos Mágicos). O modelo preditivo permite identificar 
alunos em situação de vulnerabilidade para apoio educacional e psicopedagógico.

### Solução proposta

Foi construída uma pipeline completa de Machine Learning que inclui:

- **Pré-processamento** dos dados PEDE (Excel), seleção de colunas e normalização de nomes.
- **Engenharia de atributos** (módulo preparado para features derivadas).
- **Treinamento** com XGBoost (classificação ou regressão conforme o target), com validação e métricas.
- **Registro no MLflow** para experimentos, métricas e artefatos.
- **API REST** (FastAPI) com endpoint `/predict` e interface Gradio em `/ui`.
- **Monitoramento** via logs estruturados (JSON) e endpoints `/health` e `/metrics`.

### Stack tecnológica

| Componente        | Tecnologia                          |
|-------------------|-------------------------------------|
| Linguagem         | Python 3.11                         |
| ML                | XGBoost, scikit-learn, pandas, numpy|
| API               | FastAPI                             |
| Interface extra   | Gradio (predição em `/ui`)          |
| Serialização      | Formato nativo XGBoost (JSON/UBJ)   |
| Experimentos      | MLflow                              |
| Testes            | pytest                              |
| Empacotamento     | Docker / docker-compose             |
| Documentação      | MkDocs (Material)                   |
