from floodsystem.utils import *
from floodsystem.flood import *

def run():

    stations = build_station_list()

    update_water_levels(stations)
    stations_over_tol = stations_level_over_threshold(stations, 0.8)
    assert stations_over_tol == sorted_by_key(stations_over_tol, 1, True)
    for item in stations_over_tol:
        assert type(item) == tuple
        assert type(item[0]) == MonitoringStation
        assert type(item[1]) == float

run()

