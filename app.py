from flask import Flask
import os
import yaml

from src.main.python.controller.product_controller import product_bp
from src.main.python.dao.base_dao import db
from src.main.python.exception.global_exception_handler import init_exception_handler
from src.main.python.controller.user_controller import user_bp

app = Flask(__name__)

def load_config(app):
    config_path = os.path.join(os.path.dirname(__file__), 'src/main/resource/application.yml')
    config_path = os.path.normpath(config_path)
    with open(config_path, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        app.config.update(
            SERVER_PORT=config['server']['port'],
            SQLALCHEMY_DATABASE_URI=f"mysql+mysqlconnector://{config['mysql']['username']}:{config['mysql']['password']}@{config['mysql']['host']}:{config['mysql']['port']}/{config['mysql']['database']}",
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

# 加载配置
load_config(app)

# 初始化数据库
db.init_app(app)

# 初始化异常处理器
init_exception_handler(app)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

# 创建数据库表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=app.config['SERVER_PORT'])