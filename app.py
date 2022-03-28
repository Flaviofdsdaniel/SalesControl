from flask import Flask

from ext import dao, model
from ext.config import config

app = Flask(__name__)

config.init_app(app)
dao.init_app(app)
model.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
