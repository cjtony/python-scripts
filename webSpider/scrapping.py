# Importamos librerías. #
import requests
import sys
import time 
 
from bs4 import BeautifulSoup
 
# Creamos nuestras listas. #
urls = []
urls2 = []
 
# Recibimos los argumentos. #
target_url = sys.argv[1] 
 
# Realizamos una conexión al argumento pasado y además, leemos todo el contenido del código fuente que existe en la página. #
url = requests.get(target_url).content
# Usamos nuestra librería de bs4 para posteriormente recatar lo que deseamos. #
soup = BeautifulSoup(url)
# Mediante el for y el método de bs4 llamado find_all, recolectamos todas las etiquetas donde existe a href. #
for line in soup.find_all('a'):
    new_line = line.get('href')
    try: 
        # Si existe en alguna línea del código fuente el http, lo almacenamos en nuestra lista llamada urls. #
        if new_line[:4] == "http": 
            if target_url in new_line: 
                urls.append(str(new_line)) 
        # Si no existe, intentamos combinar nuestro argumento(url de la página) + lo que encontramos. #
        elif new_line[:1] == "/": 
            try:
                comb_line = target_url+new_line 
                urls.append(str(comb_line))  
            except: 
                pass
        # Recorremos lo que hemos guardado anteriormente en nuestra lista(urls).
        for get_this in urls: 
                # Como dentro de urls están todos los enlaces, realizamos una conexión a dicha url y leemos el código fuente. #
            url = requests.get(get_this).content 
            # Usamos nuestra librería de bs4 para posteriormente recatar lo que deseamos. #
            soup = BeautifulSoup(url) 
            for line in soup.find_all('a'): 
                new_line = line.get('href') 
                try: 
                    if new_line[:4] == "http": 
                        if target_url in new_line:
                            urls2.append(str(newline)) 
                    elif new_line[:1] == "/": 
                        comb_line = target_url+new_line 
                        urls2.append(str(comb_line)) 
                except: 
                    urls_3 = set(urls2)
            # Recorremos nuestra lista llamada urls_3 e imprimimos todos los links de nuestro spider.
            for value in urls_3: 
                time.sleep(2)
                print("* Extracting " + str(value))
    except:
        pass
 
# Mortal_Poison -> https://www.youtube.com/VIINVIDEOSHD.
 
