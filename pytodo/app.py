from pytodo.extensions import appearance, configs, database
from pytodo.blueprints import views
from flask import Flask

app = Flask(__name__)
configs.init_app(app)
appearance.init_app(app)
database.init_app(app)
views.init_app(app)
    
if __name__ == "_main__":
    app.run(debug=True, host='0.0.0.0')