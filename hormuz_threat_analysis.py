import geopandas as gpd
from shapely.geometry import Point

# Basi Hormuz
basi = gpd.GeoDataFrame({
    "name": ["Bandar Abbas", "Dubai", "Muscat", "Fujairah", "Abu Dhabi", "Khasab"],
    "type": ["Naval", "Air", "Naval", "Naval", "Naval", "Strategic"],
}, geometry=[
    Point(56.2666, 27.1832),
    Point(55.2708, 25.2048),
    Point(58.3829, 23.5880),
    Point(56.3265, 25.1288),
    Point(54.3773, 24.4539),
    Point(56.2500, 26.1833),
], crs="EPSG:4326")

# Carica mappa mondiale
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(url)

# Spatial join
joined = gpd.sjoin(basi, world[["NAME", "geometry"]], 
                   how="left", predicate="within")

# Stampa ogni base → paese
print("Threat Analysis")
for idx, row in joined.iterrows():
    print(f"  {row['name']} ({row['type']}) → {row['NAME']}")

# Conta per paese
print("\n--- Basi per paese ---")
count = joined.groupby("NAME").size()
for paese, n in count.items():
    print(f"  {paese}: {n} base/i")
# Filtra paesi del Golfo dalla mappa mondiale
gulf_countries = world[world["NAME"].isin(["Iran", "Oman", "United Arab Emirates"])]

# Popolazione totale
print("\n--- Population Intelligence ---")
for idx, row in gulf_countries.iterrows():
    pop_m = round(row["POP_EST"] / 1000000, 1)
    print(f"  {row['NAME']}: {pop_m}M abitanti")

total = gulf_countries["POP_EST"].sum()
print(f"\nTotal Gulf population: {round(total/1000000, 1)}M")

# GDP
print("\n--- GDP Intelligence ---")
for idx, row in gulf_countries.iterrows():
    gdp = round(row["GDP_MD"] / 1000, 1)
    print(f"  {row['NAME']}: ${gdp}B GDP")