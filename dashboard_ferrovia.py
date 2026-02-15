import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import numpy as np

# --- 1. DADOS (Mantido igual) ---
rota_ordenada = [
    'Juiz de Fora (BRA)', 'Congonhas (BRA)', 'Horto (BRA)', 'Volta Redonda (BRA)', 'Barra Mansa (BRA)', 'Itaguaí (BRA)', 'São Paulo (BRA)', 'Uruguaiana (BRA)',
    'Buenos Aires (ARG)', 'Mendoza (ARG)', 'Valparaíso (CHI)', 'Antofagasta (CHI)',
    'Lima (PER)', 'Bogotá (COL)', 'Cidade do Panamá (PAN)',
    'Veracruz (MEX)', 'Cidade do México (MEX)', 'Monterrey (MEX)', 'Laredo (EUA)', 'Kansas City (EUA)', 'Chicago (EUA)', 'Nova York (EUA)', 'Toronto (CAN)', 'Vancouver (CAN)'
]

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
dados_lista = []
np.random.seed(42)

for cidade in rota_ordenada:
    base_consumo = np.random.randint(200, 800)
    fator_manut = np.random.uniform(0.20, 0.40)
    fator_pessoal = np.random.uniform(0.40, 0.60)
    
    for i, mes in enumerate(meses):
        variacao = np.random.randint(-50, 150) + (i * 10)
        consumo_mes = base_consumo + variacao
        custo_manut = consumo_mes * (fator_manut + np.random.uniform(-0.05, 0.05))
        custo_pessoal = consumo_mes * (fator_pessoal + np.random.uniform(-0.05, 0.05))
        
        dados_lista.append({
            'Localizacao': cidade,
            'Mes': mes,
            'Ordem_Mes': i,
            'Consumo': consumo_mes,
            'Custo_Manutencao': custo_manut,
            'Custo_Pessoal': custo_pessoal
        })

df_completo = pd.DataFrame(dados_lista)

# --- 2. INICIALIZAÇÃO ---
app = dash.Dash(__name__)
server = app.server

# --- 3. LAYOUT ---
app.layout = html.Div(style={'backgroundColor': '#0f0f0f', 'color': '#e0e0e0', 'padding': '20px', 'minHeight': '100vh', 'fontFamily': 'Segoe UI, sans-serif'}, children=[
    
    html.Div([
        html.H1("FERROVIA INTERCONTINENTAL", style={'textAlign': 'center', 'color': '#00BFFF', 'letterSpacing': '2px', 'textTransform': 'uppercase', 'marginBottom': '5px'}),
        html.H4("Analytics & Inteligência de Tráfego", style={'textAlign': 'center', 'color': '#aaaaaa', 'fontWeight': 'normal', 'marginTop': '0'})
    ], style={'marginBottom': '30px'}),
    
    html.Div([
        html.Label("Selecionar Visão:", style={'fontWeight': 'bold', 'fontSize': '16px', 'color': '#00BFFF'}),
        dcc.Dropdown(
            id='filtro-localizacao',
            options=[{'label': '🌎 ROTA COMPLETA (Visão Global)', 'value': 'todas'}] + 
                    [{'label': f"📍 {loc}", 'value': loc} for loc in rota_ordenada],
            value='todas',
            clearable=False,
            style={'color': '#000', 'marginTop': '8px', 'borderRadius': '5px'} 
        )
    ], style={'width': '70%', 'maxWidth': '800px', 'margin': '0 auto 30px auto'}),

    # CARTÕES
    html.Div([
        html.Div([
            html.H3(id='titulo-card-1', style={'textAlign': 'center', 'color': '#888', 'fontSize': '14px', 'textTransform': 'uppercase', 'marginTop': '0'}),
            html.H2(id='valor-card-1', style={'textAlign': 'center', 'fontSize': '42px', 'color': '#fff', 'margin': '10px 0', 'fontWeight': 'bold'})
        ], style={'backgroundColor': '#1a1a1a', 'padding': '20px', 'borderRadius': '12px', 'border': '1px solid #333', 'width': '30%', 'minWidth': '250px'}),

        html.Div([
            html.H3(id='titulo-card-2', style={'textAlign': 'center', 'color': '#888', 'fontSize': '14px', 'textTransform': 'uppercase', 'marginTop': '0'}),
            html.H2(id='valor-card-2', style={'textAlign': 'center', 'fontSize': '42px', 'color': '#FFD700', 'margin': '10px 0', 'fontWeight': 'bold'}) 
        ], style={'backgroundColor': '#1a1a1a', 'padding': '20px', 'borderRadius': '12px', 'border': '1px solid #333', 'width': '30%', 'minWidth': '250px'})

    ], style={'display': 'flex', 'justifyContent': 'center', 'gap': '20px', 'marginBottom': '30px', 'flexWrap': 'wrap'}),

    # GRÁFICOS
    html.Div([
        html.Div([
            dcc.Graph(id='grafico-principal', config={'displayModeBar': False})
        ], style={'width': '65%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingRight': '10px', 'boxSizing': 'border-box'}),

        html.Div([
            dcc.Graph(id='grafico-rosca', config={'displayModeBar': False})
        ], style={'width': '35%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingLeft': '10px', 'boxSizing': 'border-box'})
    ], style={'maxWidth': '1400px', 'margin': '0 auto', 'display': 'flex', 'flexWrap': 'wrap'})
])

