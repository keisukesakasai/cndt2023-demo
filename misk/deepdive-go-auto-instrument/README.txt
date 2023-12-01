### セットアップ
以下を docker-compose で立ち上げる
- Python クライアント（opentelemetry-isntrument を使った自動計装）
- Go サーバー（opentelemetry-go-instrumentation を使った自動計装）
- Jaeger

### 環境構築
```sh
# python
pip install opentelemetry-distro==0.41b0
opentelemetry-bootstrap -a install
pip install opentelemetry-sdk==v1.20.0
pip install opentelemetry-exporter-otlp==v1.20.0
pip install opentelemetry-exporter-otlp-proto-grpc # bootstrap で入れてくれ...

pip freeze >| requirements.txt
```