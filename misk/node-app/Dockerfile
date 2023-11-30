# ベースイメージとしてNode.jsのオフィシャルイメージを使用
FROM node:16

# アプリケーションのソースコードを含むディレクトリを作成
WORKDIR /usr/src/app
# WORKDIR /autoinstrumentation

# アプリケーションの依存関係ファイルをコピー
# package.json と package-lock.json (存在する場合) をコピー
COPY package*.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションがリッスンするポートを指定
EXPOSE 3000

# アプリケーションの起動コマンドを定義
CMD [ "node", "nodejs_server.js" ]