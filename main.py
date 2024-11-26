from flask import Flask, request

app = Flask(__name__)

# Главная страница с формой
@app.route('/')
def index():
    # Возвращаем HTML с формой
    html = """
        <html>
        <body>
            <form action="/hello" method="GET">
                名前: <input type="text" name="name">
                <br>
                コメント: <input type="text" name="c">
                <br>
                <input type="submit" value="送信">
            </form>
        </body>
        </html>
    """
    return html

# Обработка страницы /hello
@app.route('/hello')
def hello():
    # Получаем параметры name и c из запроса
    name = request.args.get('name')
    c = request.args.get('c')

    # Устанавливаем значения по умолчанию, если параметры не переданы
    if not name:
        name = '名無し'  # Имя не указано
    if not c:
        c = 'メッセージ無し'  # Сообщение не указано

    # Возвращаем HTML с приветствием
    return f"""
    <html>
    <body>
        <h1>{name}さん、こんにちは！</h1>
        <h2>{c}</h2>
        <a href="/">戻る</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0')
