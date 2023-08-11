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
import dash_html_components as html
import plotly.graph_objs as go
import plotly.figure_factory as ff
from datetime import datetime as dt
from dash.dependencies import Input, Output


logo_compañia = "https://i.ibb.co/54mbvXM/logobusiness.jpg"
home= "https://i.ibb.co/mHBzPPH/home2.png"
company= html.Img(src=logo_compañia, height="70px")
image = html.A(href= "/prueba.py", children=[html.Img(src=home, height="50px")])
table_style = {
    'border': '1px solid black',
    'justify':'center'
}
header_style = {
    'border': '1px solid black',
    'padding': '5px',
    'background-color': '#5585b5',  # Añadir estilo para cambiar el color de fondo
    'color': 'white',
    'text-align': 'center'
    
}
cell_style = {
    'border': '1px solid black',
    'padding': '5px',
    'text-align': 'center'
}
verde = {
    'border': '1px solid black',
    'padding': '5px',
    'text-align': 'center',
    'color': '#7dd87d'
}
vinotinto = {
    'border': '1px solid black',
    'padding': '5px',
    'text-align': 'center',
    'color': '#be3144'
}
rojo = {
    'border': '1px solid black',
    'padding': '5px',
    'text-align': 'center',
    'color': '#ff0000'
}
amarillo = {
    'border': '1px solid black',
    'padding': '5px',
    'text-align': 'center',
    'color': '#efd510'
}
##Estructura de cada pantalla 
#Gantt Cart
df = [dict(Task="Prueba 1", Start='2023-07-20', Finish='2023-08-10', Resource='Planificado'),
      dict(Task="Prueba 1", Start='2023-07-20', Finish='2023-07-21', Resource='Presentaciones'),
      dict(Task="Prueba 1", Start='2023-07-21', Finish='2023-07-30', Resource='Actual'),
      dict(Task="Prueba 1", Start='2023-07-30', Finish='2023-08-05', Resource='Informes'),
      dict(Task="Prueba 2", Start='2023-07-20', Finish='2023-07-21', Resource='Presentaciones'),
      dict(Task="Prueba 2", Start='2023-07-21', Finish='2023-07-30', Resource='PresentacionFinal'),
      dict(Task="Prueba 2", Start='2023-07-30', Finish='2023-08-05', Resource='Informes'),
      dict(Task="Prueba 3", Start='2023-08-05', Finish='2023-08-10', Resource='Cierre')]

colors = {'Planificado': 'rgb(133, 193, 233)',
          'Holgura': 'rgb(231, 76, 60)',
          'Actual': 'rgb(171, 235, 198)',
          'Informes': 'rgb(245, 176, 65)',
          'PresentacionFinal': 'rgb(69, 179, 157)',
          'Presentaciones': 'rgb(69, 179, 157)',
          'Cierre': 'rgb(165, 105, 189)'}

GanttChart= ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
GanttChart.update_layout(font=dict(size=18)) # Aumenta el tamaño de la fuente a 18
GanttChart['layout']['width'] = 1500  # Ancho en píxeles
GanttChart['layout']['height'] = 500  # Alto en píxeles

cardcronograma=dbc.Col(html.Div([
             html.H3(["Cronograma de Actividades 2023"], className="text-center"),
             html.H4(["Servicio de Pruebas de Evalución Y Penetracion en Company"], className="text-center"),
            html.Div([dcc.Graph(figure= GanttChart)] ,style={"display": "flex", "justify-content": "center"})
         ], style={"margin-left": "-150px"}
         )
         )
###Gráfico de Progreso
labels = ['Pendiente', 'Cpmpletado']
values = [90, 10]
GraficodeProgreso = go.Figure(data=[go.Pie(labels=labels, values=values)])
cardGrfico= html.Div([
             html.H4(["Gráfico General de Vulnerabilidades"], className="text-center"),
             dcc.Graph(figure=GraficodeProgreso)], style={"margin": "10px"})

TabladeActividades = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('Resumen de Actividades Técnicas del Gantt', colSpan=4, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Fecha', colSpan=1, style=cell_style),
        html.Th('Actividad', colSpan=3, style=cell_style),
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Td("00/00/2023", style=cell_style,colSpan=1),
                    html.Td(
                            [
                                html.P("Capa de Red"),
                                html.P("°Inalámbrica:"),
                                html.P("- Preparación de Ambientes."),
                            ],colSpan=2, style=cell_style
                        ),
                    html.Td(
                            [
                                html.P("Capa de Aplicación Web"),
                                html.P("-Preparación de Ambientes."),
                            ],colSpan=1, style=cell_style
                        ),

                ]
            ),
        html.Tr(
                [
                    html.Td("00/00/2023", style=cell_style,colSpan=1),
                    html.Td(
                            [
                                html.P("Capa de Red"),
                                html.P("°Inalámbrica:"),
                                html.P("- Preparación de Ambientes."),
                            ],colSpan=1, style=cell_style
                        ),
                    html.Td(
                            [
                                html.P("Capa de Aplicación Web"),
                                html.P("-Preparación de Ambientes."),
                            ],colSpan=1, style=cell_style
                        ),
                    html.Td(
                            [
                                html.P("Capa Humana"),
                                html.P("-Ajuste de plantillas en base a las observaciones del Cliente."),
                            ],colSpan=1, style=cell_style
                        ),
                ]
            ),
        html.Tr(
                [
                    html.Td("00/00/2023", style=cell_style,colSpan=1),
                    html.Td(
                            [
                                html.P("Capa de Red"),
                                html.P("°Inalámbrica:"),
                                html.P("- Preparación de Ambientes."),
                            ],colSpan=2, style=cell_style
                        ),
                    html.Td(
                            [
                                html.P("Capa de Aplicación Web"),
                                html.P("-Preparación de Ambientes."),
                            ],colSpan=1, style=cell_style
                        ),

                ]
            ),
        html.Tr(
                [
                    html.Td("00/00/2023", style=cell_style,colSpan=1),
                    html.Td(
                            [
                                html.P("Capa de Red"),
                                html.P("°Inalámbrica:"),
                                html.P("- Preparación de Ambientes."),
                            ],colSpan=1, style=cell_style
                        ),
                    html.Td(
                            [
                                html.P("Capa de Aplicación Web"),
                                html.P("-Preparación de Ambientes."),
                            ],colSpan=1, style=cell_style
                        ),
                    html.Td(
                            [
                                html.P("Capa Humana"),
                                html.P("-Ajuste de plantillas en base a las observaciones del Cliente."),
                            ],colSpan=1, style=cell_style
                        ),
                ]
            ),
        
    ],
    # Estilo de la tabla
    style=table_style
)
FasesenProceso= [
    dbc.CardHeader("Fases en  Proceso", style={"font-size": "24px"}),
    dbc.CardBody(
        [
            html.H1("7", className="card-title", style={"text-align": "center"}),
        ]
    ),
]
FasesCompletadas= [
    dbc.CardHeader("Fases Completadas", style={"font-size": "24px"}),
    dbc.CardBody(
        [
            html.H1("2", className="card-title", style={"text-align": "center"}),
        ]
    ),
]
FasesPendientes= [
    dbc.CardHeader("Fases Pendientes", style={"font-size": "24px"}),
    dbc.CardBody(
        [
            html.H1("24", className="card-title", style={"text-align": "center"}),
        ]
    ),
]
Cumplimiento= [
    dbc.CardHeader("% Cumplimiento", style={"font-size": "24px"}),
    dbc.CardBody(
        [
            html.H1("6", className="card-title", style={"text-align": "center"}),
        ]
    ),
]
cardsagrupados = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Card(FasesenProceso, color="primary", inverse=True)),
                dbc.Col(dbc.Card(FasesCompletadas, color="warning", inverse=True)),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(FasesPendientes, color="success", inverse=True)),
                dbc.Col(dbc.Card(Cumplimiento, color="danger", inverse=True)),
            ],
            className="mb-4",
        ),
    ]
)
cardrendimiento= html.Div([
             html.H4(["Estado de Rendimiento"], className="text-center"),
             html.Div([cardsagrupados])])
