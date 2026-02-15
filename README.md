# 🛡️ Sistema de Inteligência Operacional e Segurança Ferroviária

### Solução de Monitoramento de Ativos Críticos e Prevenção de Riscos (Rota Intercontinental)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen) ![Focus](https://img.shields.io/badge/Foco-Seguran%C3%A7a_Operacional-red)

Este projeto é uma solução proprietária de **Engenharia de Dados e Business Intelligence** desenvolvida em **Python**.

O sistema simula o monitoramento de uma malha ferroviária internacional (Brasil-Canadá), focando não apenas na visualização, mas na **lógica de segurança**, estruturação de dados e detecção de anomalias operacionais.

---

## 📸 Visualização do Projeto

### 1. Painel de Controle (Dashboard)
Visualização executiva para tomada de decisão em tempo real sobre a frota e custos.
![Visão do Dashboard](dashboard_preview.png)

---

## 🎯 O Desafio de Negócio
Em grandes operações ferroviárias, a segurança e a eficiência dependem da capacidade de cruzar dados de diferentes fontes (ERPs, Sensores, Planilhas de Manutenção).
O objetivo deste projeto foi eliminar silos de informação e criar uma **camada de inteligência** capaz de:
1. Centralizar dados dispersos.
2. Identificar desvios de padrão (consumo/custo) que indicam risco mecânico.
3. Apoiar a decisão rápida para prevenção de acidentes e perdas.

---

## 💡 A Solução Técnica (Motor de Regras & Lógica)

O diferencial deste projeto não é apenas o visual, mas o **backend lógico** que valida os dados antes da exibição.

### 2. Lógica de Segurança (Bastidores)
Trecho do código (`regras_negocio.py`) onde são processadas as regras de auditoria e prevenção de acidentes:
![Lógica de Segurança no VS Code](codigo_logica.png)

### Camadas do Sistema:
1.  **Engenharia de Dados (ETL):**
    - Script Python preparado para ler arquivos legados (`.csv`, `.xlsx`) ou conectar via API.
    - Limpeza automática de dados inconsistentes e tipagem forte.

2.  **Motor de Regras de Negócio:**
    - **Alerta de Fadiga:** Identificação automática de jornadas acima do limite seguro.
    - **Anomalia de Consumo:** Detecção de desvios que sinalizam falhas mecânicas iminentes (Manutenção Preditiva).

3.  **Visualização (Front-end):**
    - Painel Web interativo desenvolvido com **Dash & Plotly**.

---

## ⚙️ Tecnologias Utilizadas
O projeto prioriza performance e lógica robusta, essenciais para ambientes de Segurança Operacional.

- **Linguagem:** Python 3.10 🐍
- **Processamento:** Pandas & NumPy (Estatística e validação).
- **Visualização:** Dash & Plotly (Front-end analítico).
- **Conceitos Aplicados:** ETL, Data Cleaning, Regras de Negócio, Automação.

---

## 🚀 Como Executar o Projeto
Para rodar o projeto, execute os comandos abaixo sequencialmente no seu terminal:

```bash
# 1. Clonar o Repositório
git clone [https://github.com/GitShiryu/Ferrovia-Intercontinental-BI.git](https://github.com/GitShiryu/Ferrovia-Intercontinental-BI.git)

# 2. Instalar Dependências
pip install -r requirements.txt

# 3. Executar a Aplicação
python dashboard_ferrovia.py

*Desenvolvido por Rômulo | Foco em Soluções Digitais, Automação e Segurança Operacional.*

