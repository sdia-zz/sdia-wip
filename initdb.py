#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from datetime import timedelta
from settings import DBCONN, CITIES, SEASONS, DATES_AVAILABLE


DDL = [
    'DROP TABLE IF EXISTS cities;',
    '''
    CREATE TABLE cities (
        name TEXT PRIMARY KEY,
        lat  REAL NOT NULL,
        lon  REAL NOT NULL
    );
    ''',

    'DROP TABLE IF EXISTS dates;',
    '''
    CREATE TABLE dates (
        date DATE PRIMARY KEY,
        season TEXT
    );''',

    'DROP TABLE IF EXISTS temperatures;',
    '''
    CREATE TABLE temperatures (
        city_name TEXT,
        date DATE,
        temp_min REAL NOT NULL,
        temp_max REAL NOT NULL,
        PRIMARY KEY (city_name, date)
    );'''
]


DML_INSERT_CITIES = '''INSERT INTO cities (name, lat, lon) VALUES (?, ?, ?);'''
DML_INSERT_DATES = '''INSERT INTO dates (date, season) VALUES (?, ?)'''


def update_cities():
    with DBCONN as con:
        for cmd in DDL:
            con.execute(cmd)
        for city in CITIES:
            con.execute(DML_INSERT_CITIES, (city['name'], city['lat'], city['lon']))



def get_season(d):
    '''Takes a date object and returns the season'''

    s = d.strftime('%m-%d')
    for season in SEASONS:
        if season['start'] <= s and season['end'] >= s:
            return season['name']


def update_dates():
    date = DATES_AVAILABLE[0]
    cur = DBCONN.cursor()
    while date <= DATES_AVAILABLE[1]:
        season = get_season(date)
        cur.execute(DML_INSERT_DATES, (date, season))
        date += timedelta(days=1)

    DBCONN.commit()







if __name__ == '__main__':
    update_cities()
    update_dates()
