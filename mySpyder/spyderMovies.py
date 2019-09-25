import requests, sys, time, webbrowser
from bs4 import BeautifulSoup

flag = False
list_pages = []

try:
    url_target = sys.argv[1]
    url_defined = requests.get(url_target).status_code
    number_pages = int(input("Number of pages search: "))
    if url_defined == 200:
        search_pag = False
        if number_pages > 0:
            print("\n***** CONTENT SEARCH ENGINE WORKING PAGE *****\n")
            flag = True
            count = 0
            for i in range(1,number_pages + 1):
                if i != 1:
                    url_target = sys.argv[1] + "page/" + str(i) + "/"
                url_defined = requests.get(url_target).content
                soup = BeautifulSoup(url_defined, 'html.parser')
                print("||||| ***** TITLE : " + str.upper(soup.title.string) + " ***** |||||\n")
                tags = soup('a')
                for tag in tags:
                    if tag.img != None:
                        if tag.img.get('title') != None:
                            time.sleep(2)
                            print("[**] TITLE MOVIE: " + str(tag.img.get('title')) + ".\n   [*] LINK MOVIE: " + str(tag.get('href')) + "\n")
                            count += 1
            print("\n ***** NUMBER OF PAGES SEARCHED: " + str(number_pages) + ". TOTAL RESULTS: " + str(count) + ". *****")
    else:
        print("\n ***** SITE NOT ACCESSIBLE *****")
except:
    if flag != True:
        print("\n***** PAGE NOT FOUND VERIFY THAT THIS WRITTEN WELL *****")
    else:
        print("\n***** FINISHED PROGRAM *****")