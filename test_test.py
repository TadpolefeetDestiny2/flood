from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    stations = build_station_list()
    a = rivers_with_stations(stations)
    assert type(a) == list

    b = stations_by_river(stations)
    assert type(b) == dict
    assert len(a) == len(b)
    for key in b:
        object1 = b[key]
        assert type(object1) == list

run()
print("Test ran succesfully")