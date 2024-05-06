
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/filmes")
def filmes():
    return render_template('filmes.html')

@app.route("/diretores")
def diretores():
    return render_template('diretores.html')

@app.route("/morangos")
def morangos():
    return render_template('morango.html')

@app.route("/homens")
def homens():
    return render_template('homens.html')

@app.route("/liquidificador")
def liquitificador():
    return render_template('liquitificador.html')

@app.route("/gritos")
def gritos():
    return render_template('gritos.html')

@app.route("/midsommar")
def midsommar():
    return render_template('midsommar.html')

@app.route("/persona")
def persona():
    return render_template('persona.html')

@app.route("/pulp")
def pulp():
    return render_template('pulp.html')

@app.route("/brilho")
def brilho():
    return render_template('brilho.html')

@app.route("/passaro")
def passaro():
    return render_template('passaro.html')

@app.route("/dracula")
def dracula():
    return render_template('dracula.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)