#layout
GestiondelServicio= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Gantt del Servicio"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),
        dbc.Row([
            dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardcronograma), className="mb-3", style={"background-color": "rgb(204, 209, 209)", "display": "flex", "justify-content": "center"}    
        ),
    ]
)
         ], style={"margin-left": "-220px"}
         )
         )],
         ),
         dbc.Row([
             
            dbc.Col(
                html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardGrfico),style={"background-color": "rgb(204, 209, 209)"}  )]), 
                 html.Div([cardrendimiento]   )
                 

         ], style={"margin-left": "-220px"}
         ), width=4
         ),
         #Vulnerabilidades y Escenarios
        dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(TabladeActividades),        
        ),
    ]
)  

         ],
         ), width=8
         ),

         ],
         ),


    
    ], justify="center",
)



#______________________________________________________________________________________________________________________________________
##Aplicacion Web

#contenido de ciclo web

#####TABLA####
id_counter = 1

table_header = [
    html.Thead(html.Tr([html.Th("ID"), html.Th("Vulnerabilidad Encontrada"), html.Th("Riesgo"), html.Th("Tipo de Prueba"), html.Th("CICLO 1"), html.Th("RETESTING"), html.Th("CICLO 2")]))
]

def add_row(Vulnerabilidad_Encontrada, Riesgo, TipoPrueba, CICLO1, RETESTING, CICLO2 ):
    global id_counter
    row = html.Tr([html.Td(id_counter), html.Td(Vulnerabilidad_Encontrada), html.Td(Riesgo), html.Td(TipoPrueba), html.Td(CICLO1), html.Td(RETESTING), html.Td(CICLO2)])
    id_counter += 1
    return row

table_body = [html.Tbody([add_row("	Exposición de información del servidor y usuarios del sistema", "BAJO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X"),
                        add_row("Encabezados de respuesta no incluyen “strict-transport-security”", "MEDIO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X"), 
                        add_row("Frameable response", "BAJO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X"),
                        add_row("Login con un solo factor", "MEDIO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X")])]

table_CiclodeEvaluacion = dbc.Table(table_header + table_body,  striped=True, bordered=True, hover=True)
cardciclodeevaluacionwebTABLA= html.Div([
            html.H5(["Ciclo de Evaluación"], className="text-center"),
            table_CiclodeEvaluacion ], style={"margin-left": "-100px"} ),
####GRAFICO####
# datos de ejemplo para el gráfico de torta
labels = ['Ciclo 1', 'Ciclo 2', 'Retest', 'Ciclo 3']
values = [15, 13, 5, 3]
GraficaCilodeEvaluacionWeb = go.Figure(data=[go.Pie(labels=labels, values=values)])
cardgracicocilodeevaluacion=html.Div([
             html.H5(["Mitigación Por Ciclo"], className="text-center"),
             dcc.Graph(figure=GraficaCilodeEvaluacionWeb) ]), 
#Tablas de Diagnóstico General


tableANÁLISISEJECUTIVORIESGO = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('1- ANÁLISIS EJECUTIVO RIESGO', colSpan=5, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Escala:', style=cell_style),
        html.Th('↑Critico', style=vinotinto),
        html.Th('↗Alto', style=rojo),
        html.Th('→Medio', style=amarillo),
        html.Th('↘Bajo', style=verde)
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Th("NIVEL RIESGO GENERAL:", style=cell_style,colSpan=4),
                    html.Th("↘Bajo", colSpan=1, style=verde)
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)

tableEVALUACIONDENIVELDESEGURIDADGENERAL = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('2- EVALUACION DE NIVEL DE SEGURIDAD GENERAL', colSpan=4, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Escala:', style=cell_style),
        html.Th('↗Elevado', style=verde),
        html.Th('→Medio', style=amarillo),
        html.Th('↘Deficiente', style=rojo)
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Th("https://url.a.evaluar.com.co/", style=cell_style,colSpan=3),
                    html.Th("↗Elevado", colSpan=1, style=verde)
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)

