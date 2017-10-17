# coding: utf-8

from urllib.request import *
from urllib.parse import *
import json

class CoordinateChanger():
    def __init__(self):
        self.APIKEY = "自分のAPI"
        self.G_base = "https://maps.googleapis.com/maps/api/geocode/json?language=ja"
        self.G_sensor = "false"

    def send_request(self, url):
        try:
            response = urlopen(url)
            doc = response.read()
            return doc
        except HTTPErrorProcessor:
            print("404")
            return None

    def make_request_url(self, lat, lng):
        url = "{}&latlng={},{}".format(self.G_base, lat, lng)
        url += "&sensor={}".format(self.G_sensor)
        url += "&key={}".format(self.APIKEY)
        return url

    def change_coordinate_to_city(self, lat, lng):
        url = self.make_request_url(lat, lng)
        return self.send_request(url)

    def get_address(self,lat, lng):
        JSON = self.change_coordinate_to_city(lat, lng).decode("utf-8")
        data = json.loads(JSON)
        address = data["results"][1]["address_components"][3]["long_name"]
        sub_address = data["results"][1]["address_components"][2]["long_name"]
        return address+sub_address


def main():
    coordinateChanger = CoordinateChanger()
    lat = "34.7604130"
    lng = "135.6269390"
    result = coordinateChanger.get_address(lat, lng)
    return result.decode("utf-8")

a = CoordinateChanger()
b = a.get_address("34.7604130", "135.6269390")
print(b)