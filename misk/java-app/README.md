- Setup
```sh
```

- Execute：Java のサーバー
```sh
export JAVA_TOOL_OPTIONS="-javaagent:./opentelemetry-javaagent.jar"
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=logging
export OTEL_LOGS_EXPORTER=logging
export OTEL_SERVICE_NAME=CNDT2023-DEMO-JavaApp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

java -jar ./app/build/libs/app.jar
```

- Execute：Python のクライアント
```sh

```