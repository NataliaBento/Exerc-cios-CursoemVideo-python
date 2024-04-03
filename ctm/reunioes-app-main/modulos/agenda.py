from .common import *

from . import agenda_blueprint

@agenda_blueprint.route('/agenda_sala/<int:id>')
@login_required
def agenda_sala(id):
    email = request.cookies.get('user_email')
    user = User.query.filter_by(email=email).first()
    
    sala = Sala.query.get_or_404(id)
    
    context = {
        'user': user.username,
        'user_id': user.id,
        'navegacao': navegacao('Agendamento'),
        'sala_id': id,
    }
    
    if sala.tipo == 0:
        return render_template('templates-privados/agenda/agenda_sala.html', context=context)
    else:
        return render_template('templates-privados/agenda/agenda_sala_exp.html', context=context)

@agenda_blueprint.route('/slots_sala/<string:data>/<int:id>', methods=['GET'])
@login_required
def slots_sala(data, id):
    relogio_atual = Relogio_slots.query.filter_by(em_vigor=1).first()
    
    sala = Sala.query.get_or_404(id)
    
    if sala.tipo == 0:
        tempo = 15
    else:
        tempo = 12
        
    slots = Agenda.gerar_slots(id, data, relogio_atual.inicio.strftime("%H:%M:%S"), relogio_atual.fim.strftime("%H:%M:%S"), tempo)
    
    return jsonify({'sala': id, 'slots': slots})

@agenda_blueprint.route('/agendar', methods=['POST'])
@login_required
def agendar():
    data = request.get_json()
    
    if data.get('hora_inicio') == '' or data.get('hora_fim') == '':
        return jsonify({'message': 'Ocorreu um erro ao realizar o agendamento. Tente novamente mais tarde'}), 400
    else:
        agenda = Agenda.query.filter_by(data=data.get('data'))
        
        for reuniao in agenda:
            #print(f"Inicio: {reuniao.hora_inicio}, {data.get('hora_inicio')}\nFim: {reuniao.hora_fim}, {data.get('hora_fim')}\n =================================================")
            if (reuniao.hora_inicio == data.get('hora_inicio')) or (reuniao.hora_fim == data.get('hora_fim')) or (reuniao.hora_inicio == data.get('hora_fim')) or (reuniao.hora_fim == data.get('hora_inicio')):
                return jsonify({'message': 'Horário já foi reservado! Tente outro horário.'}), 400
        
        agendamento = Agenda (
            id_sala=data.get('id_sala'),
            id_usuario=data.get('id_usuario'),
            hora_inicio=data.get('hora_inicio'),
            hora_fim=data.get('hora_fim'),
            data=data.get('data')
        )
        
        db.session.add(agendamento)
        db.session.commit()
        
        log(agendamento.id_usuario, agendamento.id, 'Usuario agendou uma reuniao.')
        
        return jsonify({'message': 'Agendamento adicionado com sucesso!'}), 201
    
@agenda_blueprint.route('/cancelar_reuniao/<int:reuniao_id>', methods=['POST'])
@login_required
def cancelar_reuniao(reuniao_id):
    try:
        # Obter a reunião pelo ID
        reuniao = Agenda.query.get(reuniao_id)
        user_id = request.cookies.get('user_id') # Vem String necessario converter
        
        if reuniao and (int(user_id) == reuniao.id_usuario):
            # Excluir a reunião
            db.session.delete(reuniao)

            # Salvar as alterações no banco de dados
            db.session.commit()

            log(reuniao.id_usuario, reuniao.id, 'Usuario cancelou uma reuniao.')
            
            # Responder com sucesso
            return jsonify({"success": True, "message": "Reunião excluída com sucesso!"})
        else:
            # Se a reunião não for encontrada, responder com erro
            return jsonify({"success": False, "message": "Reunião não encontrada!"}), 404

    except Exception as e:
        # Lidar com qualquer exceção durante o processo
        return jsonify({"success": False, "message": str(e)}), 500
                        