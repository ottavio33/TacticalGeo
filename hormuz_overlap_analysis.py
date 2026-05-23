import geopandas as gpd
from shapely.geometry import Point

basi = gpd.GeoDataFrame({
    "name": ["Bandar Abbas", "Dubai", "Muscat"],
}, geometry=[
    Point(56.2666, 27.1832),
    Point(55.2708, 25.2048),
    Point(58.3829, 23.5880),
], crs="EPSG:4326")

# Converti in metri e crea buffer 200km
basi_m = basi.to_crs("EPSG:3857")
buffers = basi_m.copy()
buffers["geometry"] = buffers.geometry.buffer(200000)

# Controlla sovrapposizioni
print("--- Overlap Analysis ---")
for i, row1 in buffers.iterrows():
    for j, row2 in buffers.iterrows():
        if i < j:
            if row1.geometry.intersects(row2.geometry):
                overlap = row1.geometry.intersection(row2.geometry)
                area_km2 = round(overlap.area / 1000000)
                print(f"  {row1['name']} ∩ {row2['name']}: {area_km2} km²")
            else:
                print(f"  {row1['name']} ∩ {row2['name']}: no overlap")