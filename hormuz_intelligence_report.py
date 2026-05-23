import geopandas as gpd
from shapely.geometry import Point
import json

basi = gpd.GeoDataFrame({
    "name": ["Bandar Abbas", "Dubai", "Muscat", "Fujairah",
             "Khasab", "Doha", "Bab el-Mandeb"],
    "type": ["Naval", "Air", "Naval", "Naval",
             "Strategic", "Strategic", "Strategic"],
}, geometry=[
    Point(56.2666, 27.1832),
    Point(55.2708, 25.2048),
    Point(58.3829, 23.5880),
    Point(56.3265, 25.1288),
    Point(56.2500, 26.1833),
    Point(51.5310, 25.2854),
    Point(43.3667, 12.5833),
], crs="EPSG:4326")

# Buffer 150km
basi_m = basi.to_crs("EPSG:3857")
buffers = basi_m.copy()
buffers["geometry"] = buffers.geometry.buffer(150000)
buffers = buffers.to_crs("EPSG:4326")

# Build GeoJSON
geojson = {"type": "FeatureCollection", "features": []}

# Aggiungi buffer zones
for idx, row in buffers.iterrows():
    geojson["features"].append({
        "type": "Feature",
        "geometry": row.geometry.__geo_interface__,
        "properties": {"name": row["name"], "type": "buffer"}
    })

# Aggiungi punti
for idx, row in basi.iterrows():
    geojson["features"].append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row.geometry.x, row.geometry.y]
        },
        "properties": {"name": row["name"], "type": row["type"]}
    })

# Rotta principale — solo sull'acqua
geojson["features"].append({
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [
            [56.4000, 26.5000],
            [58.0000, 23.0000],
            [57.5000, 20.0000],
            [55.0000, 16.0000],
            [50.0000, 13.0000],
            [45.0000, 12.0000],
            [43.3667, 12.5833],
        ]
    },
    "properties": {"name": "Main Shipping Route", "type": "shipping"}
})

# Oil tanker route — Golfo Persico interno
geojson["features"].append({
    "type": "Feature",
    "geometry": {
        "type": "LineString",
        "coordinates": [
            [50.2000, 26.5000],
            [51.5000, 26.0000],
            [53.0000, 25.5000],
            [55.0000, 25.0000],
            [56.2000, 26.0000],
            [56.4000, 26.5000],
        ]
    },
    "properties": {"name": "Oil Tanker Route", "type": "oil"}
})

with open("hormuz_complete.geojson", "w") as f:
    json.dump(geojson, f, indent=2)

print("=== HORMUZ COMPLETE MAP ===")
print(f"Punti strategici: {len(basi)}")
print("Shipping lanes: 2")
print("Buffer zones: 7")
print("\nhormuz_complete.geojson saved!")
print("JOBDONE")