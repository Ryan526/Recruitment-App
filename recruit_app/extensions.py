# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# from flask_login import LoginManager
# login_manager = LoginManager()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.security import Security, SQLAlchemyUserDatastore
from recruit_app.user.models import User, Role
security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

from flask_migrate import Migrate
migrate = Migrate()

from flask_cache import Cache
cache = Cache()

from flask_debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

from rq_dashboard import RQDashboard
rqDashboard = RQDashboard()

from flask_admin import Admin
admin = Admin()