# --- 4. CALLBACKS ---
@app.callback(
    [Output('titulo-card-1', 'children'),
     Output('valor-card-1', 'children'),
     Output('titulo-card-2', 'children'),
     Output('valor-card-2', 'children'),
     Output('grafico-principal', 'figure'),
     Output('grafico-rosca', 'figure')],
    [Input('filtro-localizacao', 'value')]
)
def atualizar_dashboard(unidade_selecionada):
    
    # VISÃO GLOBAL
    if unidade_selecionada == 'todas':
        df_view = df_completo.groupby('Localizacao', as_index=False)['Consumo'].sum()
        df_view['Localizacao'] = pd.Categorical(df_view['Localizacao'], categories=rota_ordenada, ordered=True)
        df_view = df_view.sort_values('Localizacao')
        
        total_acumulado = df_completo['Consumo'].sum()
        media_valor = df_view['Consumo'].mean()
        
        titulo_1 = "Consumo Total da Rede (Anual)"
        titulo_2 = "Média por Terminal"
        
        # TÍTULO EXPLÍCITO DA ROSCA
        titulo_rosca = "Distribuição de Custos (ACUMULADO ANUAL)"

        fig_principal = px.line(df_view, x='Localizacao', y='Consumo', markers=True, title="Perfil da Rota (Sul ➔ Norte)", template='plotly_dark')
        fig_principal.update_traces(line_color='#00BFFF', line_width=3, fill='tozeroy', fillcolor='rgba(0, 191, 255, 0.1)')
        fig_principal.update_layout(xaxis_tickangle=-45)

        df_custos = df_completo

    # VISÃO LOCAL
    else:
        df_view = df_completo[df_completo['Localizacao'] == unidade_selecionada].sort_values('Ordem_Mes')
        
        total_acumulado = df_view['Consumo'].sum()
        media_valor = df_view['Consumo'].mean()
        
        titulo_1 = f"Total Anual: {unidade_selecionada}"
        titulo_2 = "Média Mensal Estimada"
        
        # TÍTULO EXPLÍCITO DA ROSCA
        titulo_rosca = f"Custos: {unidade_selecionada} (ACUMULADO ANUAL)"

        fig_principal = px.line(df_view, x='Mes', y='Consumo', markers=True, title=f"Evolução Mensal: {unidade_selecionada}", template='plotly_dark')
        fig_principal.update_traces(line_color='#FFD700', line_width=4)
        
        df_custos = df_view

    # Textos dos Cards
    texto_card_1 = f"{total_acumulado:,.0f} L".replace(",", ".")
    texto_card_2 = f"{media_valor:,.0f} L".replace(",", ".")

    # Layout Gráfico Principal
    fig_principal.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#e0e0e0'}
    )
    fig_principal.update_xaxes(title_text='')
    fig_principal.update_yaxes(title_text='Litros')

    # --- GRÁFICO DE ROSCA (CUSTOMIZADO COM TÍTULO CLARO) ---
    valores_custos = {
        'Combustível': df_custos['Consumo'].sum(),
        'Manutenção': df_custos['Custo_Manutencao'].sum(),
        'Pessoal': df_custos['Custo_Pessoal'].sum()
    }
    
    # Cria o DataFrame para a Rosca para facilitar o Hover
    df_pizza = pd.DataFrame({
        'Categoria': list(valores_custos.keys()),
        'Valor_Anual': list(valores_custos.values())
    })
    # Adiciona coluna de Média Mensal para mostrar no mouse
    df_pizza['Media_Mensal'] = df_pizza['Valor_Anual'] / 12

    fig_pie = px.pie(
        df_pizza,
        names='Categoria',
        values='Valor_Anual',
        title=titulo_rosca, # Título que muda para explicar que é Anual
        hole=0.6,
        template='plotly_dark',
        color_discrete_sequence=['#FF4500', '#00BFFF', '#32CD32'],
        # Personaliza o que aparece quando passa o mouse
        hover_data=['Media_Mensal'] 
    )
    
    fig_pie.update_traces(
        textinfo='percent+label', 
        textposition='outside',
        # Formata o mouse para mostrar o valor anual e a média mensal
        hovertemplate="<b>%{label}</b><br>Anual: %{value:,.0f}<br>Média Mensal: %{customdata[0]:,.0f}"
    )
    fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False)
    
    return titulo_1, texto_card_1, titulo_2, texto_card_2, fig_principal, fig_pie

# --- 5. EXECUÇÃO ---
if __name__ == '__main__':
    app.run(debug=True)