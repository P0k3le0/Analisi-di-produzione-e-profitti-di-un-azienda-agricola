#Importa pacchetti
from dash import Dash, dcc, html, Input, Output, callback, dash_table, no_update
import pandas as pd
import plotly.express as px
import random as ran
import dash_bootstrap_components as dbc

#Incorpora dati
df1 = pd.read_csv('Bernardone_Leo_0312200721_random.txt')
#Inizializza App
dex = Dash(title='Analisi aziendale',external_stylesheets=[dbc.themes.UNITED])
ProfittiTot = float(df1.iloc[12,2])
SpeseTot = float(df1.iloc[11,2])
# App layout
dex.layout = [
    html.H1('''Analisi di produzione e profitti di un'azienda agricola''',style={'textAlign':'center','color':'rgb(0,0,0)',
                                              'font-family':'Aptos','font-size':'50px'}),
    html.H3('''Questo programma aiuta con la visualizzazione delle varie quantità di prodotti,spese sostenute e profitti raccolti
    all'interno della vostra azienda''',
            style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Aptos',
                   'font-size':'20px','font-weight':'normal','padding-left':'20px'}),
    #AGGIUNGI TEMPI DI PRODUZIONE
    html.Div([
        #Tabella dati atmosferici
        html.Div([dash_table.DataTable(id='DatiAtmosferici',
        columns=([{'id': 'Dati', 'name': 'Dati Atmosferici'}]+[{'id':'numeri','name':''}]),
        data=([{'Dati':'Umidità','numeri':str(df1.iloc[8,2])+' %'},
               {'Dati':'Temperatura media annua','numeri':str(df1.iloc[9,2])+'° C'},
               {'Dati':'Precipitazioni medie annue','numeri':str(df1.iloc[10,2])+' mm'}]),
        style_cell={'textAlign': 'left'},style_as_list_view=False,
        style_header={'font-family':'Times new roman','font-size':'15'},
        style_table={'maxWidth':'99%'},
        editable=False, page_size=10)], style={'width': '30%',  'display': 'inline-block','padding-left':'10px'}),
        #Tabella tempo produzione
        html.Div([dash_table.DataTable(id='TempoProduzione',
        columns=([{'id': 'Prodot', 'name': 'Prodotto'}]+[{'id': 'Tempi', 'name': 'Tempi di produzione'}]+
                 [{'id':'efficienza','name':'Efficienza'}]+[{'id':'peso','name':'Peso prodotto'}]),
        data=([{'Prodot':'Grano','Tempi':'6/10 mesi','efficienza':str(df1.iloc[1,2])+'%','peso':str(df1.iloc[1,1])+'Kg'},
               {'Prodot':'Fieno','Tempi':'4/5 settimane','efficienza':str(df1.iloc[3,2])+'%','peso':str(df1.iloc[3,1])+'Kg'},
               {'Prodot':'Uva','Tempi':'12 mesi','efficienza':str(df1.iloc[4,2])+'%','peso':str(df1.iloc[4,1])+'Kg'},
               {'Prodot':'Uova','Tempi':'5/10 giorni','efficienza':'--','peso':str(df1.iloc[0,1])},
               {'Prodot':'Carne bovina','Tempi':'2/4 anni','efficienza':'--','peso':str(df1.iloc[2,1])+'Kg'},
               {'Prodot':'Avena','Tempi':'8/10 mesi','efficienza':str(df1.iloc[5,2])+'%','peso':str(df1.iloc[5,1])+'Kg'},
               {'Prodot':'Quadrifolgi','Tempi':'2/3 mesi','efficienza':str(df1.iloc[6,2])+'%','peso':str(df1.iloc[6,1])+'Kg'}
               ]),
        style_cell={'textAlign': 'left'},style_as_list_view=False,
        style_header={'font-family':'Times new roman','font-size':'15'},
        style_table={'maxWidth':'99%'},
        editable=False, page_size=10)], style={'width':'70%','display':'inline-block'}),
    ]),
    html.H4('''La percentuale di Efficienza mostrata su questa tabella è calcolata a partire dalla percentuale di
    umidità rilevata per la zona in cui si trova l'azienda''',
            style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Aptos',
                   'font-size':'15px','font-weight':'normal','padding-top':'20px'}),
    html.H4('''Il tempo di produzione mostrato su questa tabella è basato sul tempo medio di produzione del prodotto e
    potrebbe variare da situazione a situazione''',
            style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Aptos',
                   'font-size':'15px','font-weight':'normal','padding-top':'10px'}),
    #istogramma 1
    html.H2('Quantità di Prodotti',style={'textAlign':'','color':'rgb(50,50,50)',
                                          'font-familiy':'Sans serif','font-size':'30px','font-weight':'bold','padding-left':'20px'}),
    html.H3('Questo grafico rappresenta la quantità di prodotti raccolti per la vendita',
            style={'color':'rgb(0,0,0)','font-familiy':'Sans serif','font-size':'20px','font-weight':'normal','padding-left':'20px'}),
    dcc.RadioItems(id='RadioProd',options=[#scelta colori 1
    {'label':'Arancione','value':'Orange'},{'label':'Verde','value':'Green'},{'label':'Blu','value':'Blue'},{'label':'Rosso','value':'Red'}],value='Orange',
                   style={'color':'#000000','padding-left':'30px'},inline=True),
    dcc.Graph(id='Prodotti',figure={}),
    #istogramma 2
    html.H2('Spese sostenute',style={'color':'rgb(50,50,50)',
                                          'font-familiy':'Sans serif','font-size':'30px','font-weight':'bold','padding-left':'20px'}),
    html.H3('Questo grafico rappresenta le spese sostenute per il mantenimento della produzione aziendale',
            style={'color':'rgb(0,0,0)','font-familiy':'Sans serif','font-size':'20px','font-weight':'normal','padding-left':'20px'}),
    dcc.RadioItems(id='RadioProdu',options=[#scelta colori 2
    {'label':'Arancione','value':'Orange'},{'label':'Verde','value':'Green'},{'label':'Blu','value':'Blue'},{'label':'Rosso','value':'Red'}],value='Red',
                   style={'color':'#000000','padding-left':'30px'},inline=True),
    dcc.Graph(id='Produzione',figure={}),
    html.Div([#toast spese
        dbc.Button('Spesa complessiva',id='Spese-toggle',color='danger',n_clicks=0,size='lg'),
        dbc.Toast([html.P(f'{SpeseTot} euro')],id="Spese-toast",header='Le spese sostenute equivalgono a: ',icon='danger',
                  dismissable=True,is_open=False,header_style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Sans serif',
                   'font-size':'15px','font-weight':'normal'},body_style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Sans serif',
                   'font-size':'15px','font-weight':'normal'},style={"position": "fixed", "top": 66, "right": 50, "width": 350}),
        ],className="d-grid gap-2 col-6 mx-auto"),
    #isto? 3
    html.H2('Profitti raccolti',style={'textAlign':'','color':'rgb(50,50,50)',
                                          'font-familiy':'Sans serif','font-size':'30px','font-weight':'bold','padding-left':'20px'}),
    html.H3('Questo grafico rappresenta i profitti fruttati dai vari prodotti e attività esterne',
            style={'color':'rgb(0,0,0)','font-familiy':'Sans serif','font-size':'20px','font-weight':'normal','padding-left':'20px'}),
    dcc.RadioItems(id='RadioProf',options=[
        {'label':'Arancione','value':'Orange'},{'label':'Verde','value':'Green'},{'label':'Blu','value':'Blue'},{'label':'Rosso','value':'Red'}],value='Green',
                   style={'color':'#000000','padding-left':'30px'},inline=True),
    dcc.Graph(id='Profitti',figure={}),
    html.Div([#toast profitti
        dbc.Button('Profitti totali',id='Profitti-toggle',color='success',n_clicks=0,size='lg'),
        dbc.Toast([html.P(f'{ProfittiTot} euro')],id="Profitti-toast",header='I profitti raccolti equivalgono a: ',icon='success',
                  dismissable=True,is_open=False,header_style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Sans serif',
                   'font-size':'15px','font-weight':'normal'},body_style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Sans serif',
                   'font-size':'15px','font-weight':'normal'},style={"position": "fixed", "top": 200, "right": 50, "width": 350}),
        ],className="d-grid gap-2 col-6 mx-auto"),
    html.H4('''Questo programma non supporta una completa sostituzione dell'input umano
    e quanto tale è da utilizzare come strumento supplementare e non come analisi a sé stante.''',
            style={'color':'rgb(0,0,0)','textAlign':'center','font-familiy':'Aptos',
                      'font-size':'12px','font-weight':'normal','padding-top':'20px','padding-bottom':'20px'})
    
]

