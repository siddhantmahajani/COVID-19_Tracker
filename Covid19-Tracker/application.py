"""
Author: Siddhant Mahajani
Program: app.py
Description: Web application to perform track covid cases in India using streamlit
Date: 04/09/2024
"""

import streamlit as st
import plotly.express as px
from data_preparation import prepare
from filter_preparation import filters
import warnings

warnings.filterwarnings('ignore')

data = prepare.getData()
states = prepare.getStates(data)
filters = filters.getFilters(data, states)

selected_state = st.sidebar.selectbox('Select State', states)
districts = []

for data in filters:
    if data['State'] == selected_state:
        districts = data['Districts']

selected_district = st.sidebar.selectbox('Select District', districts)

updatedData = prepare.getPreparedData(selected_state, selected_district)

if st.sidebar.checkbox("Show state analysis", True, key=2):
    st.markdown("## **State - District wise distribution of COVID cases**")
    st.markdown("### Overall Active, Confirmed, Deceased and " +
                "Recovered cases in state %s and district %s yet" % (selected_state, selected_district))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
            updatedData,
            x='Status',
            y='Number of cases',
            labels={
                'Number of cases': 'Number of cases in state %s and district %s' % (selected_state, selected_district)},
            color='Status')
        st.plotly_chart(state_total_graph)
