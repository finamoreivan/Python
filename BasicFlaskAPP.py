from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hola, esto es una prueba de Flask app</h1>"""

if __name__ == '__main__':
    app.run(debug=True)