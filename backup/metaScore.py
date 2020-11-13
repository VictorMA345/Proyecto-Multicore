from imports import *


def obtenerinfoMetacritic(url):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers = user_agent)
    soup = bs(response.text, 'html.parser')
    lala = soup.find('script',attrs={"type":"application/ld+json"})
    info1 = str(lala.contents[0])
    info = json.loads(info1)
    rate = info['aggregateRating']
    publicador1 = info['publisher']
    publicador = publicador1[0]
    genero = info['genre']
    info_Juego={'nombre':info['name'],'descripcion':info['description'],'puntaje':rate['ratingValue'],'desarrolladora': publicador['name']}
    return info_Juego