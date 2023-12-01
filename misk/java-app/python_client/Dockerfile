# Pythonのベースイメージを使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

ENV OTEL_SERVICE_NAME=PYTHON_CLIENT_AUTO_INST
ENV OTEL_TRACES_EXPORTER=otlp
ENV OTEL_EXPORTER_OTLP_PROTOCOL=grpc
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Flaskアプリケーションを実行
CMD ["opentelemetry-instrument", "python", "app.py"]