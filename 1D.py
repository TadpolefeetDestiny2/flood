from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    stations = build_station_list()
    print(sorted(rivers_with_stations(stations))[:10], '\n')
    river_list = ['River Aire', 'River Cam', 'River Thames']
    river_dict = stations_by_river(stations)
    for river in river_dict:
        if river in river_list:
            station_list = []
            for item in river_dict[river]:
                station_list.append(item.name)
            print(river, sorted(station_list), '\n')


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
