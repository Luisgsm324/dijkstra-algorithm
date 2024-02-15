import json

data = open("assets/stations.json", mode="r", encoding="utf8")
data = json.load(data)

def take_station(station): return data["stations"][station]

def take_stations(): return data["stations"]