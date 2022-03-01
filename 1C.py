from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    radius = 10
    print(stations_within_radius(stations, centre, radius))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
