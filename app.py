# Running the app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash
from dash import dcc
from dash import html
import plotly.express as px 
import pandas as pd 

DATA_PATH  = "./pink_morsel_sales.csv"
data = pd.read_csv(DATA_PATH)

#conversion of date to datetime and sort
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values(by="date")

#visualizing overall sales

data_total = data.groupby("date")["sales"].sum().reset_index()

#using plotly to generate the line chart on the sales 

fig = px.line(data_total, x="date", y="sales", title="Pink Morsel Sales Over Time Period")

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales ($)"
)

fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
fig.add_annotation(
    x="2021-01-15",
    y=0.95,
    yref="paper",
    text="Price Increase",
    showarrow=True,
    arrowhead=1
)

#initializing the app
app = Dash(__name__)

app.layout = html.Div(style={'textAlign': 'center', 'fontFamily': 'Arial'}, children=[
    html.H1(
        children="Pink Morsel Sales Visualizer for Soul Foods",
        style={'color': '#08519a', 'marginTop': '40px'}
    ),
    html.Div(children='''
        Tracking sales data before and after the January 15th, 2021 price increase.
    ''', style={'marginBottom': '20px'}),
     
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)