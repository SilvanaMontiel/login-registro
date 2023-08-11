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
from pantallas import gestion_del_servicio, ciclo_Evaluacion_Web, postura_de_seguridad_web, top_vulnerabilidades_web,top_Riesgo_web,top_Mitre_web, top_Top10OWASP_Web, recomendacion_Mitigacion_Web, ciclo_Evaluacion_Movil, postura_de_seguridad_Movil, top_vulnerabilidades_Movil,top_Riesgo_Movil,top_Mitre_Movil, top_Top10OWASP_Movil, recomendacion_Mitigacion_Movil, ciclo_Evaluacion_Apis, postura_de_seguridad_Apis, top_vulnerabilidades_Apis,top_Riesgo_Apis, top_Mitre_Apis, top_Top10OWASP_Apis, recomendacion_Mitigacion_Apis, ciclo_Evaluacion_DDBB, postura_de_seguridad_DDBB

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

logo = "https://i.ibb.co/FHvf9h5/intelicorp.png"

logo_compañia = "https://i.ibb.co/54mbvXM/logobusiness.jpg"

# Barra "Servicio Especializado en Pruebas de Penetración y Evaluación"
navbar = dbc.NavbarSimple(
    children=[
        dbc.Col(html.Img(src=logo, height="50px", style={"float": "right", "margin-right": "0"})),
    ],
    brand=html.H1("Servicio Gestionado de iPENTEST", style={"margin-left": "-250px","font-size": "40px"}),
    brand_href="https://www.intelicorps.com",
    color="primary",
    dark=True,
    style={"max-width": "100%"}
)

#Listas Plegables del menu
GServicio = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Gestion de Servicio",href="/GestionServicio"),],
                label="Gestion de Servicio", className="my-dropdown-menu", direction="down", nav=True)

aplicacionWeb = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="/CicloDeEvaluacionWeb"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="/PosturadeSeguridadWeb"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="/TopVulnerabilidadesWeb"),
                dbc.DropdownMenuItem("Top de Riesgo",href="/TopDeRiesgoWeb"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="/TopDeMITREATT&CKWeb"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="/Top10OWASPWeb"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="/RecomendacionMitigacionWeb"),],
            label="Aplicación Web",style={"width": "dropdown_width"}, direction="down", nav=True)
aplicacionMovil =dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="/CicloDeEvaluacionMovil"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="/PosturadeSeguridadMovil"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="/TopVulnerabilidadesMovil"),
                dbc.DropdownMenuItem("Top de Riesgo",href="/TopDeRiesgoMovil"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="/TopDeMITREATT&CKMovil"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="/Top10OWASPMovil"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="/RecomendacionMitigacionMovil"),],
            label="Aplicación Móvil", className="my-dropdown-menu", direction="down", nav=True)
APIs = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="/CicloDeEvaluacionApis"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="/PosturadeSeguridadApis"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="/TopVulnerabilidadesApis"),
                dbc.DropdownMenuItem("Top de Riesgo",href="/TopDeRiesgoApis"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="/TopDeMITREATT&CKApis"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="/Top10OWASPApis"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="/RecomendacionMitigacionApis"),],
            label="APIs", className="my-dropdown-menu", direction="down", nav=True)
DD_Bb = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="/CicloDeEvaluacionDDBB"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="/PosturadeSeguridadDDBB"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="DDBB", className="my-dropdown-menu", direction="down", nav=True)
RedExterna = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="#"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="#"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="Red Externa", className="my-dropdown-menu", direction="down", nav=True)
Cloud = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="#"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="#"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="Cloud", className="my-dropdown-menu", direction="down", nav=True)
Segmentación  = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="#"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="#"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="Segmentación", className="my-dropdown-menu", direction="down", nav=True)
RedInalámbricas = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="#"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="#"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="Red Inalámbricas", className="my-dropdown-menu", direction="down", nav=True)
DispositivosIoT = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="#"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="#"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="Dispositivos IoT", className="my-dropdown-menu", direction="down", nav=True)
IngenieríaSocial = dbc.DropdownMenu(children=[
                dbc.DropdownMenuItem("Ciclos de Evaluacion",href="#"),
                dbc.DropdownMenuItem("Postura de Seguridad",href="#"),
                dbc.DropdownMenuItem("Top de Vulnerabilidades",href="#"),
                dbc.DropdownMenuItem("Top de Riesgo",href="#"),
                dbc.DropdownMenuItem("Top de MITRE ATT&CK",href="#"),
                dbc.DropdownMenuItem("Top 10 OWASP",href="#"),
                dbc.DropdownMenuItem("Recomendacion-Mitigacion",href="#"),],
            label="Ingeniería Social", className="my-dropdown-menu", direction="down", nav=True)

# Menú principal
dropdown_width = "500px"
card_menu_principal = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Ambientes objetivos", className="card-title"),
            html.Div(dbc.Card(GServicio),style={ "border-radius": "10px", "padding": "10px"},),
            html.Div(dbc.Card(aplicacionWeb),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(aplicacionMovil),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(APIs),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(DD_Bb),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(RedExterna),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(Cloud),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(Segmentación),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(RedInalámbricas),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(DispositivosIoT),style={ "border-radius": "10px", "padding": "10px"}),
            html.Div(dbc.Card(IngenieríaSocial),style={ "border-radius": "10px", "padding": "10px"}),


                       
        ]
    ),
    style={"width": "18rem"},color="primary", outline=True
)

