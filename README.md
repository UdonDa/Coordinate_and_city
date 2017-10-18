# Coordinate_and_city
## 概要
緯度経度 -> 市町村  
市町村 -> 緯度経度  

## 仕様技術
[GoogleGeocofingAPI](https://developers.google.com/maps/documentation/geocoding/intro?hl=ja)
[農研機構ジオコーディングサービス](https://www.finds.jp/rgeocode/index.html.ja)

## 環境
Python 3.6.2  

## 使い方
#### coordinate_to_city.py
\# 農研機構  
get_city(lat,lng)で、lat,lngの位置の区、市町村名を取得

