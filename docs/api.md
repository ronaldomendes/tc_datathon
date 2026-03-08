# Documentação da API

A API expõe:

- **POST /predict** – previsão (um registro ou lote).
- **GET /health** – health check.
- **GET /metrics** – contagem de requisições, erros e tempos de resposta.

A interface Gradio em **/ui** permite prever a partir dos indicadores (IPV, IPS, IAA, IEG, Nº AV, IDA) sem chamar a API manualmente.

Documentação interativa: 
 
- Swagger: **/documentation/swagger**
- Redoc: **/documentation/redoc**

---

# Exemplos de chamadas à API

## Health e métricas

```bash
curl -s http://localhost:8000/health
curl -s http://localhost:8000/metrics
```

## Previsão – um registro (objeto com features)

Entrada esperada: campos numéricos compatíveis com as features do modelo (ex.: `ipv`, `ips`, `iaa`, `ieg`, `n_av` ou `nº_av`, `ida`). A API normaliza nomes de colunas conforme `feature_names.json`.

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d "{\"ipv\": 0.5, \"ips\": 0.6, \"iaa\": 0.4, \"ieg\": 0.7, \"n_av\": 2, \"ida\": 0.5}"
```
> De forma mais intuitiva, também é possível acessar através do browser a interface gráfica em [http://localhost:8000/predict](http://localhost:8000/predict), preencher o formulário com os dados acima e iniciar a predição do modelo.

Exemplo de resposta:

```json
{
  "predictions": [0],
  "message": "ok"
}
```

## Previsão – lote

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d "{\"data\": [{\"ipv\": 0.5, \"ips\": 0.6, \"iaa\": 0.4, \"ieg\": 0.7, \"n_av\": 2, \"ida\": 0.5}, {\"ipv\": 0.3, \"ips\": 0.4, \"iaa\": 0.5, \"ieg\": 0.6, \"n_av\": 1, \"ida\": 0.4}]}"
```

Resposta:

```json
{
  "predictions": [0, 1],
  "message": "ok"
}
```

Se o modelo não estiver carregado ou houver erro, a resposta inclui `"predictions": []` e uma `"message"` explicativa.