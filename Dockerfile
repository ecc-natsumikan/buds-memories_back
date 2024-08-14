# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# ポート5000を公開（バックエンドのポートに合わせてください）
EXPOSE 5000

# バックエンドアプリケーションを起動
CMD ["python", "main.py"]
