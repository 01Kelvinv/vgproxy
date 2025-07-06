from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todos os domínios, seu front poderá acessar sem erro

API_URL = "http://servicos.cittati.com.br/WSIntegracaoCittati/Operacional/ConsultarViagens"
auth = HTTPBasicAuth("wsgru", "123")  # Mantenha assim ou depois use variável ambiente para mais segurança

@app.route("/api/viagens")
def viagens():
    data = request.args.get("data")
    empresa = request.args.get("empresa")
    params = {"data": data, "empresa": empresa}

    try:
        r = requests.get(API_URL, params=params, auth=auth, timeout=10)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
