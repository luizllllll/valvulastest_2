from flask import Flask, jsonify

app = Flask(__name__)

valvulas = [
    {
        "id": 1,
        "nome": "Válvula esfera",
        "material": "Inox",
        "estoque": 20
    },
    {
        "id": 2,
        "nome": "Válvula gaveta",
        "material": "Aço carbono",
        "estoque": 10
    }
]


@app.get("/")
def inicio():
    return "Sistema de logística de válvulas funcionando!"


@app.get("/valvulas")
def listar_valvulas():
    return jsonify(valvulas)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)