import dash 
import dash_bootstrap_components as dbc
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
from dash import dcc, html, Input, Output, State
from flask import Flask
from dash_bootstrap_components._components.Container import Container
import dash_cytoscape as cyto
import plotly.figure_factory as ff



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

user_input = html.Div(
    [
        dbc.Label("Correo:", html_for="example-usur"),
        dbc.Input(type="email", id="example-user", placeholder="Ingrese su E-mail"),
        
    ],
    className="mb-3",
)

password_input = html.Div(
    [
        dbc.Label("Contraseña:", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Ingrese su contraseña",
        ),
        
    ],
    className="mb-3",
)

form = dbc.Form([user_input, password_input])

card = dbc.Card(
    [
        dbc.CardImg(src="https://i.ibb.co/FHvf9h5/intelicorp.png", top=True),
        dbc.CardBody(
            [
                html.H4("Iniciar sesion ", className="card-title text-center"),
                html.Div(form),
                dbc.Button("Iniciar Sesión", color="primary", className="m-auto d-flex justify-content-center", href="/Home"),
            ]
        ),
    ],
    style={"width": "45rem", "margin-top": "80px"},
)

centered_card = dbc.Row(
    dbc.Col(
        card,
        width={"size": 9, "offset": 3}  # Ajusta el ancho y la posición del card
    ),
    justify="center",  # Centra el card horizontalmente
)


app.layout = dbc.Container([
    html.Div(
        style={
            'background-image': 'url("/assets/fonfo.jpg")',
            'background-repeat': 'no-repeat',
            'background-size': 'cover',
            'background-position': 'center',
            'height': '100vh',
            'width': '100vw',  # Ajusta el ancho del contenedor al 100% de la ventana
            'position': 'fixed',
            'top': 0,
            'left': 0
        },
        children=[
            dbc.Form([
               dbc.Container([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content"), centered_card
])
            ])
        ]
    )
])

'''@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def display_page(pathname):
    if pathname == "/Registro":
        from registro import pantalla_de_registro
        return pantalla_de_registro()
    else:
        return centered_card'''

if __name__ == "__main__":
    app.run_server(debug=True)
