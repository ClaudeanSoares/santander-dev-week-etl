# 🚀 Santander Dev Week 2023 - Pipeline ETL Resiliente com Python

## 📝 Sobre o Projeto
Este projeto foi desenvolvido como parte do desafio Santander Dev Week. O objetivo original era consumir uma API de clientes, transformar os dados usando IA e devolver as informações para a API.

**O Diferencial:** Devido à indisponibilidade da API original, decidi arquitetar uma solução **local e independente**. Em vez de apenas desistir do projeto, criei um fluxo de dados (ETL) que processa arquivos CSV e utiliza lógica de negócios condicional para simular o comportamento de uma IA Generativa de forma eficiente.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Pandas:** Para manipulação e análise de dados de alto desempenho.
- **Lógica de Programação:** Estruturação modular em funções (Clean Code).

## ⚙️ O Pipeline ETL

### 1. Extract (Extração)
Os dados são lidos de um arquivo `clientes_origem.csv`, simulando a extração de um banco de dados legado. Usei o Pandas para garantir que o processo seja rápido e seguro.

### 2. Transform (Transformação)
Criei um motor de regras que gera mensagens personalizadas baseadas no **perfil financeiro** do cliente (Limite do Cartão) e em seus **interesses**. 
- Clientes com limite alto recebem ofertas de investimentos VIP.
- Clientes em crescimento recebem mensagens de incentivo e educação financeira.

### 3. Load (Carregamento)
O resultado enriquecido é exportado para um novo arquivo `santander_marketing_final.csv`, pronto para ser utilizado pela equipe de marketing ou disparado via sistema de e-mail.

## 🚀 Como Executar
1. Clone o repositório.
2. Certifique-se de ter o Python e o Pandas instalados: `pip install pandas`.
3. Execute o script principal: `python pipeline_etl.py`."# santander-dev-week-etl."  
"# santander-dev-week-etl."  
Obrigado Senhor!
