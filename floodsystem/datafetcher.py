import datetime
import json
import os
import dateutil.parser
import requests


def fetch(url):
    r = requests.get(url)
    data = r.json()
    return data


def dump(data, filename):
    file = open(filename, 'w')
    json.dump(data, file)
    file.close()


def load(filename):
    file = open(filename, 'r')
    data = json.load(file)
    file.close()
    return data


def fetch_station_data(use_cache=True):

    url = "http://environment.data.gov.uk/flood-monitoring/id/stations?status=Active&parameter=level&qualifier=Stage" \
          "&_view=full "
    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except FileExistsError:
        pass
    cache_file = os.path.join(sub_dir, 'station_data.json')

    if use_cache:
        try:
            data = load(cache_file)
        except FileNotFoundError:
            data = fetch(url)
            dump(data, cache_file)
    else:
        data = fetch(url)
        dump(data, cache_file)

    return data


def fetch_latest_water_level_data(use_cache=False):

    url = "http://environment.data.gov.uk/flood-monitoring/id/measures?parameter=level&qualifier=Stage&qualifier=level"  # noqa
    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except FileExistsError:
        pass
    cache_file = os.path.join(sub_dir, 'level_data.json')

    if use_cache:
        try:
            data = load(cache_file)
        except FileNotFoundError:
            data = fetch(url)
            dump(data, cache_file)
    else:
        data = fetch(url)
        dump(data, cache_file)

    return data


def fetch_measure_levels(measure_id, dt):

    now = datetime.datetime.utcnow()
    start = now - dt

    url_base = measure_id
    url_options = "/readings/?_sorted&since=" + start.isoformat() + 'Z'
    url = url_base + url_options

    data = fetch(url)
    dates, levels = [], []
    for measure in data['items']:
        d = dateutil.parser.parse(measure['dateTime'])

        dates.append(d)
        levels.append(measure['value'])

    return dates, levels
