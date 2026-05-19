from flask import Flask, jsonify
import geopandas as gpd
from shapely.geometry import Point

app = Flask(__name__)


def get_hormuz_data():
    return [
        {"name": "Bandar Abbas", "lat": 27.1832, "lon": 56.2666, "type": "Naval"},
        {"name": "Dubai",        "lat": 25.2048, "lon": 55.2708, "type": "Air"},
        {"name": "Muscat",       "lat": 23.5880, "lon": 58.3829, "type": "Naval"},
        {"name": "Fujairah",     "lat": 25.1288, "lon": 56.3265, "type": "Naval"},
        {"name": "Doha",         "lat": 25.2854, "lon": 51.5310, "type": "Strategic"},
        {"name": "Khasab",       "lat": 26.1833, "lon": 56.2500, "type": "Strategic"},
    ]

@app.route('/')
def home():
    return jsonify({"status": "TacticalGeo API online", "version": "1.0"})

@app.route('/api/bases')
def get_bases():
    return jsonify(get_hormuz_data())

@app.route('/api/bases/naval')
def get_naval():
    naval = [b for b in get_hormuz_data() if b["type"] == "Naval"]
    return jsonify(naval)

@app.route('/api/bases/<name>')
def get_base(name):
    bases = get_hormuz_data()
    result = next((b for b in bases if b["name"].lower() == name.lower()), None)
    if result:
        return jsonify(result)
    return jsonify({"error": "Base not found"}), 404

@app.route('/api/stats')
def get_stats():
    bases = get_hormuz_data()
    types = {}
    for b in bases:
        types[b["type"]] = types.get(b["type"], 0) + 1
    return jsonify({
        "total_bases": len(bases),
        "by_type": types,
        "region": "Strait of Hormuz",
        "status": "active"
    })

if __name__ == '__main__':
    app.run(debug=True)
