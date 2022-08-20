import os

from flask import Flask, abort, Response, request


from utils import make_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

@app.route("/perform_query")
def perform_query() -> Response:
    # получаем параметры
    cmd1 = request.args.get('cmd1')
    cmd2 = request.args.get('cmd2')
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    file_name = request.args.get('file_name')

    # проверяем наличие
    if not cmd1 and value1 and file_name:
        abort(400)
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400)

    # работаем с файлом, вызываем необходимые функции
    with open(file_path) as necessary_file:
        result = make_query(cmd1, value1, necessary_file)
        if cmd2 and value2:
            result = make_query(cmd2, value2, result)
        result = "\n".join(result)

    return app.response_class(result, content_type="text/plain")


if __name__ == "__main__":
    app.run()
