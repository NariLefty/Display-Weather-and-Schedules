# -*- coding: utf-8 -*-
import urllib.request as req
import json

# jma : Japan Meteorological Agency

def get_weathers():
    """get_weathers method.
    Get weather, date, time, temp and precip.
    """
    # https://www.jma.go.jp/bosai/forecast/data/forecast/(pathCode).json
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'
    filename = 'tenki.json'

    # Download
    req.urlretrieve(url, filename)

    # Load json file
    json_open = open("./tenki.json", "r")
    json_load = json.load(json_open)

    # Get temp and precip from json file
    temp = json_load[1]["tempAverage"]["areas"][0]
    precip = json_load[1]["precipAverage"]["areas"][0]

    # Get weather , date and time from json file
    weather = json_load[0]["timeSeries"][0]["areas"][0]["weathers"][0].split("\u3000")[0]
    date, time = json_load[0]["timeSeries"][0]["timeDefines"][0].split("+")[0].split("T")
    date = date.split("-")[1:] 
    time2 = time.split(":")[0] + ":" + time.split(":")[1]

    return weather, date, time2, temp, precip