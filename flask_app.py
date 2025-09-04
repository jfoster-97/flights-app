from flask import Flask, request, render_template
from adsb_api import aircraft_in_radius
from models import Flight
import json

app = Flask(__name__)

# Default locations (NY + Ely, UK)
ny_lat_lon = (40.6407518, -73.7841027)
ely_lat_lon = (52.399774, 0.247412)

@app.route("/")
def home():
    """Render the main frontend page."""
    return render_template("index.html")

@app.route("/flights")
def get_flights():
    """Fetch flights in a given radius and return enriched data."""
    lat = float(request.args.get("lat", ny_lat_lon[0]))
    lon = float(request.args.get("lon", ny_lat_lon[1]))
    radius = float(request.args.get("radius", 15))

    try:
        flights_raw = aircraft_in_radius(lat, lon, radius)
        flights = [Flight.from_api(ac).to_dict() for ac in flights_raw]

        return app.response_class(
            response=json.dumps(flights, ensure_ascii=False, indent=2),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps({"error": str(e)}, ensure_ascii=False, indent=2),
            status=500,
            mimetype="application/json"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
