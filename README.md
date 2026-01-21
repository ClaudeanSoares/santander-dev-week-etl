# 🏦 Santander Dev Week 2025: Ciência de Dados com Python
## Evolução de um Pipeline ETL Resiliente e Inteligente

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Tecnologia](https://img.shields.io/badge/Tecnologia-Python%20%7C%20OpenAI-blue)
![Ambiente](https://img.shields.io/badge/Ambiente-Google%20Colab%20%26%20VS%20Code-orange)

## 🌟 O Desafio
O objetivo deste projeto foi agir como um **Cientista de Dados do Santander**, desenvolvendo um pipeline ETL (Extract, Transform, Load) capaz de gerar valor real para o negócio. O foco está na personalização em massa de mensagens de marketing para investimentos, unindo automação e Inteligência Artificial.

## 💡 Meu Diferencial: Resiliência Técnica
Durante o desenvolvimento, deparei-me com desafios de ambiente e conectividade. Em vez de interromper o processo, decidi arquitetar uma solução **resiliente e independente**. Desenvolvi um fluxo de dados modular que garante o funcionamento tanto em nuvem (Google Colab) quanto localmente (VS Code), tratando erros de diretório e garantindo a integridade da fonte de dados via auto-setup.

## ⚙️ O Fluxo do Pipeline (ETL)

O projeto segue os três pilares fundamentais da Engenharia de Dados:

1.  **Extract (Extração) 🔍**
    * Consumo de dados brutos da API oficial do Santander.
    * Implementação de lógica de segurança que gera e lê arquivos `SDW2023.csv` automaticamente, evitando falhas de execução (`FileNotFoundError`).

2.  **Transform (Transformação) 🤖**
    * **IA Generativa:** Integração com a **API da OpenAI (GPT-3.5-Turbo)** para atuar como um consultor financeiro virtual.
    * **Motor de Regras:** O sistema analisa o perfil financeiro do cliente e gera recomendações exclusivas (máx. 100 caracteres) com foco em educação financeira e oportunidades de investimento.

3.  **Load (Carregamento) 🚀**
    * Atualização dos registros enriquecidos de volta na API via métodos HTTP PUT.
    * Exportação final para estruturação de relatórios prontos para uso pelas equipes de marketing.

## 🛠️ Tecnologias e Pilares
* **Python 3.13:** Base para automação e scripts.
* **Pandas:** Manipulação e análise de dados de alta performance.
* **OpenAI API:** Processamento de Linguagem Natural (NLP) para personalização.
* **Clean Code:** Organização modular em funções para garantir manutenibilidade e legibilidade profissional.

## 🚀 Como Executar o Projeto

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/ClaudeanSoares/santander-dev-week-etl.git](https://github.com/ClaudeanSoares/santander-dev-week-etl.git)
    ```
2.  **Instalar dependências:**
    ```bash
    pip install pandas requests openai
    ```
3.  **Configurar Chave de API:**
    * No Colab, utilize os `Secrets` com a chave `OPENAI_API_KEY`.
    * No VS Code, configure sua variável de ambiente local.

---

### 🖋️ Autoria e Propósito
Este projeto foi desenvolvido por **Claudean Soares**.

> "A ciência sem a virtude é uma arma para o mal." — *Santo Agostinho*

Neste projeto, a técnica foi utilizada com o propósito de criar clareza e auxílio financeiro para o próximo.

---
**Nota:** Projeto desenvolvido durante a Santander Dev Week 2025, com o auxílio de IA Generativa para a estruturação do pipeline ETL e resolução de bugs de ambiente local.

*Obrigado, Senhor!*
