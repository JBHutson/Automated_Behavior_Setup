#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

mice = [
    {
        'id': 1,
        'active': True
    },
    {
        'id': 2,
        'active': False
    },
    {
        'id': 3,
        'active': True
    },
    {
        'id': 4,
        'active': False
    }      
]

@app.route('/mice_active', methods=['GET'])
def get_mice_active():
    i = 0
    for mouse in mice:
        if mouse['active'] == True:
            i = i+1
    return str(i)

if __name__ == '__main__':
    app.run(debug=True)