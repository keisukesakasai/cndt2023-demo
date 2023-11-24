## What's Is This Repository ??
Demo Shi⚪︎ty App for Cloud Native Days Tokyo 2023.

<img src="img/demo-app.png" width=auto height="300">

## App

### CNDT_ROUTER
- Setup
```sh
pip install opentelemetry-distro==0.41b0
opentelemetry-bootstrap -a install
pip install opentelemetry-sdk==v1.20.0
pip install opentelemetry-exporter-otlp==v1.20.0
```

- Environment variable
```sh
export CNDT_ROUTER_HOST="0.0.0.0"
export CNDT_ROUTER_PORT=8080
export CNDT_ROUTER_REDIS_HOST="localhost"
export CNDT_ROUTER_REDIS_port=6379
export CNDT_ROUTER_CACHE_EXPIRE_TIME=5
export CNDT_ROUTER_DATABASE_URL="postgresql://postgres:password@localhost/postgres"
export CNDT_ROUTER_EASTERN_API_URL="http://localhost:8089/call_eastern_api"
export CNDT_ROUTER_WESTERN_API_URL="http://localhost:8090/call_western_api"
```

- Usage
```sh
export OTEL_SERVICE_NAME=CNDT-ROUTER
export OTEL_TRACES_EXPORTER=otlp
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

opentelemetry-instrument python app.py
```

### CNDT_EASTERN_API
- Setup
```sh

```

- Environment variable
```sh
export CNDT_EASTERN_API_HOST="0.0.0.0"
export CNDT_EASTERN_API_PORT=8089
export CNDT_EASTERN_API_MEMCACHE_HOST="localhost"
export CNDT_EASTERN_API_MEMCACHE_PORT=11211
export CNDT_EASTERN_API_MEMCACHE_EXPIRE_TIME=60
export CNDT_EASTERN_API_DB_USER='eastern'
export CNDT_EASTERN_API_DB_PASSWOR='password'
export CNDT_EASTERN_API_DB_HOST='127.0.0.1'
export CNDT_EASTERN_API_DB_NAME='eastern'
export CNDT_EASTERN_API_DB_PORT=3306
```

### CNDT_WESTERN_API

- Environment variable
```sh
export CNDT_WESTERN_API_HOST="0.0.0.0"
export CNDT_WESTERN_API_PORT=8090
export CNDT_WESTERN_API_MEMCACHE_HOST="localhost"
export CNDT_WESTERN_API_MEMCACHE_PORT=11211
export CNDT_WESTERN_API_MEMCACHE_EXPIRE_TIME=60
export CNDT_WESTERN_API_DB_USER='western'
export CNDT_WESTERN_API_DB_PASSWOR='password'
export CNDT_WESTERN_API_DB_HOST='127.0.0.1'
export CNDT_WESTERN_API_DB_NAME='western'
export CNDT_WESTERN_API_DB_PORT=3307
```