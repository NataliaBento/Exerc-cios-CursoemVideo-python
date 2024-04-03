from flask import Flask, jsonify, render_template, request, make_response, redirect, url_for, Blueprint
from flask_migrate import Migrate, upgrade
from flask_cors import CORS
from flask_paginate import Pagination
from config import Config
from models import db
from functools import wraps
from sqlalchemy import desc, func
import subprocess
import os
from datetime import date
from dotenv import load_dotenv

# Importação dos modelos
from models import *


def dump_database():
    # Executa flask db init
    subprocess.run(['flask', 'db', 'init'])

    # Executa flask db migrate
    subprocess.run(['flask', 'db', 'migrate'])

    # Executa flask db upgrade
    subprocess.run(['flask', 'db', 'upgrade'])

    existing_user = User.query.filter_by(username='admin').first()
    
    
    if not existing_user:
        # Se o usuário não existir, cria um novo usuário padrão
        default_user = User(
            username='admin',
            nivel_acesso='admin',
            email='dti@granderecife.pe.gov.br',
            password='#@granderecife_apps@#',
            
            setor=1,
        )
        db.session.add(default_user)
        db.session.commit()
    
    existing_room = Sala.query.filter_by(id=1).first()

    if not existing_room:
        # Se a sala não existir, cria uma nova sala padrão
        default_room = Sala (
            sala='Sala 1',
            tipo=0
        )
        db.session.add(default_room)
        db.session.commit()
    
    existing_setor = Setor.query.filter_by(setor='DTI').first()
    
    if not existing_setor:
        
        setores = ['DTI', 
                   'DOP', 
                   'GTEP', 
                   'GEPO', 
                   'GEST', 
                   'GIPE', 
                   'GPIS', 
                   'GFIS',
                   'GMON',
                   'GTES',
                   'GEBF',
                   'GECO',
                   'GESI',
                   'GINF',
                   'GPLO',
                   'GFIN',
                   'GECH',
                   'GGOR',
                   'GEPA',
                   'GTMA',
                   'GECR',
                   'GERE',
                   'GIMP',
                   'GMKT',
                   'CJU',
                   'GAB',
                   'OUVI',
                   'CF',
                   'CGL',
                   'CIPA',
                   ]
        
        for setor in setores:
            # Se o setor não existir, cria um novo setor padrão
            default_setor = Setor(
                setor=setor
            )
            db.session.add(default_setor)
            db.session.commit()
        
    existing_clock = Relogio_slots.query.filter_by(nome_relogio='Relogio Padrão').first()
    
    if not existing_clock:
        default_clock = Relogio_slots (
            nome_relogio = 'Relogio Padrão',
            inicio="07:30:00",
            fim="16:30:00",
        )
        db.session.add(default_clock)
        db.session.commit()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = request.cookies.get('user_id')
        user_email = request.cookies.get('user_email')

        if user_id and user_email:
            user = User.query.filter_by(id=user_id, email=user_email).first()
            if user:
                # Adiciona o usuário à requisição para ser acessado nas rotas protegidas
                request.user = user
                return f(*args, **kwargs)

        # Redireciona para a página de login se o usuário não estiver autenticado
        return redirect(url_for('login'))

    return decorated_function

def login_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = request.cookies.get('user_id')
        user_email = request.cookies.get('user_email')

        if user_id and user_email:
            user = User.query.filter_by(id=user_id, email=user_email).first()
            if user and user.nivel_acesso == 'admin':
                # Adiciona o usuário à requisição para ser acessado nas rotas protegidas
                request.user = user
                return f(*args, **kwargs)

        # Redireciona para a página de login se o usuário não estiver autenticado
        return jsonify({'messsage': 'Somente usuário autorizado'}), 401

    return decorated_function

def navegacao(pagina):
    # 'NOME DA PAGINA NO FRONT' : ['ROTA DA PAGINA', 'PAGINA ATIVA OU NÃO']
    usuario = User.query.filter_by(id=request.cookies.get('user_id')).first()
    
    if usuario.nivel_acesso == 'admin': 
        paginas = {
            'Inicio': ['index', ''],
            'Agendamento': ['',''],
            'Histórico': ['usuario.historico',''],
            'Admin': ['admin.painel_administrativo',''],
        }
    else:
        paginas = {
            'Inicio': ['index', ''],
            'Agendamento': ['',''],
            'Histórico': ['usuario.historico',''],
            'Perfil': ['usuario.perfil',''],
        }
        
    paginas[f'{pagina}'][1] = 'uk-active'
    """
    print(paginas)
    for item in paginas:
        print(paginas[item])
    """
        
    return paginas

@login_required
def log(id_u, id_a, op):
    log_operacao = LogOps (
        id_usuario=id_u,
        id_agenda= id_a,
        operacao = op
    )
    
    db.session.add(log_operacao)
    db.session.commit()

@login_required
def paginate(query, page=1, per_page=10):
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    items = query.slice(start_index, end_index).all()
    return items


    
    
    