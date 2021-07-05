from flask import Flask, render_template, request
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
