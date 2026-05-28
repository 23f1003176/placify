from flask import Flask

from extensions import db
from models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placify.db"

db.init_app(app)


@app.route("/")
def hello():
    return "hello, placify!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
