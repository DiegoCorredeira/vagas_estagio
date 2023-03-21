from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas as pd


'''
Proximos passos: 
Adicionar aba com link da vaga 
Implementar sistema de envio de email
Mensagem do email: 'Olá, fulano! Sua atualização diaria de vagas de estágio chegou! Venha dar uma olhada.'
'''
URL_LINKEDIN_JOBS = 'https://www.linkedin.com/jobs/search?keywords=Est%C3%A1gio%20De%20TI&location=Brasil&locationId=&geoId=106057199&f_TPR=r86400&position=1&pageNum=0'

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  

    driver.get(URL_LINKEDIN_JOBS)

    results = driver.find_elements_by_class_name('base-card')

    descricao = []
    empresa = []
    local = []
    titulo = []

    while True:
        for result in results[len(descricao):]:
            result.click()
            sleep(7)
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
        'Descrição': descricao
        }
    df = pd.DataFrame(dados_coletados)
    print(df.head())
    df.to_excel('vagas.xlsx', encoding='utf-8')
