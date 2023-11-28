### 概要
MySQL Instrumentor 潜るための Misk Project

### メモ
- execute
```sh
pip install opentelemetry-distro==0.41b0
opentelemetry-bootstrap -a install
pip install opentelemetry-sdk==v1.20.0

pip install 'flask<3'
pip install mysql-connector-python
# distribution 追加したら、instrumentor も追加する
opentelemetry-bootstrap -a install

opentelemetry-instrument python app.py
```

- env
```sh
deepdive-instrumentor ❯ env | grep OTEL                  
OTEL_TRACE_EXPORTER=console
OTEL_SERVICE_NAME=deepdive
OTEL_METRICS_EXPORTER=console
OTEL_TRACES_EXPORTER=console
```

- sample
```sh
deepdive-instrumentor ❯ opentelemetry-instrument python app.py
 * Serving Flask app 'app'
 * Debug mode: off
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://10.87.21.162:8080
INFO:werkzeug:Press CTRL+C to quit
INFO:__main__:DB からデータ取得: 1434000
INFO:__main__:result = 1434000
INFO:werkzeug:127.0.0.1 - - [28/Nov/2023 15:02:20] "GET / HTTP/1.1" 200 -
{
    "name": "SELECT",
    "context": {
        "trace_id": "0xc4fd2995df357cfed2cfe63178ac5458",
        "span_id": "0xcde5a93ad9ec42f3",
        "trace_state": "[]"
    },
    "kind": "SpanKind.CLIENT",
    "parent_id": "0x5ca71a094e722623",
    "start_time": "2023-11-28T06:02:20.246340Z",
    "end_time": "2023-11-28T06:02:20.248607Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "db.system": "mysql",
        "db.name": "western",
        "db.statement": "SELECT population FROM population WHERE prefecture = %s",
        "db.user": "western",
        "net.peer.name": "127.0.0.1",
        "net.peer.port": 3307
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.20.0",
            "service.name": "deepdive",
            "telemetry.auto.version": "0.41b0"
        },
        "schema_url": ""
    }
}
{
    "name": "/",
    "context": {
        "trace_id": "0xc4fd2995df357cfed2cfe63178ac5458",
        "span_id": "0x5ca71a094e722623",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2023-11-28T06:02:20.161727Z",
    "end_time": "2023-11-28T06:02:20.249671Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.method": "GET",
        "http.server_name": "0.0.0.0",
        "http.scheme": "http",
        "net.host.port": 8080,
        "http.host": "localhost:8080",
        "http.target": "/",
        "net.peer.ip": "127.0.0.1",
        "http.user_agent": "curl/8.1.2",
        "net.peer.port": 61780,
        "http.flavor": "1.1",
        "http.route": "/",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.20.0",
            "service.name": "deepdive",
            "telemetry.auto.version": "0.41b0"
        },
        "schema_url": ""
    }
}
```