from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd


'''
Proximos passos: 
Implementar sistema de envio de email
Mensagem do email: 'Olá, fulano! Sua atualização diaria de vagas de estágio chegou! Venha dar uma olhada.'
'''

'''
Em busca da facilidade de buscar outras vagas além de estágio em TI
adicionei essa implementação onde através dessas varáveis você consegue
gerar o link de maneira mais eficaz - João Pedro Dutra
'''

keyword = "Estagio em TI" # Nome da vaga que busca - João Pedro Dutra
location = "Brasil" # Localidade da vaga que busca - João Pedro Dutra
geoid = "106057199" # Variável fixa enquanto focar apenas no Brasil - João Pedro Dutra

URL_LINKEDIN_JOBS = f"https://www.linkedin.com/jobs/search/?geoId={geoid}&keywords={keyword}&location={location}&refresh=true"

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  

    driver.get(URL_LINKEDIN_JOBS)

    results = driver.find_elements_by_class_name('base-card')
    links = driver.find_elements_by_class_name('base-card')

    descricao = []
    empresa = []
    local = []
    titulo = []
    job_links = [link.get_attribute('href') for link in links]


    while True:
        for result in results[len(descricao):]:
            result.click()
            sleep(15)
            try:
                descricao.append(
                    driver.find_element_by_class_name('description').text)
                titulo.append(
                    driver.find_element_by_class_name('topcard__title').text)
                local.append(driver.find_element_by_class_name(
                    'topcard__flavor--bullet').text)
                empresa.append(
                    driver.find_element_by_class_name('topcard__flavor').text)
                print('Vaga salva com sucesso!')
            except:
                print("Erro ao capturar dados da vaga selecionada")
        try:
            results = driver.find_elements_by_class_name('base-card')
        except:
            driver.find_element_by_xpath(
                '//*[@id="main-content"]/section[2]/button').click()
            results = driver.find_elements_by_class_name('base-card')

        if len(descricao) == len(results):
            break
    


    driver.quit()

    dados_coletados = {
        'Título': titulo,
        'Empresa': empresa,
        'Local da Vaga': local,
        'Descrição': descricao, 
        'Link': job_links
        }
    df = pd.DataFrame(dados_coletados)
    print(df.head())
    df.to_excel('vagas.xlsx', encoding='utf-8')
