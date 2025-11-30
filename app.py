from flask import Flask


app = Flask(__name__)  # インラインコメントの前にスペースを2つ


@app.route('/') # 関数定義の前に2行の空白行
def hello():
    return "Hello, DevOps World! This app is running inside a Docker container."


if __name__ == '__main__': # インラインコメントの前にスペースを2つ
    # 開発環境で動作確認するための設定
    app.run(host='0.0.0.0', port=5000)
# (ファイルの最後に必ず空行（改行）を1つ入れる)