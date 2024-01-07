from src.utils import import_config, import_data
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


config = import_config("configs/config.yml")

LOCATION = config["Path"]["Abidjan"]

data = import_data(LOCATION)

app = dash.Dash("Transport à Abidjan")


fig = px.scatter_mapbox(
    data,
    lat=data.geometry.centroid.y,
    lon=data.geometry.centroid.x,
    hover_name="name",
    color_discrete_sequence=["red"],
    zoom=3,
    height=300,
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


app.layout = html.Div(
    [html.H1("Transport à Abidjan"), html.P("Visualisation des données de transport à Abidjan"), dcc.Graph(figure=fig)]
)

if __name__ == "__main__":
    app.run_server(debug=True)
