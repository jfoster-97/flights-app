import requests

def aircraft_in_radius(lat, lon, radius):
    """
    Fetches aircraft data from ADS-B Exchange API within a radius.
    """
    url = f"https://api.adsb.lol/v2/point/{lat}/{lon}/{radius}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Handle cases where no aircraft are returned
        if not data or "ac" not in data:
            return []

        return data.get("ac", [])
    except requests.RequestException as e:
        print(f"HTTP error: {e}")
        return []
    except ValueError as e:
        print(f"JSON parse error: {e}")
        return []
