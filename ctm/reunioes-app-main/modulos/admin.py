from .common import *

from . import admin_blueprint

@admin_blueprint.route('/painel_administrativo')
@login_required
@login_admin_required
def painel_administrativo():
    email = request.cookies.get('user_email')
    user = User.query.filter_by(email=email).first()
    
    salas = Sala.query.all()
    setores = Setor.query.all()
    
    context = {
        'user': user.username,
        'navegacao': navegacao('Admin'),
        'salas': salas,
        'setores': setores,
    }
    
    return render_template('templates-privados/admin/painel_administrativo.html', context=context)


#ROTAS DE USUARIO

@admin_blueprint.route('/getUsuarios', methods=['GET'])
@login_required
@login_admin_required
def getUsuarios():
    usuarios = User.query.all()
    return jsonify({'usuarios': [usuario.to_dict() for usuario in usuarios]}), 200

@admin_blueprint.route('/getUsuario/<int:id>', methods=['GET'])
@login_required
@login_admin_required
def getUsuario(id):
    usuario = User.query.get_or_404(id)
    return jsonify({'usuario': usuario.to_dict()}), 200

@admin_blueprint.route('/addUsuario', methods=['POST'])
@login_required
@login_admin_required
def addUsuario():
    data = request.get_json()
    
    usuario = User (
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password'),
        nivel_acesso=data.get('nivel_acesso'),
        setor=data.get('setor_id')
    )
    
    db.session.add(usuario)
    db.session.commit()
    
    log(request.cookies.get('user_id'), None, f"Usuário cadastrou um novo usuário. Usuário cadastrado: {usuario.id}")
    
    return jsonify({'message': 'Usuario adcionado com sucesso!'}), 201

@admin_blueprint.route('/updtUsuario/<int:id>', methods=['POST'])
@login_required
@login_admin_required
def updtUsuario(id):
    data = request.get_json()

    usuario = User.query.get_or_404(id)
    
    usuario.username=data.get('username')
    usuario.email=data.get('email')
    usuario.set_password(data.get('password'))
    usuario.nivel_acesso=data.get('nivel_acesso')
    usuario.id_setor=data.get('setor_id')
    
    db.session.commit()
    
    log(request.cookies.get('user_id'), None, f"Usuário atualizou um usuário. Usuário atualizado: {usuario.id}")
    
    return jsonify({'message': 'Usuario atualizado com sucesso!'}), 201



@admin_blueprint.route('/getSalas', methods=['GET'])
@login_required
@login_admin_required
def getSalas():
    salas = Sala.query.all()
    return jsonify({'salas': [sala.to_dict() for sala in salas]})


@admin_blueprint.route('/getSala/<int:id>', methods=['GET'])
@login_required
@login_admin_required
def getSala(id):
    sala = Sala.query.get_or_404(id)
    return jsonify({'sala': sala.to_dict()}), 200


@admin_blueprint.route('/addSala', methods=['POST'])
@login_required
@login_admin_required
def addSala():
    data = request.get_json()
    
    sala = Sala (
        sala=data.get('sala'),
        tipo=data.get('tipo')
    )
    
    db.session.add(sala)
    db.session.commit()
    
    log(request.cookies.get('user_id'), None, 'Usuario criou uma sala.')
    
    return jsonify({'message': 'Sala criada com sucesso!'}), 201


@admin_blueprint.route('/updtSala/<int:id>', methods=['POST'])
@login_required
@login_admin_required
def updtSala(id):
    data = request.get_json()

    sala = Sala.query.get_or_404(id)
    
    sala.sala=data.get('sala')
    sala.tipo=data.get('tipo')
    
    db.session.commit()
    
    log(request.cookies.get('user_id'), None, 'Usuario atualizou uma sala.')
    
    return jsonify({'message': 'Sala atualizada com sucesso!'}), 201
