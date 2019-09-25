import urllib.request, sys, time, requests
from bs4 import BeautifulSoup

flag = False

try:
    url_target = sys.argv[1]
    url_defined = requests.get(url_target).status_code
    if url_defined == 200:
        flag = True
        print("\n***** CONTENT SEARCH ENGINE WORKING *****\n")
        url_defined = requests.get(url_target).content
        soup = BeautifulSoup(url_defined, 'html.parser')
        print("***** TITLE : " + str.upper(soup.title.string) + " *****\n")
        tags = soup('a')
        for tag in tags:
            time.sleep(2)
            print(" * Extracting href... " + tag.get('href') + " text: " + tag.text)
        print("\n***** NUMBER OF HREF FOUND: " + str(len(tags)) + " *****")
    else:
        print("\n***** SITE NOT ACCESSIBLE *****")
except:
    if flag != True:
        print("\n***** PAGE NOT FOUND VERIFY THAT THIS WRITTEN WELL *****")
    else:
        print("\n***** FINISHED PROGRAM *****")
