import geopandas as gpd
from shapely.geometry import Point

# Basi Hormuz + Tehran
basi = gpd.GeoDataFrame({
    "name": ["Tehran", "Bandar Abbas", "Dubai", "Muscat", "Fujairah", "Abu Dhabi"],
}, geometry=[
    Point(51.3890, 35.6892),
    Point(56.2666, 27.1832),
    Point(55.2708, 25.2048),
    Point(58.3829, 23.5880),
    Point(56.3265, 25.1288),
    Point(54.3773, 24.4539),
], crs="EPSG:4326")

print(basi)

# Converti in metri per distanze reali
basi_m = basi.to_crs("EPSG:3857")

# Prendi Tehran
tehran = basi_m[basi_m["name"] == "Tehran"].geometry.values[0]

# Calcola distanze da Tehran a tutte le basi
print("\n--- Distanze da Tehran ---")
distances = []
for idx, row in basi_m.iterrows():
    dist_km = round(tehran.distance(row.geometry) / 1000)
    distances.append((row["name"], dist_km))

# Ordina per distanza
distances.sort(key=lambda x: x[1])

for name, dist in distances:
    print(f"  {name}: {dist} km")

# Più vicina e più lontana
print(f"\nBase più vicina a Tehran: {distances[1][0]} ({distances[1][1]} km)")
print(f"Base più lontana da Tehran: {distances[-1][0]} ({distances[-1][1]} km)")
# Carica mappa mondiale
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(url)

# Spatial join — quale base è in quale paese?
joined = gpd.sjoin(basi, world[["NAME", "geometry"]], how="left", predicate="within")

print("\n--- Threat Analysis ---")
for idx, row in joined.iterrows():
    print(f"  {row['name']} → {row['NAME']}")

# Conta basi per paese
print("\n--- Basi per paese ---")
count = joined.groupby("NAME").size()
for paese, n in count.items():
    print(f"  {paese}: {n} base/i")