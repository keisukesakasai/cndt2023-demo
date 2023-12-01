### NODE-APP
Node.js で立てたサーバーの自動計装を試すアプリ

### Usage
- 構築
```sh
npm install --save @opentelemetry/api
npm install --save @opentelemetry/auto-instrumentations-node
npm install --save @opentelemetry/instrumentation-grpc
```

- 実行
```sh
export OTEL_TRACES_EXPORTER="otlp"
export OTEL_METRICS_EXPORTER="otlp"
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
# export OTEL_NODE_RESOURCE_DETECTORS="env,host,os,process"
export OTEL_NODE_RESOURCE_DETECTORS="env,host,os"
export OTEL_SERVICE_NAME="Node-App"
export NODE_OPTIONS="--require @opentelemetry/auto-instrumentations-node/register"
node app.js
```

NODE_OPTIONS で `opentelemetry/auto-instrumentations-node` を読み込むことで、Node.js が提供する計装ライブラリに該当するフレームワークを使っていた場合自動計装される。
リポジトリ：https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node
フレームワーク：https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node#supported-instrumentations

コードの中で、`opentelemetry/auto-instrumentations-node` で必要なライブラリをロードする方法もある。(Python の Programable Instrumentation と同じ感じ)

特定の自動軽装を OFF にするみたいな方法とか、カスタムスパンの付与はコードで書くから、一長一短な感じ。

```sh
$ node --require ./instrumentation.js app_with_instrumented.js
```