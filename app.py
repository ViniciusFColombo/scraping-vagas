from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

navegador = webdriver.Chrome()

endereco_principal = "https://br.indeed.com/jobs?q="
nome_vaga = "Python"
local = "&l=Remoto"

pesquisar = endereco_principal + nome_vaga + local

print(pesquisar)

navegador.get(pesquisar)

WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".job_seen_beacon"))
)

vagas = navegador.find_elements(By.CSS_SELECTOR, ".job_seen_beacon")

print("Quantidade de vagas encontradas:", len(vagas))

vagas_encontradas = []

for vaga in vagas:

    try:
        titulo = vaga.find_element(By.CSS_SELECTOR, "h2").text
        empresa = vaga.find_element(By.CSS_SELECTOR, "[data-testid='company-name']").text
        local = vaga.find_element(By.CSS_SELECTOR, "[data-testid='text-location']").text
        id_vaga = vaga.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("data-jk")

        link = f"https://br.indeed.com/viewjob?jk={id_vaga}"

        if titulo and empresa:
            vagas_encontradas.append({
                "Titulo": titulo,
                "Empresa": empresa,
                "Local": local,
                "Link": link
            })

    except:
        pass

arquivo = pd.DataFrame(vagas_encontradas)

arquivo.to_excel("VagasIndeed.xlsx", index=False)

print("Arquivo Excel gerado com sucesso!")

navegador.quit()