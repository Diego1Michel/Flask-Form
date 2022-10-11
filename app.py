# py -m venv flask-form 
# .\Flask-Form\Scripts\activate

from flask import Flask, request, render_template, redirect, url_for
from db import add_text, get_data
app = Flask(__name__)

@app.route("/")
def index():
    all_text = get_data()
    return render_template('index.html', all_text = all_text)

@app.route("/add_text", methods=["GET", "POST"])
def AddText():
    if request.method == "POST":
        name = request.form["textv"]
        email = request.form["textv"]
        cidade = request.form["textv"]
        endereco = request.form["textv"]
        telefone = request.form["textv"]
        cpf = request.form["textv"]
        data_nascimento = request.form["textv"]
        add_new = add_text(name, email, cidade, endereco, telefone, cpf, data_nascimento)
        return redirect(url_for('index'))

    else:
        return render_template('index.html' )
