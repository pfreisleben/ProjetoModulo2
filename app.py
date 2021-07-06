from flask import Flask, render_template, request  # Importaçao dos módulos
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# Configurações do banco de dados
user = 'dwxnfeeu'  # Usuário do banco
database = 'dwxnfeeu'  # Nome do banco
host = 'tuffi.db.elephantsql.com'  # Host do banco
password = 'EYsro5jAqVKp9hnoUgX_G8Tw3IjMd9Jo'  # Senha do banco

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "chaveOK"

# Cria o objeto SQL Alchemy, passando o app como parametro e vinculando a variavel db.
db = SQLAlchemy(app)

# Primeiras informações que vão aparecer no front(index)
# Id, Nome, Tipo, Nivel de Desafio e Imagem.


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

    def __init__(self, nome, tipo, niveldesafio, descricaoGeral, ca, pv, deslocamento, forca,
                 destreza, constituicao, inteligencia, sabedoria, carisma):
        self.nome = nome
        self.tipo = tipo
        self.niveldesafio = niveldesafio
        self.descricaogeral = descricaoGeral
        self.ca = ca
        self.pv = pv
        self.deslocamento = deslocamento
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    @staticmethod
    def read_all():
        return Bestas.query.order_by(Bestas.id.asc()).all()

    @staticmethod
    def read_single(id_registro):
        return Bestas.query.get(id_registro)

    @staticmethod
    def conta():
        return Bestas.query.count()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, novo_nome, novo_tipo, novo_nivelDesafio, novo_descricaoGeral, novo_ca, novo_pv,
               novo_deslocamento, novo_forca, novo_destreza, novo_constituicao, novo_inteligencia,
               novo_sabedoria, novo_carisma):
        self.nome = novo_nome
        self.tipo = novo_tipo
        self.niveldesafio = novo_nivelDesafio
        self.descricaoGeral = novo_descricaoGeral
        self.ca = novo_ca
        self.pv = novo_pv
        self.deslocamento = novo_deslocamento
        self.forca = novo_forca
        self.destreza = novo_destreza
        self.constituicao = novo_constituicao
        self.inteligencia = novo_inteligencia
        self.saedoria = novo_sabedoria
        self.carisma = novo_carisma

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
        registro = Bestas(form['nome'], form['imagem_url'], form['niveldesafio'], form['descricaogeral'], form['ca'], form['pv'],
                          form['deslocamento'], form['forca'], form['destreza'], form['constituicao'],
                          form['inteligencia'], form['sabedoria'], form['carisma'])
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
                        form['inteligencia'], form['sabedoria'], form['carisma'])

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
