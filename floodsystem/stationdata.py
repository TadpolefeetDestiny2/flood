from floodsystem.datafetcher import *
from floodsystem.station import MonitoringStation


def build_station_list(use_cache=True):
    data = fetch_station_data(use_cache)
    # Build list of MonitoringStation objects
    stations = []
    for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']

        # Extract river name (not always available)
        river = None
        if 'riverName' in e:
            river = e['riverName']

        # Attempt to extract typical range (low, high)
        try:
            typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))
        except Exception:
            typical_range = None

        try:
            # Create measure station object if all required data is
            # available, and add to list
            s = MonitoringStation(
                station_id=e['@id'],
                measure_id=e['measures'][-1]['@id'],
                label=e['label'],
                coord=(float(e['lat']), float(e['long'])),
                typical_range=typical_range,
                river=river,
                town=town)
            stations.append(s)
        except Exception:
            # Not all required data on the station was available, so
            # skip over
            pass

    return stations


def update_water_levels(stations):
    """Attach level data contained in measure_data to stations"""

    # Fetch level data
    measure_data = fetch_latest_water_level_data()

    # Build map from measure id to latest reading (value)
    measure_id_to_value = dict()
    for measure in measure_data['items']:
        if 'latestReading' in measure:
            latest_reading = measure['latestReading']
            measure_id = latest_reading['measure']
            measure_id_to_value[measure_id] = latest_reading['value']

    # Attach latest reading to station objects
    for station in stations:

        # Reset latest level
        station.latest_level = None

        # Attach new level data (if available)
        if station.measure_id in measure_id_to_value:
            if isinstance(measure_id_to_value[station.measure_id], float):
                station.latest_level = measure_id_to_value[station.measure_id]