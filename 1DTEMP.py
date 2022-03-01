from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    stations = build_station_list()
    for i in rivers_with_stations(stations):
        print(i)

    print(stations_by_river(stations))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