#Contenido de la pantalla 1 
card_Principal_movil = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="https://i.ibb.co/f23khmv/desarrollo-de-aplicaciones.png",
                        className="img-fluid rounded-start", style={"width": "70%"},
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Aplicacion Movil", className="card-title"),
                            dbc.CardLink("APK version 0.17.1", href="#"),

                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
    ],
    className="mb-3 w-100",
    style={
        "background-color": "#ade8f4",  # Utilizamos el color rojo de Coolors
        #"color": "#F8961E",  # Utilizamos el color naranja de Coolors para las letras
        "padding": "20px",
        "margin-left": "-300px"
        
    }
),
card_Principal_web = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="https://i.ibb.co/ngGN6CY/aplicacion-web.png",
                        className="img-fluid rounded-start", style={"width": "70%"},
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Aplicacion Web", className="card-title"),
                            dbc.CardLink("http://url.a.evaluar.com", href="#"),

                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 w-100",
    style={
        "background-color": "#d7d0b7",  # Utilizamos el color rojo de Coolors
        #"color": "#F8961E",  # Utilizamos el color naranja de Coolors para las letras
        "padding": "20px", "margin-left": "-300px"}
)

card_Principal_QA = dbc.Card(
    html.H4("QA", className="card-title"))


#Organizacion de la pantalla por filas y columnas 

pantalla1 = dbc.Row(

    [
         dbc.Col(
            html.Div(
                [
                     html.H2(["Ambientes de Prueba", html.Img(src=logo_compañia, height="70px", style={"float": "right"})], className="text-center"),
                     html.H4(["Desarrollo"], style={"text-align": "left", "margin-left": "-300px"}),
                    html.Div(card_Principal_movil),
                    html.H4(["Producción"], style={"text-align": "left", "margin-left": "-300px"}),
                    html.Div(card_Principal_web),
                    html.H4(["QA"], style={"text-align": "left"}),
                    html.Div(card_Principal_QA)

                ],
                #style={"margin-top": "50px"}  # Añade un margen superior a la columna 1
            ), width=10 

        ),
        
    
    ], justify="center",
)



# Layout de la aplicación
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        navbar,
        html.Br(),
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(card_menu_principal, md=3),
                    dbc.Col(html.Div(id="page-content"), md=9),
                ]
            ),
            fluid=True,
        ),
    ]
)

# Callback para actualizar el contenido de la página
@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")],
)
def display_page(pathname):
    if pathname == "/GestionServicio":
        return gestion_del_servicio()
    elif pathname == "/CicloDeEvaluacionWeb":
        return ciclo_Evaluacion_Web()
    elif pathname == "/PosturadeSeguridadWeb":
        return postura_de_seguridad_web()
    elif pathname == "/TopVulnerabilidadesWeb":
        return top_vulnerabilidades_web()
    elif pathname == "/TopDeRiesgoWeb":
        return top_Riesgo_web()
    elif pathname == "/TopDeMITREATT&CKWeb":
        return top_Mitre_web()
    elif pathname == "/Top10OWASPWeb":
        return top_Top10OWASP_Web()
    elif pathname == "/RecomendacionMitigacionWeb":
        return recomendacion_Mitigacion_Web()
    elif pathname == "/CicloDeEvaluacionMovil":
        return ciclo_Evaluacion_Movil()
    elif pathname == "/PosturadeSeguridadMovil":
        return postura_de_seguridad_Movil()
    elif pathname == "/TopVulnerabilidadesMovil":
        return top_vulnerabilidades_Movil()
    elif pathname == "/TopDeRiesgoMovil":
        return top_Riesgo_Movil()
    elif pathname == "/TopDeMITREATT&CKMovil":
        return top_Mitre_Movil()
    elif pathname == "/Top10OWASPMovil":
        return top_Top10OWASP_Movil()
    elif pathname == "/RecomendacionMitigacionMovil":
        return recomendacion_Mitigacion_Movil()
    elif pathname == "/CicloDeEvaluacionApis":
        return ciclo_Evaluacion_Apis()
    elif pathname == "/PosturadeSeguridadApis":
        return postura_de_seguridad_Apis()
    elif pathname == "/TopVulnerabilidadesApis":
        return top_vulnerabilidades_Apis()
    elif pathname == "/TopDeRiesgoApis":
        return top_Riesgo_Apis()
    elif pathname == "/TopDeMITREATT&CKApis":
        return top_Mitre_Apis()
    elif pathname == "/Top10OWASPApis":
        return top_Top10OWASP_Apis()
    elif pathname == "/RecomendacionMitigacionApis":
        return recomendacion_Mitigacion_Apis()
    elif pathname == "/CicloDeEvaluacionDDBB":
        return ciclo_Evaluacion_DDBB()
    elif pathname == "/PosturadeSeguridadDDBB":
        return postura_de_seguridad_DDBB()

    else:
        return pantalla1

if __name__ == "__main__":
    app.run_server(debug=True)