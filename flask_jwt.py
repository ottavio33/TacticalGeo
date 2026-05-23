from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

# Secret Key
app.config["JWT_SECRET_KEY"] = "tacticalgeo-secret-2026"
jwt = JWTManager(app)

# === LOGIN ===
@app.route('/login', methods=['POST'])
def login():
    dati = request.get_json()
    username = dati.get("username")
    password = dati.get("password")

    # Credentials hardcoded 
    if username == "ottavio" and password == "hormuz2026":
        token = create_access_token(identity=username)
        return jsonify(token=token)
    
    return jsonify({"error": "credenziali errate"}), 401

# ** Pubblic Route **
@app.route('/')
def home():
    return jsonify({"status": "TacticalGeo API online"})

# ++ Protected Route ++
@app.route('/api/bases')
@jwt_required()
def get_bases():
    bases = [
        {"name": "Bandar Abbas", "lat": 27.1832, "lon": 56.2666, "type": "Naval"},
        {"name": "Dubai",        "lat": 25.2048, "lon": 55.2708, "type": "Air"},
        {"name": "Muscat",       "lat": 23.5880, "lon": 58.3829, "type": "Naval"},
        {"name": "Fujairah",     "lat": 25.1288, "lon": 56.3265, "type": "Naval"},
    ]
    return jsonify(bases)

if __name__ == '__main__':
    app.run(debug=True)