tableNIVELESDEEFECTIVIDADDESOFTWAREYHARDWAREDESEGURIDAD = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('3- NIVELES DE EFECTIVIDAD DE SOFTWARE Y HARDWARE DE SEGURIDAD', colSpan=4, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Escala:', style=cell_style),
        html.Th('↗Elevado', style=verde),
        html.Th('→Medio', style=amarillo),
        html.Th('↘Deficiente', style=rojo)
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Th("WAF (Web Application Firewall)", style=cell_style,colSpan=3),
                    html.Th("**DETECTADO**", colSpan=1, style=verde)
                ]
            ),
        html.Tr(
                [
                    html.Th("Software / Hardware y/o configuraciones de Seguridad", style=cell_style,colSpan=3),
                    html.Th("↗Elevado", colSpan=1, style=verde)
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)
carddiagnosticogeneral=html.Div([
             html.H5(["Diagnóstico de Evaluación General de los Ciclos"], className="text-center"),
             html.P("Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet.", className="text-justify" ), 
         ]
         )
carddiagnosticogeneraldetallado=html.Div([
             html.H5(["Diagnóstico General"], className="text-center"),
             html.P("Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet.", className="text-center" ),
             html.Div([tableANÁLISISEJECUTIVORIESGO], style={'margin': 'auto', 'width': '50%'}),
             html.Div([tableEVALUACIONDENIVELDESEGURIDADGENERAL], style={'margin': 'auto', 'width': '50%', "margin-top": "20px"}),
             html.Div([tableNIVELESDEEFECTIVIDADDESOFTWAREYHARDWAREDESEGURIDAD], style={'margin': 'auto', 'width': '50%', "margin-top": "20px"}),
             html.Table(style={'position': 'absolute', 'top': '50%', 'transform': 'translateY(-50%)'})

         ]
         )
#layout
Es_CicloDeEvaluacionWeb = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Ciclo de Evaluacion Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ), #Tabla "Ciclos de Evaluación"
        dbc.Row([
            dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardciclodeevaluacionwebTABLA), className="mb-3"    
        ),
    ]
)
         ], style={"margin-left": "-120px"}
         )
         )],
         ),
        

        #Grafica
        dbc.Row([
            dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardgracicocilodeevaluacion), style={"background-color": "rgb(204, 209, 209)"}         
        ),
    ]
)  

         ], style={"margin-left": "-220px"}
         ), width=6
         ),
         #Diagnóstico de Evaluación General de los Ciclos
        dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(carddiagnosticogeneral), style={"background-color": "rgb(204, 209, 209)"}    
        ),
    ]
)  

         ]
         ), width=6
         ),
         
    #Diagnostico general
        dbc.Row([

         dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(carddiagnosticogeneraldetallado), style={"background-color": "rgb(204, 209, 209)", "margin-left": "-120px", "display": "flex", "center-content": "space-between", "width": "100%", "text-align": "center", "margin-left": "-220px"}    
        ),
    ], 
)  

         ]
         ), width=12
         ),
         


    
    ], justify="center",
)


    
    ], justify="center",
)


    
    
    ], justify="center",
)
#________________________________________________________________________________________________________________________________________________________________________________________________________


####Grafico Postura de seguridad
df = pd.DataFrame({'fecha': ['2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10', '2023-06-11', '2023-06-12', '2023-06-13', '2023-06-14', '2023-06-15'], 
                   'Vulnerabilidades': [4, 6, 2, 8, 5, 7, 1, 3, 9, 2]})
fig = go.Figure(data=[go.Scatter(
            x=df['fecha'], 
            y=df['Vulnerabilidades']
        )])
fig.update_layout(
    title='<b>Trending de Vulnerabilidades</b>', 
    title_x=0.5,  # Centrar el título horizontalmente
    xaxis_title='Ciclos de Evaluación',
    yaxis_title='Vulnerabilidades encontradas',
    yaxis=dict(tickfont=dict(size=20)),
    xaxis=dict(tickfont=dict(size=20))
)


