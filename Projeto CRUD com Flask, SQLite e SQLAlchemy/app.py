from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'exemplo.db')
db = SQLAlchemy(app)

print(base_dir)

class Energetico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    tamanho_lata = db.Column(db.Integer)  # Make sure this line is present
    sabor = db.Column(db.Text)
    marca = db.Column(db.Text)
    preco = db.Column(db.Float)



    def __init__(self, nome, tamanho_lata, sabor, marca, preco):
        self.nome = nome
        self.tamanho_lata = tamanho_lata
        self.sabor = sabor
        self.marca = marca
        self.preco = preco

    def __repr__(self):
        return f'{self.marca}: {self.nome} - {self.sabor} ({self.tamanho_lata}ml)\n{self.preco}'



@app.route('/')
def index():
    db.create_all()
    energeticos = Energetico.query.all()
    return render_template('index.html', energeticos = energeticos)


@app.route('/inserir', methods=['POST'])
def insert():
    nome = request.form['nome']
    tamanho_lata = request.form['tamanho_lata']
    sabor = request.form['sabor']
    marca = request.form['marca']
    preco = request.form['preco']

    energetico = Energetico(nome, tamanho_lata, sabor, marca, preco)
    db.session.add(energetico)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def delete(id):
    energetico = Energetico.query.get(id)
    db.session.delete(energetico)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/atualizar/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        novo_sabor = request.form['novo_sabor']
        energetico  = Energetico.query.get(id)
        energetico.sabor = novo_sabor
        db.session.commit()
        return redirect(url_for('index'))
    else:
        energetico = Energetico.query.get(id)
        return render_template('atualiza.html', energetico = energetico)
    
@app.route('/listar', methods=['POST'])
def list():
    nome = request.form['nome']
    energeticos = Energetico.query.filter(Energetico.nome.like(f'%{nome}%')).all()
    return render_template("lista.html", energeticos = energeticos)

if __name__ == '__main__':
    app.run(debug = True)