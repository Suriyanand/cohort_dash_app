#!/usr/bin/env python
# coding: utf-8

# In[10]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
df = pd.read_csv(r"D:\Development\vs.code\Data Science\data Analaytis\study problems\datasets\cohorts.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df["Week"] = df["Date"].dt.isocalendar().week
avg_weekly_data = df.groupby('Week').agg({
    "New users":'mean',
    "Returning users":'mean',
    "Duration Day 1":'mean',
    "Duration Day 7":'mean'
}).reset_index()



fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df['Date'], y=df['New users'], mode='lines+markers', name='New Users'))
fig1.add_trace(go.Scatter(x=df['Date'], y=df['Returning users'], mode='lines+markers', name='Returning Users'))
fig1.update_layout(title='Trend of New and Returning Users Over Time',
                  xaxis_title='Date',
                  yaxis_title='Number of Users')

fig2 = px.line(data_frame = df, x = "Date", y = ["Duration Day 1","Duration Day 7"], markers = True,labels = {"distribution":"values"})
fig2.update_layout(title = "identify trends and duration between 1 to 7 days", xaxis_title = "Date" , yaxis_title = "Duration")

fig3 = px.line(data_frame = avg_weekly_data, x = "Week", y = ["New users","Returning users"], markers = True)
fig3.update_layout(title = "avg between the new users and returning users",
                 xaxis_title = "Number of users",yaxis_title = "Weak of the year")

fig4 = px.line(data_frame = avg_weekly_data, x = "Week", y = ["Duration Day 1","Duration Day 7"], markers = True)
fig4.update_layout(title = "avg between the Duration day 1 and Duration day 7",
                 xaxis_title = "Number of users",yaxis_title = "Weak of the year")
# Define dropdown options
dropdown_options = [
    {'label': 'Trend of New and Returning Users Over Time', 'value': 'plot1'},
    {'label': 'identify trends and duration between 1 to 7 days', 'value': 'plot2'},
    {'label': 'avg between the new users and returning users', 'value': 'plot3'},
    {'label': 'avg between the Duration day 1 and Duration day 7', 'value': 'plot4'},

    
]

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Dashboard'),

    # Dropdown menu
    dcc.Dropdown(
        id='plot-dropdown',
        options=dropdown_options,
        value='plot1'  # Default value
    ),

    # Div to hold the selected plot
    html.Div(id='plot-container'),

])

# Callback to update the selected plot based on dropdown value
@app.callback(
    Output('plot-container', 'children'),
    [Input('plot-dropdown', 'value')]
)
def update_plot(selected_plot):
    if selected_plot == 'plot1':
        return dcc.Graph(id='graph1', figure=fig1) 
    # Plot 1
    elif selected_plot == 'plot2':
        return dcc.Graph(id='graph2', figure=fig2)
    
    elif selected_plot == 'plot3':
        return dcc.Graph(id='graph3', figure=fig3)
    elif selected_plot == 'plot4':
        return dcc.Graph(id='graph4', figure=fig4)
    # Plot 2
    # Add more elif statements for additional plots

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=8090)


# In[ ]:





# In[ ]:




