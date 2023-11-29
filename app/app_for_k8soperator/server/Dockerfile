# Pythonのベースイメージを使用
FROM --platform=linux/amd64 python:3.11 

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なライブラリをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# Flaskアプリケーションを実行
CMD ["python", "app.py"]