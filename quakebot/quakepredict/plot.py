import plotly.express as px
import plotly.io as pio
import pandas as pd

def create_plot(geo_data):
    fig = px.scatter_mapbox(
        geo_data,
        lat='Latitude',
        lon='Longitude',
        color='Magnitude',
        size='Depth (km)',
        hover_name='Region',
        hover_data={
            'date_time': True,
            'Depth (km)': True,
            'Latitude': True,
            'Longitude': True
        },
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=40,
        zoom=1,
        title='',
        animation_frame=geo_data['date_time'].dt.year
    )

    fig.update_layout(
        mapbox_style="carto-positron",
        title_x=0.5,
        margin={"r":0,"t":40,"l":0,"b":0},
        coloraxis_colorbar=dict(
            title="Magnitude",
            thicknessmode="pixels",
            thickness=10,
            lenmode="pixels",
            len=300,
            yanchor="middle",
            y=0.5,
            ticks="outside",
            ticksuffix=" Richter"
        ),
        updatemenus=[{
            'buttons': [
                {
                    'label': 'Play',
                    'method': 'animate',
                    'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                },
                {
                    'label': 'Pause',
                    'method': 'animate',
                    'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}]
                }
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': False,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top'
        }]
    )

    return pio.to_html(fig, full_html=False)