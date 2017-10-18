# coding: utf-8

from urllib.request import *
from urllib.parse import *
import urllib
import json
import xml.etree.ElementTree as ET

class CoordinateChanger():
    def __init__(self):
        self.G_APIKEY = "自分のAPI"
        self.Y_APIKEY = "dj00aiZpPXFQV1VmSTRobjFjUSZzPWNvbnN1bWVyc2VjcmV0Jng9OWY-"
        self.G_base = "https://maps.googleapis.com/maps/api/geocode/json?language=ja"
        self.Y_base = "https://map.yahooapis.jp/geoapi/V1/reverseGeoCoder?"
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
        # Google
        #url = "{}&latlng={},{}".format(self.G_base, lat, lng)
        #url += "&sensor={}".format(self.G_sensor)
        #url += "&key={}".format(self.G_APIKEY)

        # Yahoo
        url = "{}lat={}&lon={}".format(self.Y_base, lat, lng)
        url += "&appid={}".format(self.Y_APIKEY)

        # aaa = "https://map.yahooapis.jp/geoapi/V1/reverseGeoCoder?lat=35.68381981&lon=139.77456498&appid={}".format(self.Y_APIKEY)
        return url

    def change_coordinate_to_city(self, lat, lng):
        url = self.make_request_url(lat, lng)
        return self.send_request(url)

    def get_address(self,lat, lng):
        # GoogleなんとかAPI -> JSON
        #JSON = self.change_coordinate_to_city(lat, lng).decode("utf-8")
        #data = json.loads(JSON)
        # address = data["results"][1]["address_components"][3]["long_name"]
        #sub_address = data["results"][1]["address_components"][2]["long_name"]
        #return address+sub_address

        #YahooなんとかAPI
        url = self.make_request_url(lat, lng)
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:
            XmlData = response.read()
        return XmlData

    def parse_xml(self, lat, lng):
        xml_data = self.get_address(lat, lng)
        result = ET.fromstring(xml_data)
        return result




def main():
    coordinateChanger = CoordinateChanger()
    lat = "34.7604130"
    lng = "135.6269390"
    XmlData = coordinateChanger.get_address(lat, lng)
    root = ET.fromstring(XmlData)
    return root

a = CoordinateChanger()
b = a.get_address("34.7604130", "135.6269390")
print(b.decode("utf-8"))