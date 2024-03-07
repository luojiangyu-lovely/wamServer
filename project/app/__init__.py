from flask import Flask
from app.settings import BASE_DIR
from flask_cors import CORS

app = Flask(__name__)

app.url_map.strict_slashes = False

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        CONFIG_PATH = BASE_DIR / 'project/settings.py'
        app.config.from_pyfile(CONFIG_PATH, silent=True)
    else:
        app.config.from_mapping(test_config)
    # # 注册blog的视图文件
    from app.login.view import login_bp
    from  app.users.view import user_bp
    # from apps.configTb.view import configTb_bp
    # from apps.languageTb.view import languageTb_bp
    # from apps.gameReportTb.view import gameReportTb_bp
    # from apps.importTb.view import importTb_bp 
    # from apps.winRateSimTb.view import winRateSimTb_bp
    # from apps.mapTb.view import mapTb_bp
    # from apps.teamsBattleTb.view import teamsBattleTb_bp


    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    # app.register_blueprint(configTb_bp)
    # app.register_blueprint(teamsBattleTb_bp)
    # app.register_blueprint(languageTb_bp)
    # app.register_blueprint(gameReportTb_bp)
    # app.register_blueprint(importTb_bp)
    # app.register_blueprint(winRateSimTb_bp)
    # app.register_blueprint(mapTb_bp)
    CORS(app)
    return app



