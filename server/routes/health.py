
from flask import jsonify
from server import app

@app.route("/health")
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)
<<<<<<< HEAD

@app.route('/answer')
def answer():
    answer = {'The Answer to Life the Universe and Everything': 42}
    return jsonify(answer)
=======
>>>>>>> bcaa96a46d3a69cbe207a7ae3e4f41571ce636be

