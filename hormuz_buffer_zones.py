import geopandas as gpd
from shapely.geometry import Point

basi = gpd.GeoDataFrame({
    "name": ["Bandar Abbas", "Dubai", "Muscat"],
}, geometry=[
    Point(56.2666, 27.1832),
    Point(55.2708, 25.2048),
    Point(58.3829, 23.5880),
], crs="EPSG:4326")

# Converti in metri
basi_m = basi.to_crs("EPSG:3857")

# Crea buffer di 200km
buffers = basi_m.copy()
buffers["geometry"] = buffers.geometry.buffer(200000)

# Converti back in gradi e salva
buffers = buffers.to_crs("EPSG:4326")
buffers.to_file("buffers.geojson", driver="GeoJSON")

print("JobDon")