#layout
Es_PosturaDeSeguridadWeb = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Postura de Seguridad Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),
        #Gráfico Trending de Vulnerabilidades 
        html.Div([dcc.Graph(figure=fig)]),
        #Diagrama "Postura de Seguridad"
        html.Div([ 
        dbc.Row([
    dbc.Col(html.Div([ 
        html.H6(["Cliente"], className="text-center"),
    ]), width=1),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src=logo_compañia, height="80px"),
            html.H2(["↓"]), 

        ], className="d-flex flex-column align-items-center", style={"border-bottom": "2px solid black", "font-weight": "bold"})
    ]), width=11

), 
    ],justify="center", style={"margin-top": "80px", "background-color": "#ffffff", "margin-left": "-400px"}
),
    ]),
    #Agentes de amenaza
    html.Div([ 
        dbc.Row([
    dbc.Col(html.Div([ 
        html.H6(["Agentes de amenaza"], className="text-center", style={"margin-top": "30px"} ), 
    ]), width=1),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/KcgqtrV/per-removebg-preview.png" , height="70px"),
            html.H6(["Atacante autenticado remoto"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/KcgqtrV/per-removebg-preview.png" , height="70px"),
            html.H6(["Atacante remoto"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/KcgqtrV/per-removebg-preview.png" , height="70px"),
            html.H6(["Atacante no Autenticado"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center", style={"border-bottom": "2px solid black", "font-weight": "bold"})
    ]), width=5,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/KcgqtrV/per-removebg-preview.png" , height="70px"),
            html.H6(["Atacante Autenticado"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center", style={"border-bottom": "2px solid black", "font-weight": "bold"})
    ]), width=3,),


    ],justify="center",  style={"background-color": "#fafafa", "margin-left": "-400px"}
),
    ]),
    #Vectores de Ataques
     html.Div([ 
        dbc.Row([
    dbc.Col(html.Div([ 
        html.H6(["Vectores de Ataques"], className="text-center", style={"margin-top": "30px"} ), 
    ]), width=1),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/njXxjxF/cod.jpg" , height="70px"),
            html.H6(["Inserción de código malicioso"], className="text-center"),
            html.H2(["↓"]),
            
        ], className="d-flex flex-column align-items-center")
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/P4HFJPX/link-removebg-preview.png" , height="90px"),
            html.H6(["Inserción de link malicioso"], className="text-center"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/cXqJ3Pp/ida-Cookies-blog-655x470-removebg-preview.png" , height="70px"),
            html.H6(["Explotacion de vulnerabilidad mediante del acceso a las cookies"], className="text-center"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/j51JVwM/delincuente-removebg-preview.png" , height="70px"),
            html.H6(["El ciberdelincuente espia el tráfico de la red de la victima. Facilitando enlaces adecuados para que la cookie sea transmitida en texto claro"], className="text-center"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center border-bottom")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/hfyBM0t/hombreenelmedio-removebg-preview.png" , height="70px"),
            html.H6(["Ataque de hombre en el medio"], className="text-center"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center", )
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
           html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/rM2s7f8/ing-inversa-removebg-preview-2.png" , height="90px"),
            html.H6(["Ingenieria de reversa"], className="text-center"),
            html.H2(["↓"]),

            
        ], className=" d-flex flex-column align-items-center ")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.I(className="bi bi-caret-down"),
            html.Img(src="https://i.ibb.co/hfyBM0t/hombreenelmedio-removebg-preview.png" , height="70px"),
            html.H6(["Ataque de hombre en el medio"], className="text-center"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center border-bottom", )
    ]), width=1,),


    ],justify="center", style={"background-color": "#f0ece2", "margin-left": "-400px"}   
),
    ]),
    #Debilidades de Seguridad 
     html.Div([ 
        dbc.Row([
    dbc.Col(html.Div([ 
        html.H6(["Debilidades de Seguridad "], className="text-center", style={"margin-top": "30px"} ), 
    ]), width=1),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/njXxjxF/cod.jpg" , height="70px"),
            html.H6(["Cabecera Content Security Policy"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/PrRCThy/cabexera-removebg-preview.png" , height="80px"),
            html.H6(["Cabecera Anti-clickjacking"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/3Bs8HNJ/owasp-removebg-preview.png" , height="70px"),
            html.H6(["Configuracion incorrecta de seguridad"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/3Bs8HNJ/owasp-removebg-preview.png" , height="70px"),
            html.H6(["Configuracion incorrecta de seguridad"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/9mDGqdL/BD-removebg-preview.png" , height="70px"),
            html.H6(["Soporte de cifrado débil"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center ", )
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/5c80TJs/debug.png" , height="90px"),
            html.H6(["Debug activado"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className=" d-flex flex-column align-items-center ")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/BBgdz5Z/texto.png" , height="70px"),
            html.H6(["Tráfico en texto claro"], className="text-center"),
            html.I(className="bi bi-caret-down"),

            
        ], className="d-flex flex-column align-items-center ", )
    ]), width=1,),


    ],justify="center", style={"background-color": "#dfd3c3","margin-left": "-400px"}   
),
    ]),#Controles de Seguridad 
     html.Div([ 
        dbc.Row([
    dbc.Col(html.Div([ 
        html.H6(["Controles de Seguridad "], className="text-center", style={"margin-top": "30px"} ), 
    ]), width=1),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),
            
        ], className="d-flex flex-column align-items-center", )
    ]), width=1,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),

            
        ], className=" d-flex flex-column align-items-center ")
    ]), width=2,),
    dbc.Col(html.Div([
        html.Div([
            html.Img(src="https://i.ibb.co/937GrZY/seg-removebg-preview.png" , height="90px"),
            html.H2(["↓"]),

            
        ], className="d-flex flex-column align-items-center ", )
    ]), width=1,),


    ],justify="center", style={"background-color": "#c7b198","margin-left": "-400px"}   
),
    ]),
    #Impactos Técnicos-Negocios 
     html.Div([ 
        dbc.Row([
    dbc.Col(html.Div([ 
        html.H6(["Impactos Técnicos-Negocios"], className="text-center", style={"margin-top": "30px"} ), 
    ]), width=1),
    dbc.Col(html.Div([
        html.Div([
            html.H2(["↓"]),
            html.H6(["https://url.a.evaluar.com.co/"], className="text-center"),


            
        ], className="d-flex flex-column align-items-center", style={"border-top": "2px solid black", "font-weight": "bold"})
    ]), width=8,),
    dbc.Col(html.Div([
        html.Div([
            html.H2(["↓"]),
            html.H6(["Obtención de información privilegiada de los clientes como contraseñas, usuarios, transacciones, entre otros"], className="text-center"),


            
        ], className="d-flex flex-column align-items-center", style={"border-top": "2px solid black", "font-weight": "bold"})
    ]), width=3,),
   


    ],justify="center", style={"background-color": "#ff9c6d","margin-left": "-400px"}   
),
    ]),
    

   
        
    
    ], justify="center"
)
#____________________________________________________________________________________________________________________________________________________________
###Gráfico General de Vulnerabilidades
labels = ['Bajo', 'Medio', 'Info', 'Critico']
values = [16, 5, 2, 0]

GraficaTopDeVulnerabilidades = go.Figure(data=[go.Pie(labels=labels, values=values)])
cardestsdisticasdevulnerabilidadesweb= html.Div([
             html.H4(["Estadísticas de Vulnerabilidades por Nivel de Riesgo"], className="text-center"),
             html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet. "),   
             html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet." ),   
             html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet." ),   

         ]
         )
cardgraficotopvulnerabilidades=html.Div([
             html.H4(["Gráfico General de Vulnerabilidades"], className="text-center"),
             dcc.Graph(figure=GraficaTopDeVulnerabilidades)])
cardvulnerabilidadesyEscenarios=html.Div([
             html.H4(["Vulnerabilidades y Escenarios"], className="text-center"),
                html.H5(["Nivel Medio:"]),
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet. " ),   
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet." ),   
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet."),   

                html.H5(["Nivel Bajo:"]),
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet. " ),   
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet." ),   
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet."),   

                html.H5(["Nivel Informativo:"]),
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet. " ),   
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet." ),   
                    html.P("• Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet."),   
         ]
         )
#Layout
Es_TopDeVulnerabilidadesWeb= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top de Vulnerabilidades Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),
        dbc.Row([
            dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardestsdisticasdevulnerabilidadesweb), className="mb-3", style={"background-color": "rgb(204, 209, 209)"}  
        ),])
         ], style={"margin-left": "-200px"}
         )
         )],
         ),

         #Garfica
         dbc.Row([
             dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardgraficotopvulnerabilidades),  style={"background-color": "rgb(204, 209, 209)"}     
        ),
    ]
)  

         ],style={"margin-left": "-200px"}
         ), width=6
         ),
         #Vulnerabilidades y Escenarios
         dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardvulnerabilidadesyEscenarios),  style={"background-color": "rgb(204, 209, 209)"}     
        ),
    ]
)  

         ]
         ), width=6
         ),

         ],
         ),
    
    ], justify="center",
)

