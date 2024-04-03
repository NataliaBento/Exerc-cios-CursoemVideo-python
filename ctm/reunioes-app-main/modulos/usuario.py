from .common import *

from . import usuario_blueprint

@usuario_blueprint.route('/perfil')
@login_required
def perfil():
    user = User.query.get_or_404(request.cookies.get('user_id'))
    
    if user.nivel_acesso == 'admin':
        nv = 'Admin'
    else:
        nv = 'Perfil'
    
    context = {
        'user': user.username,
        'navegacao': navegacao(f'{nv}'),
    }
    
    return render_template('templates-privados/usuario/perfil.html', context=context)


@usuario_blueprint.route('/getPerfil')
@login_required
def getPerfil():
    usuario = User.query.get_or_404(request.cookies.get('user_id'))
    
    perfil = {
        'username' : usuario.username,
    }
    
    return jsonify({'usuario': perfil})


@usuario_blueprint.route('/uptdPerfil', methods=['POST'])
@login_required
def uptdPerfil():
    usuario = User.query.get_or_404(request.cookies.get('user_id'))
    data = request.get_json()
    
    print(data)
    
    usuario.username = data.get('username')
    usuario.set_password(data.get('password'))
    
    db.session.commit() 
    
    return jsonify({'message': 'Seu usuário foi alterado com sucesso!'})

@usuario_blueprint.route('/acessos', methods=['GET'])
@login_required
def acessos():
    page = request.args.get('page', type=int, default=1)
    per_page = 10
    
    usuario = User.query.get_or_404(request.cookies.get('user_id'))
    
    if usuario.nivel_acesso == 'admin':
        logs_query = LogUser.query.order_by(LogUser.id.desc())
        nv = 'Admin'
    else:
        logs_query = LogUser.query.filter_by(id_usuario=usuario.id).order_by(LogUser.id.desc())
        nv = 'Perfil'

    logs_pagination = Pagination(page=page, total=logs_query.count(), per_page=per_page, bs_version=3)
    
    logs_acesso = logs_query.offset((page - 1) * per_page).limit(per_page).all()
    
    context = {
        'user': usuario.username,
        'logs_acesso': [log.to_dict() for log in logs_acesso],
        'navegacao': navegacao(f'{nv}')
    }
    
    return render_template('templates-privados/usuario/acessos.html', context=context, pagination=logs_pagination)


@usuario_blueprint.route('/historico', methods=['GET'])
@login_required
def historico():
    page = request.args.get('page', type=int, default=1)
    per_page = 10
    
    usuario = User.query.get_or_404(request.cookies.get('user_id'))
    
    if usuario.nivel_acesso == 'admin':
        logs_query = LogOps.query.order_by(LogOps.id.desc())
        nv = 'Admin'
    else:
        logs_query = LogOps.query.filter_by(id_usuario=usuario.id).order_by(LogOps.id.desc())
        nv = 'Perfil'

    logs_pagination = Pagination(page=page, total=logs_query.count(), per_page=per_page, bs_version=3)
    
    logs_ops = logs_query.offset((page - 1) * per_page).limit(per_page).all()
    
    context = {
        'user': usuario.username,
        'logs_ops': [log.to_dict() for log in logs_ops],
        'navegacao': navegacao('Histórico')
    }
    
    return render_template('templates-privados/usuario/historico.html', context=context, pagination=logs_pagination)


