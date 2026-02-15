🛡️ Sistema de Inteligência Operacional e Segurança Ferroviária
Solução de Monitoramento de Ativos Críticos e Prevenção de Riscos (Rota Intercontinental)
Este projeto é uma solução proprietária de Engenharia de Dados e Business Intelligence desenvolvida em Python.

O sistema simula o monitoramento de uma malha ferroviária internacional (Brasil-Canadá), focando não apenas na visualização, mas na lógica de segurança, estruturação de dados e detecção de anomalias operacionais.

🎯 O Desafio de Negócio
Em grandes operações ferroviárias, a segurança e a eficiência dependem da capacidade de cruzar dados de diferentes fontes (ERPs, Sensores, Planilhas de Manutenção). O objetivo deste projeto foi eliminar silos de informação e criar uma camada de inteligência capaz de:

Centralizar dados dispersos.

Identificar desvios de padrão (consumo/custo) que indicam risco mecânico.

Apoiar a decisão rápida para prevenção de acidentes e perdas.

💡 A Solução Técnica (Além do Dashboard)
O sistema foi arquitetado em três camadas para garantir integridade e escalabilidade:

1. Camada de Engenharia de Dados (ETL)
Ingestão: Script Python preparado para ler arquivos legados (.csv, .xlsx) ou conectar via API.

Tratamento: Limpeza automática de dados inconsistentes e tipagem forte (garantindo que datas e valores numéricos sejam processados corretamente).

Regras de Negócio:

Cálculo de Desvio: Algoritmo que compara o realizado vs. planejado.

Auditoria de Custos: Validação automática de lançamentos de manutenção.

2. Camada de Visualização e Decisão
Um Painel Web Interativo (Dark Mode) desenvolvido com Dash & Plotly:

Monitoramento Geográfico: Rastreabilidade de ativos em rota crítica.

Análise de Tendência: Curvas de evolução mensal para prever desgaste e demanda.

Breakdown de Custos: Visão granular de Combustível, Pessoal e Manutenção Preventiva.

⚙️ Arquitetura e Tecnologias
O projeto prioriza performance e lógica robusta, essenciais para ambientes de Segurança Operacional.

Linguagem: Python 3.10 🐍

Processamento: Pandas & NumPy (Para estatística e validação de regras).

Visualização: Dash & Plotly (Front-end analítico).

Conceitos Aplicados: ETL, Data Cleaning, Regras de Negócio, Automação.

🚀 Como Executar o Projeto
Clone o repositório:

Bash
git clone https://github.com/GitShiryu/Ferrovia-Intercontinental-BI.git
Instale as dependências:

Bash
pip install -r requirements.txt
Execute a aplicação:

Bash
python dashboard_ferrovia.py
Desenvolvido por Rômulo | Foco em Soluções Digitais, Automação e Segurança Operacional.