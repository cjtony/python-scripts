#Con esta libreria podemos ver el contenido fuente de cualquier pagina y realizar peticiones como GET y POST. El metodo de requests.get nos devuelve también un código de status.
import requests as req
page_get = req.get("https://google.com")
#print(page_get)
import sys as sistem

#Bs4 nos permite la extracción de datos en concreto de una página web
from bs4 import BeautifulSoup
page = req.get('https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211')
soup = BeautifulSoup(page.content, 'html.parser')
soup_get = soup.find_all('h1')

if page.status_code == 200:
    print("correcto!")
else:
    print("falso")