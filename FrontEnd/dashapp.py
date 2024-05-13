import os
import dash
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, Output, Input, dcc
from django.db.models import Q
from plotly.subplots import make_subplots

# Initialize the Dash app (note: running the Dash app is not possible in this environment)
app = dash.Dash(__name__)

# Data to be displayed in the table
data = {
    'Player': ['A', 'B', 'C'],
    'Points': ['20', '30', '8']
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)


def generate_table(dataframe):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(len(dataframe))
        ])
    ])


# Set the layout of the Dash app
app.layout = html.Div(children=[generate_table(df)])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
