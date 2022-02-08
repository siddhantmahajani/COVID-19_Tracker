# Covid19-Tracker
A simple state - district wise covid cases tracker using streamlit

The program is to display state wise cases of covid in India. The application is a web based application and the input is State and district which is to be selected from drill-down. The output will be a a bar chart to display total number of cases i.e. Active, Confirmed, Deceased, and Recovered. 

Libraries used:<br/>
1. streamlit: Library used to create a web based application using streamlit. The library is used to host the application on local host and provide a UI to the application.<br/>
2. plotly: Library used to display graphical visualisation of the data as output.<br/>
3. requests: Library to used to fetch data from URL.<br/>
4. pandas: Library used to convert the json data into data frame which is then passed to the graphical library to plot it on a graph.<br/>

Dataset:<br/>
The data set is fetched from https://api.covid19india.org/state_district_wise.json as it returns a json response.

Code:<br/>
1. application.py: This is the main program which is to be executed. This program will host the application on the local host and provide a UI to display output of the application.<br/>
2. prepare.py: This program is used to fetch the data, fetch the states, and prepare data in appropriate format for the analysis and visualisation.<br/>
3. filters.py: This program is used to fetch the filters that are to be provided as input to the code. The filters include States and Districts of the selected states.<br/>