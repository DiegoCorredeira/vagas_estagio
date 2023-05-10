from tkinter import * 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


def buscar_vagas():
    keyword = keyword_entry.get()
    location = location_entry.get()
    geoid = "106057199"
    URL_LINKEDIN_JOBS = f"https://www.linkedin.com/jobs/search/?&keywords={keyword}&location={location}&refresh=true"
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  # mudar
    driver.get(URL_LINKEDIN_JOBS)
    
    sleep(5)
    
    results = driver.find_elements(By.CSS_SELECTOR, '.base-card')
    
    output_text.delete(1.0, END)
    
    for i, result, in enumerate(results): 
        if i >= 10: 
            break
        
        result.click()
        sleep(15)
    
        try: 
            descricao = driver.find_element(By.CLASS_NAME, 'description').text
            titulo = driver.find_element(By.CLASS_NAME, 'topcard__title').text
            local = driver.find_element(By.CLASS_NAME, 'topcard__flavor--bullet').text
            empresa = driver.find_element(By.CLASS_NAME, 'topcard__flavor').text
            link = driver.current_url
            
            
            output_text.insert(END, f'Título: {titulo}\n')
            output_text.insert(END, f'Empresa: {empresa}\n')
            output_text.insert(END, f'Local: {local}\n')
            output_text.insert(END, f'Descrição: {descricao}\n')
            output_text.insert(END, f'Link: {link}\n')
            output_text.insert(END, f'------------------------------------------------------------------------\n')
            
            print('Vaga será exibida ao fechar navegador')
            
        except:
            print('Erro ao tentar exibir ou capturar a vaga')

    driver.quit()


root = Tk()
root.title('Buscador de vagas GUI')
root.geometry("800x400")


keyword_label = Label(root, text='Vaga: ')
keyword_label.pack()
keyword_entry = Entry(root)
keyword_entry.pack()


location_label = Label(root, text='Localidade: ')
location_label.pack()
location_entry = Entry(root)
location_entry.pack()

space_label = Label(root)
space_label.pack()

search_button = Button(root, text='Buscar', command=buscar_vagas)
search_button.config(padx=150, pady=10)
search_button.pack()

space_label = Label(root)
space_label.pack()

output_text = Text(root)
output_text.pack()


root.mainloop()