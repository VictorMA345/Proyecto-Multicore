import requests
from bs4 import BeautifulSoup as bs
import time
import threading
links =['https://www.metacritic.com/game/game-boy-advance/final-fantasy-tactics-advance',
'https://www.metacritic.com/game/game-boy-advance/the-legend-of-zelda-a-link-to-the-past',
'https://www.metacritic.com/game/playstation-3/killzone-2',
'https://www.metacritic.com/game/pc/bioshock',
'https://www.metacritic.com/game/pc/sid-meiers-civilization-v',
'https://www.metacritic.com/game/pc/borderlands-2',
'https://www.metacritic.com/game/pc/call-of-duty-4-modern-warfare',
'https://www.metacritic.com/game/pc/age-of-empires-ii-the-age-of-kings',
'https://www.metacritic.com/game/game-boy-advance/pokemon-emerald-version'
] 
def secuencial():
    info_secuencial= []
    info_div = []
    info_p = []
    info_a = []
    start = time.time()
    for url in links:
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url, headers = user_agent)
        soup = bs(response.text, 'html.parser')
        a = soup.findAll('a')
        p = soup.findAll('p')
        div = soup.findAll('div')
        info_div.append(div)
        info_a.append(a)
        info_p.append(p)
        info_secuencial.append(soup)
    end = time.time()
    print("el tiempo de ejecución secuencial duro: ")
    print(end - start," segundos")

def paralelo1():
    part = (len(links)//3)-1
    info_secuencial1= []
    info_div1 = []
    info_p1 = []
    info_a1 = []
    while(part != 0):
        url = links[part]
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url, headers = user_agent)
        soup = bs(response.text, 'html.parser')
        a = soup.findAll('a')
        p = soup.findAll('p')
        div = soup.findAll('div')
        info_div1.append(div)
        info_a1.append(a)
        info_p1.append(p)
        info_secuencial1.append(soup)
        part =part - 1

def paralelo2():
    part1 = len(links)//3
    part2 = ((len(links)//3) * 2)-1
    info_secuencial1= []
    info_div1 = []
    info_p1 = []
    info_a1 = []
    while(part2 != part1):
        url = links[part2]
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url, headers = user_agent)
        soup = bs(response.text, 'html.parser')
        a = soup.findAll('a')
        p = soup.findAll('p')
        div = soup.findAll('div')
        info_div1.append(div)
        info_a1.append(a)
        info_p1.append(p)
        info_secuencial1.append(soup)
        part2 =part2 - 1
  
def paralelo3():
    part1 = (len(links)//3)*2
    part2 = len(links)-1
    info_secuencial2= []
    info_div2 = []
    info_p2 = []
    info_a2 = []
    while(part2 != part1):
        url = links[part2]
        user_agent = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(url, headers = user_agent)
        soup = bs(response.text, 'html.parser')
        a = soup.findAll('a')
        p = soup.findAll('p')
        div = soup.findAll('div')
        info_div2.append(div)
        info_a2.append(a)
        info_p2.append(p)
        info_secuencial2.append(soup)
        part2 =part2 - 1
  

secuencial()
inicio = time.time()
hilo1 = threading.Thread(target=paralelo1)
hilo2 = threading.Thread(target=paralelo2)
hilo3 = threading.Thread(target=paralelo3)
hilo1.start()
hilo2.start()
hilo3.start()
hilo1.join()
hilo2.join()
hilo3.join()
fin = time.time() 
print("el tiempo de ejecución paralela duro: ")
print(fin - inicio," segundos")
