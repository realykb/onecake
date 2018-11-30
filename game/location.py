from geopy.geocoders import Nominatim


class Locator():
    def __init__(self):
        self.geolocator = Nominatim(user_agent="onecake")

    def _get_location(self, lat, lng):
        return self.geolocator.reverse(", ".join([str(lat), str(lng)]))

    def get_address(self, lat, lng):
        location = self._get_location(lat, lng)
        return location.address

    def get_city(self, lat, lng):
        location = self._get_location(lat, lng)
        return location.raw['address']['city']

    def get_postcode(self, lat, lng):
        location = self._get_location(lat, lng)
        return location.raw['address']['postcode']
