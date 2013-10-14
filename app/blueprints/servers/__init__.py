from flask import Blueprint

blueprint = Blueprint('server_module', __name__, template_folder='templates',
                      url_prefix='/server')

from app import app
from app.blueprints.servers import views

submenu = [
    ('server_module.index', 'List Servers'),
    ('server_module.create_hourly', 'Create Hourly Bare Metal'),
    ('server_module.create_monthly', 'Create Monthly Bare Metal'),
]
app.add_menu('left', submenu, 'Servers', 1)

# Servers Add
blueprint.add_url_rule('/add/hourly', view_func=views.create_hourly,
                       methods=['GET', 'POST'])
blueprint.add_url_rule('/add/monthly', view_func=views.create_monthly)
blueprint.add_url_rule('/add/monthly/<int:package_id>',
                       view_func=views.create_monthly, methods=['GET', 'POST'])

# Servers List
blueprint.add_url_rule('/', view_func=views.index)
blueprint.add_url_rule('/index', view_func=views.index)

# Server Price Check (AJAX call)
blueprint.add_url_rule('/priceCheck/<string:server_type>',
                       view_func=views.price_check, methods=['GET', 'POST'])

# Server Status (AJAX call)
blueprint.add_url_rule('/status', view_func=views.status)
blueprint.add_url_rule('/status/<int:server_id>', view_func=views.status)
