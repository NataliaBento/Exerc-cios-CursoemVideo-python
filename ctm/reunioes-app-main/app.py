from modulos import *

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_APP_KEY_ROOMS', 'not-secret-flask123')

app.config.from_object(Config)

db.init_app(app)

CORS(app) 

migrate = Migrate(app, db)

load_dotenv()

def run_migrations():
    with app.app_context():
        # Executa as migrações antes de iniciar o aplicativo
        dump_database()
        
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticacao', methods=['POST'])
def authenticate():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        # Salva os dados do usuário em um cookie
        response = make_response(jsonify({'success': True, 'user': f'{user.id}'}))
        response.set_cookie('user_id', str(user.id))
        response.set_cookie('user_email', user.email)
        
        log = LogUser(
            id_usuario=user.id
        )
        
        db.session.add(log)
        db.session.commit()
        
        return response
    else:
        return jsonify({'success': False, 'message': 'Login falhou. Verifique suas credenciais.'})
    
@app.route('/logout')
@login_required
def logout():
    # Limpa os cookies de autenticação e redireciona para a página de login
    response = make_response(redirect(url_for('login')))
    response.set_cookie('user_id', '', expires=0)
    response.set_cookie('user_email', '', expires=0)
    return response

@app.route('/')
@login_required
def index():
    email = request.cookies.get('user_email')
    user = User.query.filter_by(email=email).first()
    
    salas = Sala.query.all()
    
    reunioes_all = Agenda.query.filter_by(id_usuario=user.id).all()
    
    reunioes_next = []
   
    for reuniao in reunioes_all:
        if reuniao.data >= date.today( ):
            reunioes_next.append(reuniao)
    
    context = {
        'user': user.username,
        'navegacao': navegacao('Inicio'),
        'salas': salas,
        'reunioes': reunioes_next,
    }
    
    #print(context['user'])
    return render_template("templates-privados/index.html", context=context)

@app.route('/sobre')
@login_required
def sobre():
    app_version = os.getenv("APP_VERSION")
    
    user = User.query.get_or_404(request.cookies.get('user_id'))
    
    context = {
        'env' : app_version,
        'user': user.username,
        'navegacao': navegacao('Inicio')
    }
    
    return render_template('/templates-privados/sobre.html', context=context)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('erros/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('erros/404.html'), 404


app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(usuario_blueprint, url_prefix='/usuario')
app.register_blueprint(agenda_blueprint, url_prefix='/agenda')

if __name__ == '__main__':
    # Executa as migrações antes de iniciar o aplicativo
    #run_migrations()
    
    app.run(debug=True, port=os.getenv("PORT", default=8081), use_reloader=True)