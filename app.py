from flask import Flask, jsonify, request

app = Flask(__name__)

"""
VARIÁVEIS TEMPORÁRIAS
"""
chamados = []
proximo_id = 1

"""
ROTAS da aplicação:
"""

@app.get("/")
def inicio():
    """ROTA inicial da aplicação"""
    return jsonify({"mensagem": "API de chamados em funcionamento"}), 200


@app.post("/chamados")
def create_chamado():
    """Salva o chamado"""
    global chamados
    global proximo_id

    dados = request.get_json()

    novo_chamado = {
        "id": proximo_id,
        "titulo": dados.get("titulo"),
        "descricao": dados.get("descricao"),
        "solicitante": dados.get("solicitante"),
        "prioridade": dados.get("prioridade"),
        "status": "aberto", 
    }

    chamados.append(novo_chamado)
    proximo_id += 1

    return jsonify(novo_chamado), 201


@app.get("/chamados")
def get_chamados():
    global chamados
    return jsonify(chamados), 200


@app.get("/chamados/<int:chamado_id>")
def get_chamado_by_id(chamado_id):
    """Retorna o chamado que tem id == chamado_id"""
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return jsonify(chamado), 200

    return jsonify({"mensagem": "Chamado não encontrado"}), 404