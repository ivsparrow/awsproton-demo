from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <head>
            <title>AWS Proton Demo from Prod</title>
            <style>
                body {
                    background-color: #f0f8ff;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 100px;
                    color: #333;
                }
                h1 {
                    font-size: 2.5em;
                }
            </style>
        </head>
        <body>
            <h1>Hello from AWS App Runner!</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
