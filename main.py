#!/usr/bin/env python3
#-*- coding:utf-8 -*-



import calendar
from datetime import datetime

import requests



from settings import DBCONN

## https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]



URL_REQUEST = 'https://api.darksky.net/forecast/{secret_key}/{lat},{lon},{utime}'
SECRET_KEY = 'ceeee8549ff8e93e9cc0da349a201a74'


def get_city_location(name):
    '''Given a city's name, returns the tuple (latitude, longitude)
       when the city exists, raises an exception otherwise.'''

    cur = DBCONN.cursor()
    cur.execute('select lat, lon from cities where name = (?)', (name,))
    res = cur.fetchone()

    if res:
        return (res[0], res[1])
    raise Exception('City %s not found, please update the city configuration and run an update' % name)


def date_to_unix_time(d):
    '''Given a date object returns unix time in UTC'''
    return int(calendar.timegm(d.timetuple()))


def get_city_temperature(name, date):
    '''Given a city's name and date, returns temperature
       when the city exists, raises an exception otherwise.'''

    lat, lon = get_city_location(name)
    utime = date_to_unix_time(date)
    url_request = URL_REQUEST.format(secret_key=SECRET_KEY, lat=lat, lon=lon, utime=utime)
    print(url_request)

    r = requests.get(url_request)
    r.raise_for_status()
    resp = r.json()
    print(resp['daily']['data'][0]['temperatureMin'], resp['daily']['data'][0]['temperatureMax'])


if __name__ == '__main__':
    print('Berlin ', get_city_location('berlin'))
    print('Delhi ', get_city_location('delhi'))
    # print('Dakar ', get_city_location('dakar'))

    get_city_temperature('berlin', datetime(2018,1,1))
    get_city_temperature('delhi', datetime(2018,1,1))
    get_city_temperature('dakar', datetime(2018,1,1))
