"""
Author: Siddhant Mahajani
Program: filters.py
Description: This program is to prepare filters for selection of data for graphs of covid cases in India
Date: 8th Feb 2022
"""

import warnings

warnings.filterwarnings("ignore")


def getFilters(data, states):
    filters = []

    for state in states:
        dis = []
        for dist in (data[state]['districtData']).items():
            district = dist[0]
            dis.append(district)

        state_dict = {"State": state, "Districts": dis}
        filters.append(state_dict)

    return filters
