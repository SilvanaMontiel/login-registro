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

user_input = html.Div(
    [
        dbc.Label("Usuario:", html_for="example-user"),
        dbc.Input(type="user", id="example-user", placeholder="Ingrese un usuario"),
        
    ],
    className="mb-3",
)

password_input = html.Div(
    [
        dbc.Label("Contraseña:", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Ingrese una contraseña",
    
        ),
        
    ],
    className="mb-3",
)

confirm_password_input = html.Div(
    [
        dbc.Label("Confirme su contraseña:", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Ingrese una contraseña nuevamente",
    
        ),
        
    ],
    className="mb-3",
)

form = dbc.Form([user_input, password_input,confirm_password_input])

card_registro = dbc.Card(
    [
        dbc.CardImg(src="https://i.ibb.co/FHvf9h5/intelicorp.png", top=True),
        dbc.CardBody(
            [
                html.H4("Registro de Usuario ", className="card-title text-center"),
                html.Div(form),
                dbc.Button("Registrarse", color="primary", className="m-auto d-flex justify-content-center", href="/Home"),
                dbc.CardLink("Iniciar Sesión", href="/login.py", className="text-center d-flex justify-content-end mt-3 ml-auto"),
            ]
        ),
    ],
    style={"width": "45rem", "margin-top": "50px"},
)

centered_card_registro = dbc.Row(
    dbc.Col(
        card_registro,
        width={"size": 9, "offset": 3}  # Ajusta el ancho y la posición del card
    ),
    justify="center",  # Centra el card horizontalmente
)

def pantalla_de_registro():
    return html.Div([
        centered_card_registro
    ])