import requests, sys, time, datetime
from bs4 import BeautifulSoup

url_defined = requests.get('https://www.milenio.com').content

try:
    print("||| Bienvenido usted podra ver noticias de la página milenio.com ||| ")
    print("*** Seleccione alguna de las siguientes opciones... ***")
    print("A). Portada.\nB). Noticias.\n")
    option = input("Opcion: ")
    soup =  BeautifulSoup(url_defined, 'html.parser')
    number_new = 0
    date_act = datetime.date.year
    print(str(date_act))
    print("\n")
    if option == 'A' or option == 'a':
        portrait = soup.find_all('div',{'class':'summary-container'})
        for port in portrait:
            portrait_title = port.a.getText()
            portrait_summary = port.find('div',{'class':'abstract'}).getText()
            print("[*] Titulo: " + str(portrait_title) + "[**] Descripcion: " + str(portrait_summary))
    elif option == 'B' or option == 'b':
        news = soup.find_all('div',{'class':'text'})
        for new in news:
            if new.a:
                if new.a.get('href') != None:
                    if new.find('div',{'class':'abstract'}) != None:
                        number_new += 1
                        time.sleep(2)
                        new_find = new.a.text
                        new_summary = new.find('div',{'class':'abstract'}).getText()
                        print("[*] Noticia numero: " + str(number_new) + "\n")
                        print("[**] Titulo: " + str(new_find))
                        print("[***] Descripción: " + str(new_summary))
        print("* Total de noticias encontradas: " + str(number_new) + " *")
    else:
        print("La opción introducida no es correcta...")
        sys.exit()
except KeyboardInterrupt:
    print("Programa terminado")
except Exception as Exot:
    print(Exot)