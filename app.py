from flask import Flask


app = Flask(__name__) # E305エラー対策: クラス定義後に2行の空白行

@app.route('/')
def hello():
    return "Hello, DevOps World! This app is running inside a Docker container."


if __name__ == '__main__': # E302エラー対策: 関数定義の前に2行の空白行
    # 開発環境で動作確認するための設定
    app.run(host='0.0.0.0', port=5000)

# W292エラー対策: ファイルの最後に空行（改行）を追加