import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Base de datos simulada en memoria
spell_data = {
    "Pedro123": {
        "spell": "shield",
        "timestamp": 0
    }
}

@app.route("/spell", methods=["GET"])
def get_spell():
    user_id = request.args.get("userId")
    if not user_id:
        return jsonify({"error": "userId missing"}), 400

    data = spell_data.get(user_id, {"spell": "", "timestamp": 0})
    return jsonify(data)

@app.route("/cast", methods=["POST"])
def cast_spell():
    data = request.get_json()
    user_id = data.get("userId")
    spell = data.get("spell")

    if not user_id or not spell:
        return jsonify({"error": "Missing userId or spell"}), 400

    spell_data[user_id] = {
        "spell": spell.lower(),
        "timestamp": int(datetime.now().timestamp())
    }

    return jsonify({"status": "ok", "received": spell_data[user_id]})

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
