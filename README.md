# Coordinate_and_city
## 概要
緯度経度 -> 市町村  
市町村 -> 緯度経度  

## 仕様技術
[GoogleGeocofingAPI](https://developers.google.com/maps/documentation/geocoding/intro?hl=ja)


## 環境
Python 3.6.2  

## 使い方
#### coordinate_to_city.py
coordinateChanger = CoordinateChanger()
b = a.get_address("緯度", "経度")
(b = ○○市○町)

