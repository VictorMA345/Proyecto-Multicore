
import tiempoPasarJuego as tiempo
import playStationPrices as play
import metaScore
import precioHB as humble
import linksJuegos as juegos
from imports import json


def thread1():
    for var in range(0,len(juegos.juegos)//2):# range(0-14)
        que = Queue()
        hilo1 = threading.Thread(target = lambda q, arg1: q.put(obtenerinfoMetacritic(arg1)),args = (que,x['linkMetacritic'],))
        hilo2 = threading.Thread(target = lambda q, arg1: q.put(extraePrecioPlay(arg1)),args = (que,x['linkPlay'],))
        hilo3 = threading.Thread(target = lambda q,arg1: q.put(extraeTiempoPasar(arg1)),args = (que,x['linkHowLTB']))
        hilo1.start()
        hilo2.start()
        hilo3.start()
        hilo1.join()
        hilo2.join()
        hilo3.join()
        resultado1 = que.get()
        resultado2 = que.get()
        resultado3 = que.get()
        print(resultado1)
        print(resultado2)
        print(resultado3)

def thread2():
    for var in range(len(juegos.juegos)//2,len(juegos.juegos)):#range(15-29)
        que = Queue()
        hilo1 = threading.Thread(target = lambda q, arg1: q.put(obtenerinfoMetacritic(arg1)),args = (que,x['linkMetacritic'],))
        hilo2 = threading.Thread(target = lambda q, arg1: q.put(extraePrecioPlay(arg1)),args = (que,x['linkPlay'],))
        hilo3 = threading.Thread(target = lambda q,arg1: q.put(extraeTiempoPasar(arg1)),args = (que,x['linkHowLTB']))
        hilo1.start()
        hilo2.start()
        hilo3.start()
        hilo1.join()
        hilo2.join()
        hilo3.join()
        resultado1 = que.get()
        resultado2 = que.get()
        resultado3 = que.get()
        print(resultado1)
        print(resultado2)
        print(resultado3)


def precios():
    pass

