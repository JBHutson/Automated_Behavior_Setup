from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Cage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    minute = db.Column(db.Integer, unique=False, nullable=False)
    lick = db.Column(db.Integer, unique=False, nullable=False)
    mouse = db.Column(db.String(80), unique=False, nullable=False)
    time = db.Column(db.DateTime(), unique=False, nullable=False)
    cage = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return self.mouse


@app.route('/')
def index():
    return 'server running'

@app.route('/mice_active', methods=['GET'])
def get_mice_active():
    active_mice = []
    for mouse in mice:
        if mouse['active'] == True:
            active_mice.append({'id': mouse['id']})
    return jsonify(active_mice)

@app.route('/cage_info/<mouse>', methods=['GET'])
def get_data(mouse):
    mouse_info = Cage.query.filter_by(mouse=mouse)
    return jsonify(mouse_info)