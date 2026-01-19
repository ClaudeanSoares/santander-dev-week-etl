import pandas as pd
import random

# --- CONFIGURAÇÕES ---
ARQUIVO_ENTRADA = 'clientes_origem.csv'
ARQUIVO_SAIDA = 'santander_marketing_final.csv'

def extrair_dados(caminho):
    """Etapa 1: Extract - Recupera os dados de forma segura."""
    try:
        df = pd.read_csv(caminho)
        print(f"[INFO] {len(df)} clientes carregados com sucesso.")
        return df
    except FileNotFoundError:
        print("[ERRO] Arquivo de origem não encontrado!")
        return None

def transformar_com_ia_local(cliente):
    """Etapa 2: Transform - Lógica de geração de mensagens personalizadas."""
    nome = cliente['Nome']
    interesse = cliente['Interesse']
    limite = float(cliente['Cartao_Limite'])
    
    # Criamos variações para a IA não parecer repetitiva (Indetectável)
    introducoes = ["Olá", "Oi", "Tudo bem,", "Saudações,"]
    intro = random.choice(introducoes)
    
    if limite > 8000:
        return f"{intro} {nome}! Vimos seu perfil premium. Que tal investir em {interesse} para potencializar seu patrimônio?"
    elif limite > 3000:
        return f"{intro} {nome}. Sabia que {interesse} é uma excelente forma de proteger seu futuro? Vamos conversar?"
    else:
        return f"{intro} {nome}, comece hoje sua jornada em {interesse}. O banco Santander te ajuda a crescer!"

def carregar_dados(df, caminho):
    """Etapa 3: Load - Salva o enriquecimento de dados no destino."""
    df.to_csv(caminho, index=False, encoding='utf-8-sig')
    print(f"[SUCCESS] Pipeline finalizado. Resultados salvos em: {caminho}")

# --- EXECUÇÃO DO PIPELINE ---
if __name__ == "__main__":
    print("--- Iniciando Pipeline ETL Santander ---")
    
    # 1. Extração
    dados_clientes = extrair_dados(ARQUIVO_ENTRADA)
    
    if dados_clientes is not None:
        # 2. Transformação (Aqui simulamos o enriquecimento que a IA faria)
        print("[PROCESS] Aplicando inteligência de marketing...")
        dados_clientes['Mensagem_Marketing'] = dados_clientes.apply(transformar_com_ia_local, axis=1)
        
        # 3. Carregamento
        carregar_dados(dados_clientes, ARQUIVO_SAIDA)