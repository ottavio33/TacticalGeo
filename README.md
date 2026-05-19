# TacticalGeo <img width="1198" height="856" alt="Screenshot 2026-05-19 224932" src="https://github.com/user-attachments/assets/8c5655a3-55f6-4000-9e64-099e230068c6" />

Geospatial intelligence system for the Strait of Hormuz

## What it does
- Processes real geographic data with Python + GeoPandas
- Generates strategic bases, shipping lanes, buffer zones
- Serves data via Flask REST API
- Visualizes layers in QGIS on satellite imagery

## API Endpoints
| Endpoint | Description |
|---|---|
| GET / | API status |
| GET /api/bases | All strategic bases |
| GET /api/bases/naval | Naval bases only |
| GET /api/bases/<name> | Specific base data |
| GET /api/stats | Statistics by type |

## Tech Stack
Python · GeoPandas · Flask · SQLite · QGIS · GeoJSON

## Screenshots


## How to run
pip install flask geopandas
python flask_intro.py

## Author
Ottavio di Thiene — Hamburg, Germany
