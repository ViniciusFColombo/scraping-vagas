# Scraper de Vagas do Indeed com Python

## 📌 Descrição

Este projeto é uma automação desenvolvida em Python que coleta vagas de emprego diretamente do site Indeed.

O script abre o site, busca por vagas relacionadas a **Python em formato remoto**, extrai as informações principais das vagas e gera automaticamente um arquivo **Excel** com os resultados.

As informações coletadas incluem:

* Título da vaga
* Empresa
* Localização
* Link direto para a vaga

O objetivo do projeto é demonstrar habilidades em **automação web, scraping de dados e manipulação de dados com Python**.

---

## 🚀 Tecnologias utilizadas

* Python
* Selenium
* Pandas
* WebDriverWait (espera dinâmica de elementos)

---

## ⚙️ Como funciona

1. O script acessa o site do Indeed
2. Realiza a busca por vagas de **Python Remoto**
3. Aguarda as vagas carregarem na página
4. Extrai as informações de cada vaga
5. Organiza os dados
6. Gera automaticamente um arquivo **Excel** com os resultados

---

## 📄 Exemplo de saída

O script gera um arquivo chamado:

```
VagasIndeed.xlsx
```

Com as seguintes colunas:

* Título
* Empresa
* Local
* Link da vaga

---

## ▶️ Como executar o projeto

1. Instale as dependências:

```
pip install selenium pandas
```

2. Execute o script:

```
app.py
```

3. O arquivo Excel será gerado automaticamente na pasta do projeto.

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte do meu portfólio para demonstrar conhecimentos em:

* Web Scraping
* Automação de tarefas
* Extração e organização de dados
* Integração com Excel

---

## 👨‍💻 Autor

Desenvolvido por Vinicius Colombo
