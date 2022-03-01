from floodsystem.flood import *


def run():
    stations = build_station_list()
    update_water_levels(stations)
    riskiest_stations = (stations_highest_rel_level(stations, 10))
    for station in riskiest_stations:
        print(station.name, relative_water_level(station))
        assert type(station.name) == str
        assert type(relative_water_level(station)) == float

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
