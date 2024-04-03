from .common import *

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')
usuario_blueprint = Blueprint('usuario', __name__, template_folder='templates')
agenda_blueprint = Blueprint('agenda', __name__, template_folder='templates')

from . import admin, agenda, usuario