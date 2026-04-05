# Price Comparison Bot - Mercado Livre

Bot de automação web desenvolvido em **Python + Playwright** para pesquisar produtos no Mercado Livre, capturar os **5 primeiros resultados exibidos na busca** e exportar os dados para Excel.

---

## Funcionalidades
- Pesquisa de produto digitado pelo usuário
- Automação web com Playwright
- Espera inteligente do carregamento do DOM
- Captura de nome e preço dos produtos
- Exportação automática para Excel (`produtos.xlsx`)
- Estrutura modularizada
- Tratamento de erros

---

## Tecnologias
- Python
- Playwright
- OpenPyXL
- Excel
- Web Scraping
- Automação Web

---

## Estrutura
```bash
web-automation-bot-playwright/
│
├── main.py
├── bot.py
├── excel.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Como executar
1. Instale as dependências:

```bash
pip install -r requirements.txt
playwright install
```

2. Rode o projeto:

```bash
python main.py
```

3. Digite o produto desejado:

```text
iphone 17
```

4. O resultado será salvo em:

```text
produtos.xlsx
```

---

## Objetivo do projeto
Este projeto foi desenvolvido com foco em aprendizado prático de automação e comparação de preços em marketplaces.

### Habilidades aplicadas
- automação web com Playwright
- web scraping
- manipulação de listas e dicionários
- exportação de dados para Excel
- comparação de preços
- tratamento de tempo de carregamento do DOM
- integração com marketplace

---

## Próximas melhorias
- Integração com Amazon
- Ordenação global dos menores preços
- Comparação entre múltiplos marketplaces
- Histórico de consultas
- Dashboard de preços

---

## Autor
**Marcelo Carvalho Batista**  
Estudante de Análise e Desenvolvimento de Sistemas com foco em back-end, automação e soluções para e-commerce.