@callback(
    Output(component_id='Prodotti',component_property='figure'),
    Input(component_id='RadioProd',component_property='value'))
def update_prodotti(colore):
    fig=px.histogram(df1[1:6],x='Prodotti', y='Quantità prodotti',color_discrete_sequence=[colore])
    return fig

@callback(
    Output(component_id='Produzione',component_property='figure'),
    Input(component_id='RadioProdu',component_property='value'))
def update_spese(colore):
    fig=px.histogram(df1[8:17],x='Prodotti',y='Quantità prodotti',color_discrete_sequence=[colore],
                                            labels={
                                                'Prodotti':'Tipo di spesa',
                                                'Quantità prodotti':'Spesa sostenuta'})
    return fig

@callback(
    Output("Spese-toast", "is_open"),
    [Input("Spese-toggle", "n_clicks")],
)
def apri_spese(n):
    if n == 0:
        return no_update
    return True

@callback(
    Output(component_id='Profitti',component_property='figure'),
    Input(component_id='RadioProf',component_property='value'))
def update_profitti(colore):
    fig=px.histogram(df1[18:27],x='Prodotti',y='Quantità prodotti',color_discrete_sequence=[colore],
                                            labels={
                                                'Prodotti':'Fonte di profitto',
                                                'Quantità prodotti':'Quantità raccolta'},)
    return fig

@callback(
    Output("Profitti-toast", "is_open"),
    [Input("Profitti-toggle", "n_clicks")],
)
def apri_profitti(n):
    if n == 0:
        return no_update
    return True

#Avvio app
if __name__ == '__main__':
    dex.run(debug=False)

#template='plotly_dark'