#_________________________________________________________________________________________________________________________________________________________________________________
# Datos de ejemplo
labels = ['Bajo', 'Medio', 'Info', 'Critico', 'Alto']
values = [16, 5, 2, 0,0]

# Creamos la figura de Plotly
fig = go.Figure(go.Bar(
    x=labels,
    y=values,
    marker_color='indianred'
))
data = {'Tareas': ['Cifrados Débiles habilitados', 'Daño Cosmetico a la aplicacion ', 'Fallas de cigfrado', 'Exposición de Componentes', 'Falta de alertas de cierre de sesión'],
        'Porcentaje': [38, 30, 25, 18, 25]}
df = pd.DataFrame(data)
graficotopderiesgo = go.Figure(go.Bar(
            x=df['Porcentaje'],
            y=df['Tareas'],
            orientation='h'))

graficotopderiesgo.update_layout(
    yaxis=dict(tickfont=dict(size=20)),
    xaxis=dict(tickfont=dict(size=20))
)
cardestadisticasgeneralderiesgo=html.Div([
             html.H4(["Estadísticas Generales del Escenario de Riesgo"], className="text-center"),
             html.P("Es importante destacar que, durante el mes de junio del 2023, Intelicorp ha actualizado la escala de riesgos utilizada para la clasificación de los niveles de riesgos en base a un puntaje de 0 a 81 puntos. Dicha escala se presenta a continuación, y contempla para su calculo el análisis inherente al impacto técnico y de negocios derivado de las vulnerabilidades identificadas durante las actividades desarrolladas en este informe. En este sentido, los resultados presentados en este informen cuentan con esta nueva metodología de análisis de resultados. " ),   
         ], style={"margin-left": "-20px"}
         )
cardgraficostobderiesgo= html.Div([
             html.H4(["Gráfico Top de Riesgo de seguridad"], className="text-center"),
             dcc.Graph(figure=fig)   

         ], style={"margin-left": "-20px"}
         )
cardgraficotopderiesgo= html.Div([
            html.H4(["Top de Riesgo Web"], className="text-center"),
            dcc.Graph(figure=graficotopderiesgo)
        ])
#Layuot
Es_TopDeRiesgoWeb= dbc.Row(
    [

        dbc.Col(
            html.Div(
                [
                    html.H2(["Top de Riesgo Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),
            #Garfica
         dbc.Row([
                          #Vulnerabilidades y Escenarios
        dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardestadisticasgeneralderiesgo),  style={"background-color": "rgb(204, 209, 209)"}     
        ),
    ]
)  

         ],style={"margin-left": "-200px"}
         ), width=6
         ),
             dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardgraficostobderiesgo),  style={"background-color": "rgb(204, 209, 209)"}     
        ),
    ]
)  

         ],
         ), width=6




         ),
         ],
         ),
         dbc.Row([
            dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardgraficotopderiesgo), className="mb-3", style={"background-color": "rgb(204, 209, 209)"}  
        ),])
         ], style={"margin-left": "-200px"}
         )
         )],
         ),


    
    ], justify="center",
)
#___________________________________________________________________________________________________
Tablamitre = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('TOP 10 OWASP 2020', colSpan=5, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Vulnerabilidad', colSpan=1, style=cell_style),
        html.Th('Impacto', colSpan=1, style=cell_style),
        html.Th('MitreID', colSpan=1, style=cell_style),
        html.Th('Técnica', colSpan=1, style=cell_style),
        html.Th('Mitigacion', colSpan=1, style=cell_style),


    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Td("Cabecera Content Security Policy (CSP) no configurada", style=cell_style,colSpan=1),
                    html.Td("INFO", style=cell_style,colSpan=1),
                    html.Td("N/A", style=cell_style,colSpan=1),
                    html.Td("N/A", style=cell_style,colSpan=1),
                    html.Td("N/A", style=cell_style,colSpan=1),
                ]
            ),
        html.Tr(
                [
                    html.Td("Falta de cabecera Anti-Clickjacking", style=cell_style,colSpan=1),
                    html.Td("MEDIO", style=cell_style,colSpan=1),
                    html.Td("T1185", style=cell_style,colSpan=1),
                    html.Td("Adversary-in-the-Midd", style=cell_style,colSpan=1),
                    html.Td("1. Deshabilitar o remover características y programas innecesarios 2.Cifrar la informa", style=cell_style,colSpan=1),
                ]
            ),
        html.Tr(
                [
                    html.Td("Exposición de información sensible y ejecución de código ", style=cell_style,colSpan=1),
                    html.Td("BAJO", style=cell_style,colSpan=1),
                    html.Td("T1185", style=cell_style,colSpan=1),
                    html.Td("Abuse Elevation Control Mechanism", style=cell_style,colSpan=1),
                    html.Td("1. Guía al desarrollador de aplicaciones", style=cell_style,colSpan=1),
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)

cardmitretabla= html.Div([
            html.Div([Tablamitre])
        ])
#Layout
Es_TopMITREWeb= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top MITRE ATT&CK Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),
         #tabla
         dbc.Row([
            dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardmitretabla), className="mb-3",style={"background-color": "rgb(204, 209, 209)"}  
        ),])
         ], style={"margin-left": "-200px"}
         )
         )],
         ),
    
    ], justify="center",
)
#___________________________________________________________________________
Tablatop10 = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('TOP 10 OWASP 2020', colSpan=4, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('ID', colSpan=1, style=cell_style),
        html.Th('RIESGO', colSpan=3, style=cell_style),
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Td("A123", style=cell_style,colSpan=1),
                    html.Td([
                                html.P("FALLAS CRIPTGRÁFICAS"),
                                html.P("°Cookie sin el flag Secure."),
                                html.P("°Cifrados débiles habilitados"),


        ], colSpan=3, style=cell_style)
                ]
            ),
        html.Tr(
                [
                    html.Th("A12", style=cell_style,colSpan=1),
                    html.Td([
                                html.P("INYECCIÓN"),
                                html.P("°Inyección de contenido no deseado en PDF"),

        ], colSpan=3, style=cell_style)
                ]
            ),
        html.Tr(
                [
                    html.Td("A04", style=cell_style,colSpan=1),
                    html.Td([
                                html.P("DISEÑO INSEGURO"),
                                html.P("°Uso de Google Analytics en la aplicación bancaria y envío de datos privados"),
                                html.P("°Falta de alerta de cierre de sesión"),
                                html.P("°Falta de doble factor de autenticación en operación sensible"),


        ], colSpan=3, style=cell_style),
        ]
            ),
         html.Tr(
                [
                    html.Td("A04", style=cell_style,colSpan=1),
                    html.Td([
                                html.P("CONFIGURACIÓN DEFICIENTE DE SEGURIDAD"),
                                html.P("°Cabecera Content Security Policy (CSP) no configurada"),
                                html.P("°Falta de cabecera Anti-Clickjacking"),
                                html.P("°Cookie sin el flag HttpOnly"),
                                html.P("°Exposición de hash de cuenta o tarjeta en la URL"),


        ], colSpan=3, style=cell_style),
                ]
            )
            
    ],
    # Estilo de la tabla
    style=table_style
)
labels = ['Inyeccion', 'FALLAS CRIPTGRÁFICAS']
values = [90, 10]
GraficodeTop10 = go.Figure(data=[go.Pie(labels=labels, values=values)])
cardgraficotop10= html.Div([
            html.Div([
            html.H4(["Gráfico de Vulnerabilidades TOP 10 OWASP"], className="text-center"),
             dcc.Graph(figure=GraficodeTop10)  
         ], style={"margin-left": "-20px"}
         ),
        ])
