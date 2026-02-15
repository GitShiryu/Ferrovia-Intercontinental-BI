import pandas as pd

# Módulo de Auditoria e Segurança Operacional

def validar_seguranca_operacional(df):
    """
    Simula uma integração que audita dados em tempo real para prevenção de acidentes.
    """
    # Regra 1: Alerta de Fadiga/Excesso de Jornada (Foco em Segurança)
    alertas_jornada = df[df['horas_operacao'] > 12]
    
    # Regra 2: Alerta de Velocidade/Consumo Incompatível (Risco Mecânico)
    media_consumo = df['consumo_litros'].mean()
    risco_mecanico = df[df['consumo_litros'] > (media_consumo * 1.3)]

    print("--- Relatório de Auditoria de Segurança ---")
    if not alertas_jornada.empty:
        print(f"[ALERTA] {len(alertas_jornada)} ativos com jornada acima do limite de segurança.")
    
    if not risco_mecanico.empty:
        print(f"[CRÍTICO] {len(risco_mecanico)} ativos com anomalia de consumo (Possível falha).")

# Simulação de processamento de dados vindos do ERP/SAP
if __name__ == "__main__":
    # O sistema lê o dado bruto e aplica as regras antes de mandar para o Dashboard
    df_mrs = pd.read_excel('dados_ferrovia.xlsx') # Usa o seu arquivo que já existe na pasta
    validar_seguranca_operacional(df_mrs)