from bs4 import BeautifulSoup
import requests

#pagina web donde buscar
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#hacerlo mas bonito
print(soup.prettify())

#encontrar el texto
box = soup.find('article', class_='main-article')
#encontrar el titulo, al poner box.find se excluye todo lo que este fuera de ese box
title = box.find('h1').get_text()


#strip limpia la string antes y despues, separator hace de delimitador
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')


print(title)
print(transcript)

