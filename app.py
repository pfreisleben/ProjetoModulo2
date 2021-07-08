# Integrantes: Pedro Freisleben, Wagner Cardoso Rodrigues, Filipe Mascarenhas Paiva
# A ideia era montar um bestiário com monstros do jogo de RPG Dungeons & Dragons
# No desenvolvimento, começamos a modelar primeiro o banco de dados, criando as tabelas
# definindo os campos dos elementos, depois estruturamos o back-end, os endpoints e
# modelagem do banco no SQLAlchemy, e por fim fizalizamos pelo Front-End.
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

user = 'dwxnfeeu'
database = 'dwxnfeeu'
host = 'tuffi.db.elephantsql.com'
password = 'EYsro5jAqVKp9hnoUgX_G8Tw3IjMd9Jo'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "chaveOK"


db = SQLAlchemy(app)


class Bestas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(255), nullable=False)
    niveldesafio = db.Column(db.Integer, nullable=False)
    descricaogeral = db.Column(db.String(1000), nullable=False)
    ca = db.Column(db.Integer, nullable=False)
    pv = db.Column(db.Integer, nullable=False)
    deslocamento = db.Column(db.Integer, nullable=False)
    forca = db.Column(db.Integer, nullable=False)
    destreza = db.Column(db.Integer, nullable=False)
    constituicao = db.Column(db.Integer, nullable=False)
    inteligencia = db.Column(db.Integer, nullable=False)
    sabedoria = db.Column(db.Integer, nullable=False)
    carisma = db.Column(db.Integer, nullable=False)
    imagem_url = db.Column(db.String(255), nullable=True)
    nomesimplificado = db.Column(db.String(255), nullable=True)

    def __init__(self, nome, tipo, niveldesafio, descricaogeral, ca, pv, deslocamento, forca,
                 destreza, constituicao, inteligencia, sabedoria, carisma, imagem_url, nomesimplificado):
        self.nome = nome
        self.tipo = tipo
        self.niveldesafio = niveldesafio
        self.descricaogeral = descricaogeral
        self.ca = ca
        self.pv = pv
        self.deslocamento = deslocamento
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.imagem_url = imagem_url
        self.nomesimplificado = nomesimplificado

    @ staticmethod
    def read_all():
        return Bestas.query.order_by(Bestas.id.asc()).all()

    @ staticmethod
    def read_single(id_registro):
        return Bestas.query.get(id_registro)

    @ staticmethod
    def conta():
        return Bestas.query.count()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, novo_nome, novo_tipo, novo_nivelDesafio, novo_descricaoGeral, novo_ca, novo_pv,
               novo_deslocamento, novo_forca, novo_destreza, novo_constituicao, novo_inteligencia,
               novo_sabedoria, novo_carisma, novo_imagem_url, novo_nomesimplificado):
        self.nome = novo_nome
        self.tipo = novo_tipo
        self.niveldesafio = novo_nivelDesafio
        self.descricaogeral = novo_descricaoGeral
        self.ca = novo_ca
        self.pv = novo_pv
        self.deslocamento = novo_deslocamento
        self.forca = novo_forca
        self.destreza = novo_destreza
        self.constituicao = novo_constituicao
        self.inteligencia = novo_inteligencia
        self.saedoria = novo_sabedoria
        self.carisma = novo_carisma
        self.imagem_url = novo_imagem_url
        self.nomesimplificado = novo_nomesimplificado

        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


@app.route('/')
def index():
    total = Bestas.conta()
    return render_template('index.html', total=total)


@app.route("/read")
def read_all():
    registros = Bestas.read_all()
    return render_template("read_all.html", registros=registros)


@app.route("/read/<id_registro>")
def read_id(id_registro):
    registro = Bestas.read_single(id_registro)
    return render_template("read_single.html", registro=registro)


@app.route("/create", methods=('GET', 'POST'))
def create():
    novo_id = None

    if request.method == 'POST':

        form = request.form
        registro = Bestas(form['nome'], form['tipo'], form['niveldesafio'], form['descricaogeral'], form['ca'], form['pv'],
                          form['deslocamento'], form['forca'], form['destreza'], form['constituicao'],
                          form['inteligencia'], form['sabedoria'], form['carisma'], form['imagem_url'], form['nomesimplificado'])
        registro.save()
        novo_id = registro.id

    return render_template("create.html", novo_id=novo_id)


@app.route('/update/<id_registro>', methods=('GET', 'POST'))
def update(id_registro):
    sucesso = False

    registro = Bestas.read_single(id_registro)

    if request.method == 'POST':
        form = request.form

        registro.update(form['nome'], form['tipo'],
                        form['niveldesafio'], form['descricaogeral'], form['ca'], form['pv'],
                        form['deslocamento'], form['forca'], form['destreza'], form['constituicao'],
                        form['inteligencia'], form['sabedoria'], form['carisma'], form['imagem_url'],
                        form['nomesimplificado'])

        sucesso = True

    return render_template('update.html', registro=registro, sucesso=sucesso)


@app.route('/delete/<id_registro>')
def delete(id_registro):
    registro = Bestas.read_single(id_registro)
    return render_template("delete.html", registro=registro)


@app.route('/delete/<id_registro>/confirmed')
def delete_confirmed(id_registro):
    sucesso = False

    registro = Bestas.read_single(id_registro)

    if registro:
        registro.delete()
        sucesso = True

    return render_template("delete.html", registro=registro, sucesso=sucesso)


if __name__ == '__main__':
    app.run(debug=True)
