from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/chau")
def bye_world():
    return "<p>Bye, World!</p>"

@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"Hola {nombre}"

@app.route("/nomape/<nombre>/<apellido>")
def nomape(nombre, apellido):
    return f"Hola {nombre} {apellido}"

app.run()