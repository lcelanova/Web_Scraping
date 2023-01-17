from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/usr/local/bin/chromedriver'
s=Service(path)
driver = webdriver.Chrome(service=s)

driver.get(website)

#Busca un nodo que tenga como nombre de tag label, y dentro de ese nodo un atributo cuyo nombre sea analytics event y contenga All Matches
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

#Buscar en la lista desplegable por ID country:
dropdown = Select(driver.find_element(By.ID, 'country')) 

#En el caso de que no haya ID y solo haya class name que no es unico:
""" 
caja = driver.find_element(By.CLASS_NAME, 'panel-body')
dropdown = Select(caja.find_element(By.ID, 'country'))
"""

dropdown.select_by_visible_text('Spain')


#dejar cargar la pagina para que no de un error si la pagina tarde en cargar
time.sleep(5)

#buscar por el tag name tr(el nombre de cada fila)
matches =  driver.find_elements(By.TAG_NAME, 'tr')

partidos = []
#Meter cada uno de los partidos en la lista partidos
for match in matches:
    partidos.append(match.text)

#cerrar el driver
driver.quit()


#PANDAS
#crear un data frame, una lista dentro de un diccionario
df = pd.DataFrame({'partidos': partidos})
print(df)
#crear con los partidos un archivo csv (excel) con la info obtenida
df.to_csv('partidos.csv', index=False)