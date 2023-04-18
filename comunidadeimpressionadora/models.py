from comunidadeimpressionadora import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    post = database.relationship('Post',backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não informado')

class Post(database.Model):
    id= database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    #foreignKey será o nome da classe(em minusculo) mais o id ( que foi escrito na classe
    id_usuario = database.Column(database.Integer,database.ForeignKey('usuario.id'), nullable=False)

    """
    CONSOLE
from models import Usuario, Post
from main import app
app.app_context().push()
database.create_all()
usuario = Usuario(username='João',email='joao@gmail.com',senha='123456')
database.session.add(usuario)
database.session.commit()
Usuario.query.all()
[<Usuario 1>]
usuario.query.first()
<Usuario 1>
usuario_teste = usuario.query.first()
usuario_teste.email
'joao@gmail.com'
"""