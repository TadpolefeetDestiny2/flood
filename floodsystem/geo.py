from haversine import haversine
from floodsystem.utils import sorted_by_key


def stations_by_distance(stations, p):
    tuple_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        distance_tuple = (station.name, station.town, distance)
        tuple_list.append(distance_tuple)
    sorted_list = sorted_by_key(tuple_list, 2)
    return sorted_list[:10], "\n", sorted_list[-10:]


def stations_within_radius(stations, centre, r):
    radius_stations = []
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
            radius_stations.append(station.name)
    return sorted(radius_stations)


def rivers_with_stations(stations):
    rivers = []
    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)
    return rivers


def stations_by_river(stations):
    rivers = rivers_with_stations(stations)
    river_dict = {}
    for river in rivers:
        station_list = []
        for station in stations:
            if station.river == river:
                station_list.append(station)
        river_dict[river] = station_list
    return river_dict


def rivers_by_station_number(stations, n):
    river_dict = stations_by_river(stations)
    river_tuples_list = []
    for river in river_dict:
        river_tuple = (river, len(river_dict[river]))
        river_tuples_list.append(river_tuple)
    sorted_river_tuples_list = sorted_by_key(river_tuples_list, 1, True)
    while sorted_river_tuples_list[n][1] == sorted_river_tuples_list[n - 1][1]:
        n = n + 1
    return sorted_river_tuples_list[:n]