Cardcuadrotop10=html.Div([
             html.Div([Tablatop10], style={'margin': 'auto', 'width': '50%', "margin-top": "20px"}),


         ], style={
        'width': '100%',
        'height': '100%',
        'text-align': 'center',
        'vertical-align': 'middle',
        'display': 'flex',
        'flex-direction': 'column',
        'justify-content': 'center'
    }
         )

#layout
Es_Top10OWASPWeb= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top 10 OWASP Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),       dbc.Row([
                     #Garfica
         dbc.Row([
             dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardgraficotop10), className="mb-3", style={"background-color": "rgb(204, 209, 209)"}  
        ),])
         ], style={"margin-left": "-200px"}
         )
         ),
         ],
         ),
            
         ],
         ),# Cuadro
         dbc.Row([
             dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(Cardcuadrotop10), className="mb-3",style={"background-color": "rgb(204, 209, 209)"}  
        ),])
         ], style={"margin-left": "-200px"}
         )
         ),
         ],
         ),



        
 



    
    ], justify="center",
)
#________________________________________________________________________________
card_style = {
    "border-radius": "10px",
    "padding": "10px",
    "background-color": "#007bff",
    "color":"#007bff",
    "font-size": "20px",

}
cardrecomendacion= html.Div([
                    html.P("Seguir las recomendaciones técnicas dadas para cada hallazgo." ),   
                    html.P("Nuestras recomendaciones generales van de la mano con las últimas tendencias de seguridad para aplicaciones web teniendo en cuenta las brechas de seguridad más frecuentes, el objetivo es que sirvan como mejores prácticas en la implementación y desarrollo de aplicaciones web." ),   
         ])
cardsegunelfabricante=html.Div([
     html.Div(dbc.Card("Según Fabricante", color="primary", inverse=True, style=card_style, className="text-center")),
     html.H6("1. Estar siempre prevenidos ante amenazas desconocidas:"),
     html.P("A medida que el uso de aplicaciones aumenta, las amenazas a la seguridad también evolucionan y pueden aparecer tipos de ataques desconocidos. Por este motivo, hay que estar al día de las últimas tendencias en ciberataques y contar con un plan proactivo para actuar lo antes posible ante un peligro de esta índole." ),   
     html.H6("2. Buenas prácticas de seguridad:"),
     html.P("Buenas prácticas de seguridad cuando se desarrolla una aplicación, para que, cuando ésta sea usada, no haya ningún tipo de problema durante su utilización y los datos de los usuarios se mantengan siempre protegidos." ),   
     html.H6("3. Mantener un historial de datos y accesos para que, en caso de que exista algún problema o interrupción de datos, sea posible identificar rápidamente su origen"),
     html.H6("4. Seguridad durante el desarrollo de código"),
     html.P("Cualquier laguna en la codificación o diseño puede dar acceso a los atacantes a información sensible del usuario, por ello los desarrolladores deben validar los datos para que solo los que cuenten con el formato correcto entren en la estructura de la aplicación web."),
     html.H6("5. Evaluaciones continuas de seguridad:"),
    html.P("Se observa que la aplicación se produce bajo un proceso de desarrollo ágil. se recomienda ejecutar pruebas de seguridad en paralelo con las pruebas de QA de cada release para evitar que las nuevas vulnerabilidades que se generen en el desarrollo sean expuestas al público."),
])
cardsegunmitre=html.Div([
     html.Div(dbc.Card("Según MitreAtt&CK", color="primary", inverse=True, style=card_style, className="text-center")),
     html.H6("1. Gestión de cuentas de usuario"),
     html.H6("2. Entrenamiento de los usuarios"),
     html.H6("3. Deshabilitar o remover características y programas innecesarios"),
     html.H6("4. Cifrar la información sensible"),
     html.H6("5. Filtrar el tráfico de red"),
     html.H6("5. Limitar el acceso a los recursos de red"),
     html.H6("5. Prevención de intrusos de red"),
     html.H6("5. Segmentación de red"),
     html.H6("5. Entrenamiento al usuario"),
     html.H6("5. Guía para el desarrollador de la aplicación"),
     html.H6("5. Encriptar en tráfico de red"),
     html.H6("5. Usar la versión más reciente del sistema operativo"),
     html.H6("5. El tipo de técnica de ataque Data from Local System no se puede mitigar fácilmente con controles preventivos ya que se basa en el abuso de las funciones del sistema."),
])
#Layout
Es_Recomendacion_Mitigacion_Web= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Recomendación Y Mitigación Web"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2

        ),   #Segun Fabricante 
                 dbc.Row([
             dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardsegunelfabricante), style={"background-color": "rgb(204, 209, 209)"}      
        ),
    ]
)  

         ],style={"margin-left": "-200px"}
         ), width=6
         ),
         #Segun Mitre
         dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardsegunmitre), style={"background-color": "rgb(204, 209, 209)"}   
        ),
    ]
)  

         ]
         ), width=6
         ),

         ],
         ),
    
    ], justify="center",
)
#------------------------------------------------------------------------------------------------------------------------------
##Aplicacion Movil
#contenido de ciclo web
#####TABLA####
id_counter = 1

