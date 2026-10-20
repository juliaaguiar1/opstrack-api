from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "OpsTrack API funcionando!"})


@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "online"})


@app.route("/tickets", methods=["GET"])
def tickets():
    return jsonify({"tickets": [
        {"id": 1, "titulo": "Erro no sistema", "status": "aberto"},
        {"id": 2, "titulo": "Problema de acesso", "status": "fechado"},
    ]})


@app.route("/sobre", methods=["GET"])
def sobre():
    return jsonify({"nome": "OpsTrack API", "versao": "1.0.0"})


@app.route("/versao", methods=["GET"])
def versao():
    return jsonify({"versao": "1.0.0"})


@app.route("/version", methods=["GET"])
def version():
    return jsonify({"versao": "1.0.0"})


@app.route("/usuarios", methods=["GET"])
def usuarios():
    return jsonify({"usuarios": [
        {"id": 1, "nome": "Ana"},
        {"id": 2, "nome": "Bruno"},
    ]})


if __name__ == "__main__":
    app.run(debug=True)
