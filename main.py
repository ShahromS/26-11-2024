from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    html = """
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    color: #333;
                    margin-top: 50px;
                }
                form {
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    display: inline-block;
                    padding: 20px;
                    margin-top: 20px;
                }
                input[type="text"] {
                    width: 200px;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    background-color: #007BFF;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <h1>ようこそ!</h1>
            <form action="/hello" method="GET">
                <label for="name">名前:</label><br>
                <input type="text" name="name" id="name" placeholder="名前を入力してください"><br>
                <label for="c">コメント:</label><br>
                <input type="text" name="c" id="c" placeholder="コメントを入力してください"><br>
                <input type="submit" value="送信">
            </form>
        </body>
        </html>
    """
    return html

@app.route('/hello')
def hello():
    name = request.args.get('name')
    c = request.args.get('c')

    if not name:
        name = '名無し'  
    if not c:
        c = 'メッセージ無し'  

    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                text-align: center;
                margin: 0;
                padding: 0;
            }}
            h1 {{
                color: #333;
                margin-top: 50px;
            }}
            h2 {{
                color: #666;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #007BFF;
                padding: 10px 20px;
                border: 1px solid #007BFF;
                border-radius: 5px;
                transition: background-color 0.3s, color 0.3s;
            }}
            a:hover {{
                background-color: #007BFF;
                color: white;
            }}
        </style>
    </head>
    <body>
        <h1>{name}さん、こんにちは！</h1>
        <h2>{c}</h2>
        <a href="/">戻る</a>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')
