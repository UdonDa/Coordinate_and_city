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

    def get_city_name(self, dic):
        lat = dic[0]
        lng = dic[1]
        JSONFILE = self.get_response(lat, lng)
        values = JSONFILE['result']['municipality']['mname']
        value = values.split(" ")
        if(value[0] == "さいたま市"):
            city_name = "さいたま市"
        elif(value[0] == "川口市" or value[0] =="蕨市"):
            city_name = "川口市"
        elif(value[0] == "北区"):
            city_name = "東京都"
        elif(value[0] == "荒川区"):
            city_name = "足立区"
        elif(value[0] == "台東区" or value[0] =="千代田区" or value[0] =="中央区" or value[0] =="港区" or value[0] =="品川区"):
            city_name = "東京都"
        elif(value[0] == "川崎市"):
            city_name = "川崎市"
        elif(value[0] == "大田区"):
            city_name = "大田区"
        elif(value[0] == "鎌倉市"):
            city_name = "神奈川県 市部"
        else:
            city_name = value[0]

        return city_name

#京浜東北線駅情報

stations = {
"omiya" : [35.906295,139.623999],
"saitama_sintosin" : [35.893867,139.633587],
"yono" : [35.884393,139.639085],
"kita_urawa" : [35.872156,139.646196],
"urawa" :  [35.858482,139.657087],
"minami_urawa" : [35.847681,139.66915],
"maki" : [35.828148,139.690443], # 牧志 -> 川口市
"nishi_kawaguchi" : [35.815725,139.704364],
"kawaguchi" : [35.801922,139.717583],
"akabane" : [35.778051,139.720856], # 北区 -> 東京都
"higashi_jujo" : [35.762947,139.727694],
"ouji" : [35.752474,139.738139],
"uenakazato" : [35.746586,139.746927],
"tabata" : [35.738062,139.76086],
"nishi_nippori" : [35.732135,139.766787], # 荒川区 -> 足立区
"nippori" : [35.727772,139.770987],
"uguisudani" : [35.720495,139.778837], # 台東区 -> 東京都
"ueno" : [35.713768,139.777254],
"okachimachi" : [35.707893,139.774332],
"akihabara": [35.698683,139.774219],
"kanda": [35.69169,139.770883],
"tokyo" : [35.681382,139.766084],
"yuurakucho" : [35.675069,139.763328],
"shinbashi" : [35.665498,139.75964],
"hamamatsucho" : [35.655646,139.756749],
"tamachi" : [35.645736,139.747575],
"shinagawa" : [35.630152,139.74044],
"ooicho" : [35.606249,139.734855],
"omori" : [35.588442,139.727929],
"kamata" : [35.562479,139.716051],
"kawasaki" : [35.531328,139.696899],
"tsurumi" : [35.508565,139.676018],
"shinkoyasu" : [35.487106,139.65554],
"higashi_kanagawa" : [35.477951,139.633347],
"yokohama" : [35.466188,139.622715],
"sakuragicho" : [35.450918,139.631073],
"kannnai" : [35.443233,139.637134],
"ishikawa_cho" : [35.438247,139.643151],
"yamate" : [35.427249,139.646206],
"negishi" : [35.415795,139.635057],
"tubuteshi" : [35.399881,139.617916],
"shinsugita" : [35.385877,139.620533],
"youkoudai" : [35.378713,139.596505],
"kounandai" : [35.37528,139.576712],
"hongoudai" : [35.367436,139.550281],
"oofune" : [35.353435,139.531124],
}

a = CoordinateChanger()
b = a.get_city_name(stations["omiya"])

keys = stations.keys()
for key in keys:
    b = a.get_city_name(stations[key])
    print("{}: {}".format(key, b))
#print(b)

