import urllib.request
import json

# Step 1 - Login e ottieni token
data = json.dumps({"username": "ottavio", "password": "hormuz2026"}).encode()
req = urllib.request.Request(
    "http://localhost:5000/login",
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())
    token = result["token"]
    print(f"Token ricevuto: {token[:50]}...")

# Step 2 - Usa il token per accedere ai dati
req2 = urllib.request.Request(
    "http://localhost:5000/api/bases",
    headers={"Authorization": f"Bearer {token}"}
)

with urllib.request.urlopen(req2) as response:
    bases = json.loads(response.read())
    print(f"\nBasi ricevute: {len(bases)}")
    for base in bases:
        print(f"  {base['name']} → {base['type']}")