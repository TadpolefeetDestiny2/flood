from floodsystem.utils import *
from floodsystem.flood import *

def run():

    stations = build_station_list()

    update_water_levels(stations)
    for station in stations:
        if station.name == "Whitchurch Main":
            print(station, relative_water_level(station))
    stations_over_tol = stations_level_over_threshold(stations, 0.8)
    for item in stations_over_tol:

        print(item[0].name, item[1])



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
