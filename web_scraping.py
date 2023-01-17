from bs4 import BeautifulSoup
import requests

#pagina web donde buscar
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text

#obtener el codigo html
soup = BeautifulSoup(content, 'lxml')
#hacerlo mas bonito y legible
print(soup.prettify())

#encontrar el texto usando las clases y palabras claves
box = soup.find('article', class_='main-article')
#encontrar el titulo, al poner box.find se excluye todo lo que este fuera de ese box
title = box.find('h1').get_text()


#limpia la string antes y despues y pone un espacio para delimitar
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

#imprimir en pantalla las variables creadas con el contenido
#print(title)
#print(transcript)

#para crear un archivo txt llamado file, en este caso de solo escritura, con el contenido de transcript
with open('titanic.txt', 'w') as file:
    file.write(transcript)

#Otra opcion en cuyo caso el nombre variaría con el nombre de la película:
""" with open(f'{title}.txt', 'w') as file:
    file.write(transcript) """