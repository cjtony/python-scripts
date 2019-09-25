#Con esta libreria podemos ver el contenido fuente de cualquier pagina y realizar peticiones como GET y POST. El metodo de requests.get nos devuelve también un código de status.
import requests as req
page_get = req.get("https://google.com")
#print(page_get)
import sys as sistem
import time

#Bs4 nos permite la extracción de datos en concreto de una página web
from bs4 import BeautifulSoup
page = req.get('https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211')
soup = BeautifulSoup(page.content, 'html.parser')
soup_get = soup.find_all('h1')
#print(soup_get)

#Se crean 2 listas
urls = []
urlsTwo = []

#Se reciben los argumentos
target_url = sistem.argv[1]

#Se reliza una conexion al argumento pasado y ademas lee todo el contenido de código fuente que existe en la página
flag = False
url_verify = req.get(target_url)
if url_verify.status_code == 200:
    flag = True

if flag:
    url = req.get(target_url).content
    soup_url = BeautifulSoup(url, 'html.parser')
    #Mediante el for y el método de bs4 llamado find_all, recolectamos todas las etiquetas donde existe a href.
    for line in soup_url.find_all('a'):
        new_line = line.get('href')
        try:
            #Si existe alguna línea del código fuente el http, lo almacenamos en nuestra lista llamada urls.
            if new_line[:4] == "http" or new_line[:4] == "https":
                if target_url in new_line:
                    urls.append(str(new_line))
            #Si no existe, intentamos combinar nuestro argumento(url de la página) +  lo que encontramos
            elif new_line[:1] == "/":
                try:
                    comb_line = target_url + new_line
                    urls.append(str(comb_line))
                except:
                    pass
            #Recorre lo que se guarda anteriormente en la lista urls
            for get_this in urls:
                #Dentro de urls están todos los enlaces, se realiza una conexion a dicha url y se lee el código fuente
                url = req.get(get_this).content
                #Usamos nuestra librería de bs4 para posteriormente recatar lo que deseamos
                soup_url = BeautifulSoup(url, 'html.parser')
                for line in soup_url.find_all('a'):
                    new_line = line.get('href')
                    try:
                        if new_line[:4] == "http" or new_line[:4] == "https":
                            if target_url in new_line:
                                urlsTwo.append(str(new_line))
                        elif new_line[:1] == "/":
                            comb_line = target_url + new_line
                            urlsTwo.append(str(comb_line))
                    except:
                        urlsTrh = set(urlsTwo)
                #Recorre la lsita urlTrh e imprime todos los links de nuestro spider
                for value in urlsTrh:
                    time.sleep(2)
                    print("Extracting url... " + value)
        except:
            pass