table_headerMovil = [
    html.Thead(html.Tr([html.Th("ID"), html.Th("Vulnerabilidad Encontrada"), html.Th("Riesgo"), html.Th("Tipo de Prueba"), html.Th("CICLO 1"), html.Th("RETESTING"), html.Th("CICLO 2")]))
]

def add_row(Vulnerabilidad_Encontrada, Riesgo, TipoPrueba, CICLO1, RETESTING, CICLO2 ):
    global id_counter
    row = html.Tr([html.Td(id_counter), html.Td(Vulnerabilidad_Encontrada), html.Td(Riesgo), html.Td(TipoPrueba), html.Td(CICLO1), html.Td(RETESTING), html.Td(CICLO2)])
    id_counter += 1
    return row

table_bodyMovil = [html.Tbody([add_row("	Exposición de información del servidor y usuarios del sistema", "BAJO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X"),
                        add_row("Encabezados de respuesta no incluyen “strict-transport-security”", "MEDIO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X"), 
                        add_row("Frameable response", "BAJO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X"),
                        add_row("Login con un solo factor", "MEDIO", "Prueba Manual", "Notificado al cliente", "Notificado al cliente", "X")])]

table_CiclodeEvaluacionMovil= dbc.Table(table_headerMovil + table_bodyMovil,  striped=True, bordered=True, hover=True)
cardciclodeevaluacionwebTABLAMovil= html.Div([
            html.H5(["Ciclo de Evaluación"], className="text-center"),
            table_CiclodeEvaluacionMovil ], style={"margin-left": "-100px"} ),
####GRAFICO####
# datos de ejemplo para el gráfico de torta
labelsMovil = ['Ciclo 1', 'Ciclo 2', 'Retest', 'Ciclo 3']
valuesMovil = [15, 13, 5, 3]
GraficaCilodeEvaluacionMovil = go.Figure(data=[go.Pie(labels=labelsMovil, values=valuesMovil)])
cardgracicocilodeevaluacionMovil=html.Div([
             html.H5(["Mitigación Por Ciclo"], className="text-center"),
             dcc.Graph(figure=GraficaCilodeEvaluacionMovil) ]), 
#Tablas de Diagnóstico General


tableANÁLISISEJECUTIVORIESGOMovil = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('1- ANÁLISIS EJECUTIVO RIESGO', colSpan=5, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Escala:', style=cell_style),
        html.Th('↑Critico', style=vinotinto),
        html.Th('↗Alto', style=rojo),
        html.Th('→Medio', style=amarillo),
        html.Th('↘Bajo', style=verde)
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Th("NIVEL RIESGO GENERAL:", style=cell_style,colSpan=4),
                    html.Th("↘Bajo", colSpan=1, style=verde)
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)

tableEVALUACIONDENIVELDESEGURIDADGENERALMovil = html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('2- EVALUACION DE NIVEL DE SEGURIDAD GENERAL', colSpan=4, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Escala:', style=cell_style),
        html.Th('↗Elevado', style=verde),
        html.Th('→Medio', style=amarillo),
        html.Th('↘Deficiente', style=rojo)
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Th("https://url.a.evaluar.com.co/", style=cell_style,colSpan=3),
                    html.Th("↗Elevado", colSpan=1, style=verde)
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)

tableNIVELESDEEFECTIVIDADDESOFTWAREYHARDWAREDESEGURIDADMovil= html.Table(
    # Encabezado de la tabla
    [html.Tr([html.Th('3- NIVELES DE EFECTIVIDAD DE SOFTWARE Y HARDWARE DE SEGURIDAD', colSpan=4, style=header_style)])] +
    # Encabezados de columna
    [html.Tr([
        html.Th('Escala:', style=cell_style),
        html.Th('↗Elevado', style=verde),
        html.Th('→Medio', style=amarillo),
        html.Th('↘Deficiente', style=rojo)
    ])] +
    # Filas de datos
   [
        html.Tr(
                [
                    html.Th("WAF (Web Application Firewall)", style=cell_style,colSpan=3),
                    html.Th("**DETECTADO**", colSpan=1, style=verde)
                ]
            ),
        html.Tr(
                [
                    html.Th("Software / Hardware y/o configuraciones de Seguridad", style=cell_style,colSpan=3),
                    html.Th("↗Elevado", colSpan=1, style=verde)
                ]
            )
    ],
    # Estilo de la tabla
    style=table_style
)
carddiagnosticogeneralMovil=html.Div([
             html.H5(["Diagnóstico de Evaluación General de los Ciclos"], className="text-center"),
             html.P("Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet.", className="text-justify" ), 
         ]
         )
carddiagnosticogeneraldetalladoMovil=html.Div([
             html.H5(["Diagnóstico General"], className="text-center"),
             html.P("Adipisicing esse ea occaecat velit ex culpa. Cillum fugiat anim et adipisicing labore. Ullamco velit anim et elit nostrud. Esse labore est esse ad commodo excepteur sit magna do quis. Ad ipsum pariatur qui aute sit amet.", className="text-center" ),
             html.Div([tableANÁLISISEJECUTIVORIESGOMovil], style={'margin': 'auto', 'width': '50%'}),
             html.Div([tableEVALUACIONDENIVELDESEGURIDADGENERALMovil], style={'margin': 'auto', 'width': '50%', "margin-top": "20px"}),
             html.Div([tableNIVELESDEEFECTIVIDADDESOFTWAREYHARDWAREDESEGURIDADMovil], style={'margin': 'auto', 'width': '50%', "margin-top": "20px"}),
             html.Table(style={'position': 'absolute', 'top': '50%', 'transform': 'translateY(-50%)'})

         ]
         )


