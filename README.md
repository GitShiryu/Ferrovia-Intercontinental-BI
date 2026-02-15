# 🌎 Ferrovia Intercontinental - Dashboard Logístico

### Sistema de Monitoramento de Tráfego e Custos (Rota das Américas)

Este projeto é uma solução proprietária de **Business Intelligence (BI)** desenvolvida em **Python** para simular e resolver gargalos de visualização em grandes malhas ferroviárias internacionais.

O sistema monitora uma rota fictícia que conecta o **Brasil ao Canadá**, passando por Argentina, Chile, Peru, Colômbia, Panamá, México e EUA.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)

## 🎯 O Problema
Em operações logísticas de escala continental, a dependência de planilhas estáticas e a rigidez de ERPs tradicionais dificultam a tomada de decisão rápida. Gestores precisam visualizar gargalos de consumo e custos em tempo real, cruzando fronteiras e moedas.

## 💡 A Solução
Um Dashboard Web Interativo (Dark Mode) que atua como camada de inteligência:
- **Monitoramento Global:** Visualização da rota completa (Sul ➔ Norte).
- **Análise de Tendência:** Algoritmos que projetam a evolução mensal (Jan-Dez) de cada terminal.
- **Gestão de Custos:** Breakdown automático de despesas (Combustível, Manutenção e Pessoal).

## 🛠️ Tecnologias
- **Python:** Processamento de dados (Backend).
- **Dash & Plotly:** Interface analítica interativa.
- **Pandas/NumPy:** Modelagem estatística e tratamento de dados.

- ## ⚙️ Arquitetura de Integração (Simulação)
Embora este portfólio utilize dados estáticos por segurança, o código foi estruturado com princípios de **ETL (Extract, Transform, Load)** para ambientes corporativos:

1.  **Camada de Ingestão:** O script aceita entrada de arquivos `.csv` (padrão SAP/ERP) ou conexão via API Rest.
2.  **Processamento (Pandas):**
    - Limpeza de dados nulos.
    - Tipagem de variáveis (Data, Float, String).
    - Criação de colunas calculadas (KPIs de Custo x Km).
3.  **Visualização (Front-end):** O Dash consome apenas os dados já tratados, garantindo performance leve para o usuário final.

---
*Projeto desenvolvido para portfólio de Data Science e Logística.*
