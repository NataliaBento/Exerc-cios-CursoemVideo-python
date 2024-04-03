from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import pytz
import json
import secrets

db = SQLAlchemy()
     
class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setor = db.Column(db.String(50), nullable=False)
    
    def __init__(self, setor):
        self.setor = setor
    
    def to_dict(self):
        return {
            'id': self.id,
            'setor': self.setor,
        }
    
class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sala = db.Column(db.String(50), unique=True, nullable=False)
    tipo = db.Column(db.Integer, default=0, nullable=False) # 0 - Sala normal, 1 - Sala Rápida
    
    def __init__(self, sala, tipo):
        self.sala = sala
        self.tipo = tipo
    
    def to_dict(self):
        return {
            'id': self.id,
            'sala': self.sala,
            'tipo': self.tipo,
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    nivel_acesso = db.Column(db.String(10), nullable=False)
    id_setor = db.Column(db.Integer, db.ForeignKey(Setor.__tablename__ + '.id'), nullable=False)
    
    setor = db.relationship('Setor', backref='user', foreign_keys=[id_setor])
    
    def __init__(self, username, email, password, nivel_acesso, setor):
        self.username = username
        self.email = email
        self.set_password(password)
        self.nivel_acesso = nivel_acesso
        self.id_setor = setor
        
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'nivel_acesso': self.nivel_acesso,
            'setor': [self.setor.id, self.setor.setor],
        }
        
class LogUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(User.__tablename__ + '.id'), nullable=False)
    acesso = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    usuario = db.relationship('User', backref='log', foreign_keys=[id_usuario])
    
    def __init__(self, id_usuario):
        tz_recife = pytz.timezone('America/Recife')
        
        self.id_usuario = id_usuario
        self.acesso =  datetime.now(tz_recife)
        
    def to_dict(self):
        return {
            'id_log': self.id,
            'usuario': {
                'id': self.usuario.id,
                'username': self.usuario.username,
                'setor': self.usuario.setor.setor,
            },
            'acesso': self.acesso,
        }
        
class Agenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_sala = db.Column(db.Integer, db.ForeignKey(Sala.__tablename__ + '.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey(User.__tablename__ + '.id'), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)
    data = db.Column(db.Date, nullable=False)
    dt_cadastro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    sala = db.relationship('Sala', backref='agenda', foreign_keys=[id_sala])
    usuario = db.relationship('User', backref='agenda', foreign_keys=[id_usuario])
    
    
    def __init__ (self, id_sala, id_usuario, hora_inicio, hora_fim, data):
        tz_recife = pytz.timezone('America/Recife')
        
        self.id_sala = id_sala
        self.id_usuario = id_usuario
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.data = data
        self.dt_cadastro = datetime.now(tz_recife)    

    def to_dict(self):
        return {
            'id': self.id,
            'sala': {self.sala.id, self.sala.sala, self.sala.tipo},
            'usuario': {
                'id':self.usuario.id, 
                'username':self.usuario.username,
                'setor': self.usuario.setor.setor,
            },
            'inicio': self.hora_inicio,
            'fim': self.hora_fim,
            'data': self.data,
            'cadastro': self.dt_cadastro,
        }
    
    @staticmethod
    def gerar_slots(id_sala, data, hora_inicio, hora_fim, intervalo_minutos):
        tz_recife = pytz.timezone('America/Recife')
        formato_hora = "%H:%M:%S"
        tempo_slot = timedelta(minutes=intervalo_minutos)

        # Convertendo as strings de hora e data para objetos datetime
        data_inicio = datetime.strptime(f"{data} {hora_inicio}", "%Y-%m-%d %H:%M:%S")
        data_fim = datetime.strptime(f"{data} {hora_fim}", "%Y-%m-%d %H:%M:%S")

        # Obtendo a data e hora atual
        data_atual = datetime.now(tz_recife)

        # Inicializando a lista de slots
        slots = []

        # Definindo a hora de início com base na condição
        hora_inicio_slot = max(data_inicio.time(), data_atual.time()) if data == str(data_atual.date()) else data_inicio.time()

        # Criando os slots de acordo com a agenda existente
        atual = datetime.combine(data_inicio.date(), hora_inicio_slot)
        
        while atual < data_fim:
            disponibilidade = "Disponivel"
            ocupante = None

            # Verificando se o slot está ocupado na agenda
            ocupacao = Agenda.query.filter(
                Agenda.hora_inicio <= atual.time(),
                Agenda.hora_fim > atual.time(),
                Agenda.data == atual.date(),
                Agenda.id_sala == id_sala
            ).first()

            if ocupacao:
                disponibilidade = "Indisponivel"
                ocupante = ocupacao.usuario.to_dict()

            # Arredonda para o minuto mais próximo fechado
            atual = atual.replace(minute=(atual.minute // intervalo_minutos) * intervalo_minutos, second=0)
            
            slots.append({
                'slot': atual.strftime(formato_hora),
                'disponibilidade': disponibilidade,
                'ocupante': ocupante
            })

            atual += tempo_slot

        return slots


    # Adicionando este método à classe Agenda
    def obter_slots_agenda(self, id_sala, data, intervalo_minutos):
        return self.gerar_slots(id_sala, data, self.hora_inicio.strftime("%H:%M:%S"), self.hora_fim.strftime("%H:%M:%S"), intervalo_minutos)

class LogOps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(User.__tablename__ + '.id'), nullable=False)
    id_agenda = db.Column(db.Integer, nullable=True)
    momento_operacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    operacao = db.Column(db.String(100), nullable=False)
    
    usuario = db.relationship('User', backref='logops', foreign_keys=[id_usuario])
    
    def __init__(self, id_usuario, id_agenda, operacao):
        tz_recife = pytz.timezone('America/Recife')
        
        self.id_usuario = id_usuario
        self.id_agenda = id_agenda
        self.operacao = operacao
        self.momento_operacao =  datetime.now(tz_recife)
        
    def to_dict(self):
        return {
            'id_log': self.id,
            'usuario': {
                'id': self.usuario.id,
                'username': self.usuario.username,
                'setor': self.usuario.setor.setor,
            },
            'id_agenda': self.id_agenda,
            'momento_operacao': self.momento_operacao,
            'operacao': self.operacao
        }

class Relogio_slots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_relogio = db.Column(db.String(50), unique=True, nullable=False)
    inicio = db.Column(db.Time, nullable=False)
    fim = db.Column(db.Time, nullable=False)
    em_vigor = db.Column(db.Boolean, nullable=True)
    
    def __init__ (self, nome_relogio, inicio, fim):
        self.nome_relogio = nome_relogio
        self.inicio = inicio
        self.fim = fim
        self.em_vigor = True
        
    def to_dict(self):
        return {
            'id': self.id,
            'nome_relogio': self.nome_relogio,
            'inicio': self.inicio,
            'fim': self.fim,
            'vigencia': self.em_vigor
        }
    