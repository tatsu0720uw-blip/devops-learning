# ベースイメージの指定: Python 3.9 のスリム版 (軽量OS) を使用
FROM python:3.9-slim

# 環境変数 (設定) の定義: Pythonが標準出力にログを出すように設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係ファイルをコピーし、インストール
# このステップは頻繁に変更されないため、キャッシュを効率的に使うため先に行う
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーション本体をコピー
COPY . .

# コンテナがリッスンするポートを指定
EXPOSE 5000

# コンテナ起動時に実行するコマンド
CMD ["python", "app.py"]