#Layout
Es_CicloDeEvaluacionMovil = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Ciclo de Evaluacion Móvil"], className="text-center"),                    
                ],style={"text-align": "center"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
        dbc.Col(
            html.Div(
                [
                     html.Div(
                        [company, image],),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=2


        ), 
       #Tabla "Ciclos de Evaluación"
        dbc.Row([
            dbc.Col(html.Div([
             html.Div([dbc.Card(
                 dbc.CardBody(cardciclodeevaluacionwebTABLAMovil), className="mb-3"    
        ),
    ]
)
         ], style={"margin-left": "-120px"}
         )
         )],
         ),
        

        #Grafica
        dbc.Row([
            dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(cardgracicocilodeevaluacionMovil), style={"background-color": "rgb(204, 209, 209)"}         
        ),
    ]
)  

         ], style={"margin-left": "-220px"}
         ), width=6
         ),
         #Diagnóstico de Evaluación General de los Ciclos
        dbc.Col(html.Div([
                html.Div([dbc.Card(
                 dbc.CardBody(carddiagnosticogeneralMovil), style={"background-color": "rgb(204, 209, 209)"}    
        ),
    ]
)  

         ]
         ), width=6
         ),
         
    #Diagnostico general
       dbc.Row([
    dbc.Col(
        html.Div([
            html.Div([
                carddiagnosticogeneraldetalladoMovil
               
            ])
        ]), 
        width=12
    )
])


    
    ], justify="center",
)


    
    
    ], justify="center",
)
#________________________________________________________________________________________________
#prueba


#layout
Es_PosturaDeSeguridadMovil = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Postura de Seguridad Móvil"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), html.Div(
    children=[
        html.H1('Mi Aplicación Dash'),
        
    ]
)
        
    
    ], justify="center",
)

Es_TopDeVulnerabilidadesMovil= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top deVulnerabilidades Móvil"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_TopDeRiesgoMovil= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top de Riesgo Móvil"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_TopMITREMovil= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top MITRE ATT&CK Móvil"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_Top10OWASPMovil= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top 10 OWASP Móvil"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_Recomendacion_Mitigacion_Movil= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Recomendación y Mitigación Móvil"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)
##APIs
Es_CicloDeEvaluacionApis = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Ciclo de Evaluación Apis"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_PosturaDeSeguridadApis = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Postura de Seguridad APIs"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_TopDeVulnerabilidadesApis= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top deVulnerabilidades APIs"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_TopDeRiesgoApis= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top de Riesgo Apis"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_TopMITREApis= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top MITRE ATT&CK APIs"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_Top10OWASPApis= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Top 10 OWASP APIs"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_Recomendacion_Mitigacion_Apis= dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Recomendación y Mitigación APIs"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

##DDBB
Es_CicloDeEvaluacionDDBB = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Ciclo de Evaluación DDBB"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)

Es_PosturaDeSeguridadDDBB = dbc.Row(
    [

         dbc.Col(
            html.Div(
                [
                    html.H2(["Postura de Seguridad DDBB"], className="text-center"),
                     html.Div(
                        [company, image],
                        className="d-flex justify-content-end align-items-center"),
                    
                ],style={"display": "flex", "justify-content": "space-between", "width": "100%"}
                
                #style={"margin-top": "50px"}   Añade un margen superior a la columna 1
            ), width=10

        ), 
    
    ], justify="center",
)


#_______________________________________________________________________________________________________________________
##Funciones de pantallas 
def gestion_del_servicio():
    return html.Div([
        GestiondelServicio
    ])

#Aplicacion Web
def ciclo_Evaluacion_Web():
    return html.Div([
        Es_CicloDeEvaluacionWeb
    ])

def postura_de_seguridad_web():
    return html.Div([
        Es_PosturaDeSeguridadWeb
    ])

def top_vulnerabilidades_web():
    return html.Div([
        Es_TopDeVulnerabilidadesWeb
    ])

def top_Riesgo_web():
    return html.Div([
        Es_TopDeRiesgoWeb
    ])

def top_Mitre_web():
    return html.Div([
        Es_TopMITREWeb
    ])

def top_Top10OWASP_Web():
    return html.Div([
        Es_Top10OWASPWeb
    ])

def recomendacion_Mitigacion_Web():
    return html.Div([
        Es_Recomendacion_Mitigacion_Web
    ])

#Aplicacion Movil
def ciclo_Evaluacion_Movil():
    return html.Div([
        Es_CicloDeEvaluacionMovil
    ])

def postura_de_seguridad_Movil():
    return html.Div([
        Es_PosturaDeSeguridadMovil
    ])

def top_vulnerabilidades_Movil():
    return html.Div([
        Es_TopDeVulnerabilidadesMovil
    ])

def top_Riesgo_Movil():
    return html.Div([
        Es_TopDeRiesgoMovil
    ])

def top_Mitre_Movil():
    return html.Div([
        Es_TopMITREMovil
    ])

def top_Top10OWASP_Movil():
    return html.Div([
        Es_Top10OWASPMovil
    ])

def recomendacion_Mitigacion_Movil():
    return html.Div([
        Es_Recomendacion_Mitigacion_Movil
    ])

#Aplicacion APIs
def ciclo_Evaluacion_Apis():
    return html.Div([
        Es_CicloDeEvaluacionApis
    ])

def postura_de_seguridad_Apis():
    return html.Div([
        Es_PosturaDeSeguridadApis
    ])

def top_vulnerabilidades_Apis():
    return html.Div([
        Es_TopDeVulnerabilidadesApis
    ])

def top_Riesgo_Apis():
    return html.Div([
        Es_TopDeRiesgoApis
    ])

def top_Mitre_Apis():
    return html.Div([
        Es_TopMITREApis
    ])

def top_Top10OWASP_Apis():
    return html.Div([
        Es_Top10OWASPApis
    ])

def recomendacion_Mitigacion_Apis():
    return html.Div([
        Es_Recomendacion_Mitigacion_Apis
    ])

#DDBB
def ciclo_Evaluacion_DDBB():
    return html.Div([
        Es_CicloDeEvaluacionDDBB
    ])

def postura_de_seguridad_DDBB():
    return html.Div([
        Es_PosturaDeSeguridadDDBB
    ])
