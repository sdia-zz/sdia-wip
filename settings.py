#!/usr/bin/env python3
#-*- coding:utf-8 -*-




import os
import sqlite3
from datetime import datetime


DBCONN = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sample.db'))

CITIES = [dict(name='berlin',   lat=52.5200, lon=13.4050),
          dict(name='paris',    lat=48.8566, lon=2.3522),
          dict(name='tokyo',    lat=35.6895, lon=139.6917),
          dict(name='delhi',    lat=28.7041, lon=77.1025),
          dict(name='shanghai', lat=31.2304, lon=121.4737),
]

SEASONS = [dict(name='spring', start='03-21', end='06-20'),
           dict(name='summer', start='06-21', end='09-20'),
           dict(name='autumn', start='09-21', end='12-20'),
           dict(name='winter', start='12-21', end='12-31'),
           dict(name='winter', start='01-01', end='03-20'),
]

DATES_AVAILABLE = (datetime(2017,1,1), datetime(2020, 12, 31))
