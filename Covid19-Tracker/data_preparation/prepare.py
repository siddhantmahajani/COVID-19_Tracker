"""
Author: Siddhant Mahajani
Program: prepare.py
Description: This program is to prepare state wise distribution of covid cases in India
Date: 8th Feb 2022
"""

import requests
import pandas
import warnings

warnings.filterwarnings("ignore")

DATA_URL = "https://api.covid19india.org/state_district_wise.json"


def getData():
    data = ((requests.get(DATA_URL)).json())
    return data


def getStates(data):
    states = []
    for key in data.items():
        state = key[0]
        states.append(state)

    return states


def getPreparedData(selected_state, selected_district):
    data = getData()
    states = getStates(data)
    tc = []
    dis = []
    act, con, dec, rec = 0, 0, 0, 0
    for state in states:
        if state == selected_state:
            for key in (data[state]['districtData']).items():
                district = key[0]
                if district == selected_district:
                    dis.append(district)
                    active = data[state]['districtData'][district]['active']
                    confirmed = data[state]['districtData'][district]['confirmed']
                    deceased = data[state]['districtData'][district]['deceased']
                    recovered = data[state]['districtData'][district]['recovered']
                    if district == 'Unknown':
                        active, confirmed, deceased, recovered = 0, 0, 0, 0
                    tc.append([active, confirmed, deceased, recovered])
                    act = act + active
                    con = con + confirmed
                    dec = dec + deceased
                    rec = rec + recovered

            tc.append([act, con, dec, rec])
            dis.append('Total')

    df = pandas.DataFrame({
        'Status': ['Active', 'Confirmed', 'Deceased', 'Recovered'],
        'Number of cases': (act, con, dec, rec)
    })
    return df
