from floodsystem.stationdata import *
from floodsystem.station import *
from floodsystem.utils import *

def stations_level_over_threshold(stations, tol):
    stations_over_tol = []
    for station in stations:
        rel = relative_water_level(station)
        if type(rel) == float and rel > tol:
            stations_over_tol.append((station, rel))
    return sorted_by_key(stations_over_tol, 1, True)

def stations_highest_rel_level(stations, N):
    all_valid_stations = stations_level_over_threshold(stations, -100)[:N]
    temp_list = []
    for station in all_valid_stations:
        temp_list.append(station[0])
    return temp_list
