from flask import Flask,render_template,request,url_for,redirect,flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simbolos")
def simbolos():
    return render_template("simbolos.html")

@app.route("/academico")
def academico():
    return render_template("academico.html")

@app.route("/comunidad")
def comunidad():
    return render_template("comunidad.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)