import requests
from bs4 import BeautifulSoup as bs
import urllib.parse, urllib.error
import ssl
from urllib.request import Request, urlopen
import re
import pandas as pd
import json
def validarBusqueda(string):
    string = string.lower()
    string = string.replace(" ","-")
    string = string.replace("'","")
    return string
def obtenerinfoMetacritic(url):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers = user_agent)
    soup = bs(response.text, 'html.parser')
    lala = soup.find('script',attrs={"type":"application/ld+json"})
    info = str(lala.contents[0])
    info1 = json.loads(info)
    return info1
def busquedaMetacritic(juegoBuscado,tipo):
    try:
        tipoConsola = validarBusqueda(tipo)
        juego = validarBusqueda(juegoBuscado)
        urlJuego = 'https://www.metacritic.com/game/'+tipoConsola+"/"+juego
        dict1 = obtenerinfoMetacritic(urlJuego)
        return dict1
    except:
        return None
flag = True
plataformas = [ "playstation-4","pc","playstation-2","playstation","xbox-360","switch","xbox-one","ds","3ds","playstation-vita",
                "psp","wii","wii-u","game-boy-advance","xbox","nintendo-64","gamecube","dreamcast"]
while(flag):
    try:
        print("Digite el nombre del juego que desea buscar")
        juego = input()
        for tipo in plataformas:
            info = busquedaMetacritic(juego,tipo)
            if info != None:
                break
        print(info)
        print("¿Desea realizar otra busqueda?Si/No")
        respuesta = input()
        respuesta = respuesta.lower()
        if respuesta == "no":
            flag = False
    except:
        print("juego no encontrado, digite el nombre del juego correctamente")
        print("¿Desea realizar otra busqueda?Si/No")
        respuesta = input()
        respuesta = respuesta.lower()
        if respuesta == "no":
            flag = False



