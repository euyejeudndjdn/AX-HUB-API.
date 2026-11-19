from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'servers.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/servers', methods=['GET'])
def get_servers():
    return jsonify(load_data())

@app.route('/add', methods=['POST'])
def add_server():
    data = request.json
    if data:
        servers = load_data()
        servers.append(data)
        save_data(servers)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400
