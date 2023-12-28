import requests


class ISSLocationFetcher:
    def __init__(self):
        self.url = "https://api.wheretheiss.at/v1/satellites/25544"
        self.latitude = None
        self.longitude = None
        self.velocity = None

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            self.latitude = data["latitude"]
            self.longitude = data["longitude"]
            self.velocity = data["velocity"]
        else:
            raise Exception(
                "Error al hacer la llamada HTTP. Código de estado:", response.status_code)

    def get_latitude(self):
        if self.latitude is None:
            self.fetch_data()
        return self.latitude

    def get_longitude(self):
        if self.longitude is None:
            self.fetch_data()
        return self.longitude

    def get_velocity(self):
        if self.velocity is None:
            self.fetch_data()
        return self.velocity


location_fetcher = ISSLocationFetcher()
try:
    location_fetcher.fetch_data()
    print("Donde esta el ISS?")
    print("Latitud:", location_fetcher.get_latitude())
    print("Longitud:", location_fetcher.get_longitude())
    print("Velocity", location_fetcher.get_velocity())
except Exception as e:
    print(str(e))
