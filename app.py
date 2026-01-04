# Running the app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import callback
import plotly.express as px 
import pandas as pd 

DATA_PATH  = "./pink_morsel_sales.csv"
data = pd.read_csv(DATA_PATH)

#conversion of date to datetime and sort
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values(by="date")

# Price increase date for reference line
PRICE_INCREASE_DATE = '2021-01-15'

# Initialize the Dash app
app = Dash(__name__)

# Define custom CSS styles
app.layout = html.Div(
    style={
        'backgroundColor': '#f8f9fa',
        'fontFamily': 'Arial, sans-serif',
        'padding': '40px',
        'maxWidth': '1200px',
        'margin': '0 auto',
        'boxShadow': '0 4px 12px rgba(0,0,0,0.1)',
        'borderRadius': '12px'
    },
    children=[
        html.H1(
            "Soul Foods - Pink Morsel Sales Dashboard",
            style={
                'textAlign': 'center',
                'color': "#095097",
                'marginBottom': '30px',
                'fontWeight': 'bold',
                'fontSize': '36px'
            }
        ),

        html.Div(
            style={
                'textAlign': 'center',
                'marginBottom': '40px',
                'backgroundColor': '#ffffff',
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.05)'
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={'fontSize': '20px', 'fontWeight': 'bold', 'color': "#095097", 'marginRight': '20px'}
                ),
                dcc.RadioItems(
                    id='region-radio',
                    options=[
                        {'label': ' All Regions', 'value': 'all'},
                        {'label': ' North', 'value': 'north'},
                        {'label': ' South', 'value': 'south'},
                        {'label': ' East', 'value': 'east'},
                        {'label': ' West', 'value': 'west'}
                    ],
                    value='all',
                    inline=True,
                    style={'fontSize': '18px'}
                )
            ]
        ),

        dcc.Graph(id='sales-line-chart')
    ]
)

# Callback to update the chart based on selected region
@callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        plot_data = data.groupby('date')['sales'].sum().reset_index()
        title = 'Total Pink Morsel Sales Across All Regions'
        line_color = '#3498db'
    else:
        plot_data = data[data['region'] == selected_region]
        title = f'Pink Morsel Sales - {selected_region.capitalize()} Region'
        # Different colors for each region to make them distinct
        colors = {'north': "#c3c30f", 'south': '#2ecc71', 'east': "#1dc7e9", 'west': '#9b59b6'}
        line_color = colors.get(selected_region, '#3498db')

    fig = px.line(
        plot_data,
        x='date',
        y='sales',
        title=title,
        color_discrete_sequence=[line_color]
    )

    # Styling the figure
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Daily Sales ($)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=14),
        hovermode='x unified',
        title_x=0.5,  # Center title
        title_font_size=24
    )

    # Add vertical line and annotation for price increase
    fig.add_vline(
        x=PRICE_INCREASE_DATE,
        line_dash="dash",
        line_color="red",
        line_width=2
    )
    fig.add_annotation(
        x=PRICE_INCREASE_DATE,
        y=0.95,
        yref='paper',
        text="Price Increase →",
        showarrow=True,
        arrowhead=2,
        arrowcolor="red",
        font=dict(color="red", size=14)
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)