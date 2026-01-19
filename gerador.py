import csv  # Importamos a biblioteca que sabe lidar com arquivos de planilhas (CSV)

# Criamos uma lista de listas. Cada lista interna é uma 'linha' da nossa tabela.
dados_clientes = [
    ["Guilherme Silva", "1001-X", "4500.00", "Investimentos"],
    ["Mariana Souza", "2002-5", "8200.00", "Tecnologia"],
    ["Ricardo Nunes", "3003-9", "1500.00", "Culinária"],
    ["Beatriz Rocha", "4004-1", "12500.00", "Viagens"]
]

# 'with open' abre o arquivo. 
# 'w' significa WRITE (escrever). 
# 'newline=""' serve para não pular linhas extras entre os dados.
# 'encoding="utf-8"' garante que acentos (como em 'Culinária') apareçam certo.
with open('clientes_origem.csv', 'w', newline='', encoding='utf-8') as arquivo:
    
    # Criamos um objeto 'escritor' que vai traduzir nossos dados para o formato CSV
    escritor = csv.writer(arquivo)
    
    # Escrevemos a primeira linha (o cabeçalho)
    escritor.writerow(["Nome", "Conta", "Cartao_Limite", "Interesse"]) 
    
    # Escrevemos todas as linhas de dados de uma vez só
    escritor.writerows(dados_clientes)

print("Arquivo 'clientes_origem.csv' criado com sucesso!")