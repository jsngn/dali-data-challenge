# Author: Mien Nguyen
# Date: 05/03/2019
# Purpose: Create a bubble chart showing the effect of affiliation status on the alcohol consumption and dinner
# participation habits that result in low stress levels (data visualization for DALI's Data Challenge)

import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd

# Gets the file with the data
dali_info = pd.read_json('DALI_Data-Anon.json')

# Scales the bubbles' size
MAX_MARKER_SIZE = 400
sizeref = 10 * max(dali_info['stressed']) / MAX_MARKER_SIZE

# Creates trace for affiliated data set
data_affiliated = [go.Scatter(
    x=dali_info['alcoholDrinksPerWeek'][dali_info['affiliated'] == 1],  # Number of drinks on the x axis
    y=dali_info['socialDinnerPerWeek'][dali_info['affiliated'] == 1],  # Number of dinners on the y axis
    name='Affiliated',  # Displays 'Affiliated' in legend
    hoverinfo='text',
    text=dali_info['stressed'][dali_info['affiliated'] == 1],  # Displays stress level in hover text
    mode='markers',  # Displays data as a bubble chart
    marker=dict(
                opacity=0.5,  # Sets opacity of bubbles
                color='rgb(114, 21, 214)',  # Sets color of bubbles to purple
                size=dali_info['stressed'][dali_info['affiliated'] == 1],  # Visualize stress data using bubble size
                sizeref=sizeref  # Scales bubbles' size
                )
)
]

# Creates trace for unaffiliated data set
data_unaffiliated = [go.Scatter(
    x=dali_info['alcoholDrinksPerWeek'][dali_info['affiliated'] == 0],  # Number of drinks on the x axis
    y=dali_info['socialDinnerPerWeek'][dali_info['affiliated'] == 0],  # Number of dinners on the y axis
    name='Unaffiliated',  # Displays 'Unaffiliated' in legend
    hoverinfo='text',
    text=dali_info['stressed'][dali_info['affiliated'] == 0],  # Displays stress level in hover text
    mode='markers',  # Displays data as a bubble chart
    marker=dict(
                opacity=0.5,  # Sets opacity of bubbles
                color='rgb(0, 175, 96)',  # Sets color of bubbles to green
                size=dali_info['stressed'][dali_info['affiliated'] == 0],  # Visualize stress data using bubble size
                sizeref=sizeref  # Scales bubbles' size
                )
)
]

# Determines layout of chart
layout = go.Layout(
    # Displays title (bold), subtitle, explanation of bubbles' size & hover text (italics) at top left
    title=go.layout.Title(
        text='<b>'
             'Affiliation impacts the emotionally optimal level of alcohol consumption and social dinner participation.'
             '</b>'
             '<br>'
             'Low-stress unaffiliated students consume 0-4 drinks and 0-1 dinner weekly; the numbers rise to 2-8 and 4-6 for low-stress affiliated students.'
             '<br>'
             '<i>'
             'Bubble size and hover text indicate the stress level.'
             '</i>'
             '</br>',
        xref='paper',
        x=0,
        font=dict(size=14)  # Sets font size of this text to 14
        ),
    xaxis=dict(title='Number of Alcohol Drinks Per Week'),  # x axis label
    yaxis=dict(title='Number of Social Dinners Per Week'),  # y axis label
    hovermode='closest',  # Displays hover text for the exact bubble the mouse hovers over
)

# Packs data
data_plotted = data_affiliated + data_unaffiliated

# Plots data and creates chart
fig = go.Figure(data=data_plotted, layout=layout)
ply.plot(fig, filename='DALI_plot.html')
