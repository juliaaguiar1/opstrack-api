from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "OpsTrack API funcionando!"
    })


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "status": "online"
    })


@app.route("/tickets", methods=["GET"])
def tickets():
    return jsonify({
        "tickets": [
            {
                "id": 1,
                "titulo": "Erro no sistema",
                "status": "aberto"
            },
            {
                "id": 2,
                "titulo": "Problema de acesso",
                "status": "fechado"
            }
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)