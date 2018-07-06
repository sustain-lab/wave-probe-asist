#!/usr/bin/env python3

import dash
import dash_core_components as dcc
import dash_html_components as html

from wave_probe_asist.data import load_data

# load data from a single file
time, elevation = load_data()

app = dash.Dash()

# html elements
header = html.H1(children='wave-probe-asist')
div = html.Div(children='Wave probe data from ASIST')

# prepare data
data = {
    'x': time,
    'y': elevation,
    'type': 'line',
    'name': 'deep'
    }

graph = dcc.Graph(id='wave-probe-graph',
                  figure={
                      'data': [data],
                      'layout': {'title': 'ASIST wave probe example'}
                  }
        )

app.layout = html.Div(children=[header, div, graph])

if __name__ == '__main__':
    app.run_server(debug=True)
