from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    print(f'Number of stations: {len(stations)}')
    for station in stations:
        if station.name in ['Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge']:
            print(station)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
