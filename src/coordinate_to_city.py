# coding: utf-8

from urllib.request import *
from urllib.parse import *
import urllib
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

class CoordinateChanger():
    def __init__(self):
        self.G_APIKEY = "自分のAPI"
        self.G_base = "https://maps.googleapis.com/maps/api/geocode/json?language=ja"
        self.G_sensor = "false"

        self.N_base = "https://www.finds.jp/ws/rgeocode.php?json"

    def send_request(self, url):
        try:
            response = urlopen(url)
            doc = response.read()
            return doc
        except HTTPErrorProcessor:
            print("404")
            return None

    def make_request_url(self, lat, lng):
        # Google
        #url = "{}&latlng={},{}".format(self.G_base, lat, lng)
        #url += "&sensor={}".format(self.G_sensor)
        #url += "&key={}".format(self.G_APIKEY)

        # 農研機構
        url = "{}&lat={}&lon={}".format(self.N_base, lat, lng)
        return url

    def change_coordinate_to_city(self, lat, lng):
        url = self.make_request_url(lat, lng)
        return self.send_request(url)

    def get_response(self,lat, lng):
        # GoogleなんとかAPI -> JSON
        #JSON = self.change_coordinate_to_city(lat, lng).decode("utf-8")
        #data = json.loads(JSON)
        # address = data["results"][1]["address_components"][3]["long_name"]
        #sub_address = data["results"][1]["address_components"][2]["long_name"]
        #return address+sub_address

        #農研機構
        JSON = self.change_coordinate_to_city(lat,lng)
        data = json.loads(JSON)
        return data

    def get_city(self, lat, lng):
        JSONFILE = self.get_response(lat, lng)
        values = JSONFILE['result']['municipality']['mname']
        value = values.split(" ")
        city_name = value[-1]
        return city_name


a = CoordinateChanger()
b = a.get_city("34.7604130", "135.6269390")
print(b)

