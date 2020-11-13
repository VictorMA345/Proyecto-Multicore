from imports import *

def obtenerPrecioHB(url):
    try:
        usuario = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        url1 = requests.get(url,headers=usuario)
        soup = bs(url1.text,'html.parser')
        info =soup.findAll('script',attrs= {'type':'application/ld+json'})
        info_sel = info[0]
        info1 = str(info_sel.contents[0])
        precio = json.loads(info1)
        sacar = precio['offers'] 
        precio1 = sacar['price']
        return precio1
    except: 
        return 'juego no encontrado'
