import sqlite3

conn = sqlite3.connect("tactical.db")
cursor = conn.cursor()

# Drop e ricrea tabella pulita
cursor.execute("DROP TABLE IF EXISTS bases")
cursor.execute("""
    CREATE TABLE bases (
        id INTEGER PRIMARY KEY,
        name TEXT,
        lat REAL,
        lon REAL,
        type TEXT
    )
""")

cursor.execute("INSERT INTO bases VALUES (1, 'Hamburg',  53.55, 9.99,  'Naval')")
cursor.execute("INSERT INTO bases VALUES (2, 'Berlin',   52.52, 13.40, 'Air')")
cursor.execute("INSERT INTO bases VALUES (3, 'Roma',     41.90, 12.50, 'Terrestrial')")
cursor.execute("INSERT INTO bases VALUES (4, 'Dubai',    25.20, 55.27, 'Naval')")
cursor.execute("INSERT INTO bases VALUES (5, 'Tehran',   35.68, 51.38, 'Strategic')")

conn.commit()
print("Database created!")

cursor.execute("SELECT * FROM bases")
rows = cursor.fetchall()
print("\n--- All bases ---")
for row in rows:
    print(f"{row[1]} -> lat {row[2]}, type {row[4]}")

# Filter with WHERE
print("\n--- Only Naval bases ---")
cursor.execute("SELECT name, lat FROM bases WHERE type = 'Naval'")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]} -> lat {row[1]}")

# Filter by latitude
print("\n--- Bases north of 45° ---")
cursor.execute("SELECT name, lat FROM bases WHERE lat > 45")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]} -> {row[1]}°")

# Count
print("\n--- Count ---")
cursor.execute("SELECT COUNT(*) FROM bases")
total = cursor.fetchone()
print(f"Total bases: {total[0]}")

# Order by latitude
print("\n--- Bases ordered North to South ---")
cursor.execute("SELECT name, lat FROM bases ORDER BY lat DESC")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]} -> {row[1]}°")

# Multiple filters
print("\n--- Naval bases north of 30° ---")
cursor.execute("SELECT name, lat FROM bases WHERE type = 'Naval' AND lat > 30")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]} -> {row[1]}°")

conn.close()